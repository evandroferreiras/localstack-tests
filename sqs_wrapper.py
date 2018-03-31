import boto3
import json

def __init_sqs():
    return boto3.resource('sqs', endpoint_url="http://localhost:4576") 


def create_queue():
    sqs = __init_sqs()
    sqs.create_queue(QueueName='teste')


def __get_queue_by_name(name):
    sqs = __init_sqs()
    return sqs.get_queue_by_name(QueueName=name)


def send_json(msg):
    queue = __get_queue_by_name('teste')
    queue.send_message(MessageBody= json.dumps(msg))


def return_all():
    queue = __get_queue_by_name('teste')
    messages = queue.receive_messages()
    result = []
    while len(messages) > 0:
        message = messages[0]
        json_returned = json.loads(message.body)
        result.append(json_returned)        
        message.delete()
        messages = queue.receive_messages()
    return result