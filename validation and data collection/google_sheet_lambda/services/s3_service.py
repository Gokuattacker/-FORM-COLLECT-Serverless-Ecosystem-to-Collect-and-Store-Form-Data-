import json
import os
import logging
import boto3
from botocore.exceptions import ClientError


def get_csv_from_s3(object_name):
    s3_client = boto3.client('s3')
    bucket_name = os.getenv("CSV_S3_BUCKET_NAME")
    
    try:
        csv_object = s3_client.get_object(Bucket=bucket_name, Key=object_name)
        csv_content = csv_object['Body'].read()
        return csv_content
    except ClientError as e:
        print(e)
        return None

def delete_csv_from_s3(object_name):
    s3_client = boto3.client('s3')
    bucket_name = os.getenv("CSV_S3_BUCKET_NAME")
    
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        return "Deleted"
    except ClientError as e:
        print(e)
        return None


def get_google_credentials_from_s3():
    s3_client = boto3.client('s3')
    bucket_name = os.getenv("GOOGLE_CREDENTIALS_S3_BUCKET")
    object_name = os.getenv("GOOGLE_CREDENTIALS_OBJECT_KEY_NAME")

    try:
      json_object = s3_client.get_object(Bucket=bucket_name, Key=object_name) 
      json_object_data = json_object['Body'].read().decode('utf-8')

      return json.loads(json_object_data)
    except ClientError as e:
        print(e)
        return None




