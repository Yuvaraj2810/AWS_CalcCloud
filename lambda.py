# import the JSON utility package
import json
# import the Python math library
import math

# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('PowerofMaths-DB')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    base = int(event['base'])
    exponent = int(event['exponent'])
    operation = event['operation']

    if operation == 'power':
        result = math.pow(base, exponent)
    elif operation == 'add':
        result = base + exponent
    elif operation == 'subtract':
        result = base - exponent
    elif operation == 'divide':
        result = base / exponent if exponent != 0 else 'undefined'
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation')
        }

    # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(result),
            'LatestGreetingTime': now
        })

    # return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(result))
    }
