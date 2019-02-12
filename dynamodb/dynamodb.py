import boto3
import botocore
import json

dynamodb = boto3.resource('dynamodb')
dynamoDBClient = boto3.client('dynamodb')


def put_item(table, object):
    table = dynamodb.Table(table)
    response = table.put_item(
        Item=object
    )
    #print response

def get_item(table, object):
    table = dynamodb.Table(table)
    response = table.get_item(
        Key=object
    )
    return response['Item'] if 'Item' in response else None

def item_count(table):
    table = dynamoDBClient.describe_table(
        TableName=table
    )
    #print table
    return table['ItemCount']