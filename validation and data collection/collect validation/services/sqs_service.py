import boto3
import os

sqs = boto3.client('sqs',region_name=os.environ.get("REGION_NAME"))

def send_message_to_sqs_service(message_body):
    sqs_queue_name = os.environ.get("SQS_QUEUE_NAME")
    assert(type(sqs_queue_name) != None)

    sqs.send_message(
        QueueUrl=sqs_queue_name,
        MessageBody=message_body
    )

