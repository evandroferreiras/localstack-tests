import boto3
from boto3.dynamodb.conditions import Key, Attr

def __init_dynamodb():
    return boto3.resource('dynamodb', endpoint_url="http://localhost:4569")

def __return_table():
    dynamodb = __init_dynamodb()
    return dynamodb.Table('math_expressions')

def create_table():
    
    client = boto3.client('dynamodb', endpoint_url="http://localhost:4569")
    existing_tables = client.list_tables()['TableNames']

    if 'math_expressions' not in existing_tables:
        dynamodb = __init_dynamodb()
        table = dynamodb.create_table(
            TableName='math_expressions',
            KeySchema=[
                {
                    'AttributeName': 'first_number',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'second_number',
                    'KeyType': 'RANGE'
                }            
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'first_number',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'second_number',
                    'AttributeType': 'N'
                }           
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        table.meta.client.get_waiter('table_exists').wait(TableName='math_expressions')


def send_data(data):
    table = __return_table()
    table.put_item(
        Item=data
    )

def return_data():
    table = __return_table()
    response = table.scan(
        FilterExpression=Attr('first_number').gt(0)
    )
    return response['Items']
