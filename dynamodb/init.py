import boto3
import constant

dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')

def createTable():
    waiter = dynamodb_client.get_waiter('table_not_exists')
    waiter.wait(TableName=constant.TABLE_OFFERS)
    print('creating table')

    table = dynamodb.create_table(
        TableName=constant.TABLE_OFFERS,
        KeySchema=[
            {
                'AttributeName': 'url',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'url',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName=constant.TABLE_OFFERS)
    print("Tables created")


def deleteTable():
    print('deleting table')
    return dynamodb_client.delete_table(TableName=constant.TABLE_OFFERS)


deleteTable()
createTable()
