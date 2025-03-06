import json

def lambda_handler(event, context):
    data = {
        "timestamp": "2025-03-06T07:11:49.027049",
        "temperature": 20.9,
        "humidity": 83,
        "location": "Bangalore"
    }
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
