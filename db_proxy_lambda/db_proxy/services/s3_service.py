import os
import uuid
import boto3
from botocore.exceptions import ClientError
import logging

def upload_file_to_s3(file_path):
    s3 = boto3.resource('s3')
    object_name = str(uuid.uuid4())+".csv"
    bucket_name = os.getenv("S3_BUCKET_NAME")
    bucket = s3.Bucket(bucket_name)
    try:
        bucket.put_object(Key=object_name,Body=file_path)
        return object_name
    except ClientError as e:
        logging.error(e)
        return None


