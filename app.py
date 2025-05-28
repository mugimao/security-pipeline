import json

def handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps('Hello again from Lambda new!')
    }