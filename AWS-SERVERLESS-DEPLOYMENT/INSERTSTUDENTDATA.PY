import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentdata')

def lambda_handler(event, context):

    table.put_item(
        Item={
            'studentid': event['studentid'],
            'name': event['name'],
            'class': event['class'],
            'age': event['age']
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps("Data saved!")
    }
