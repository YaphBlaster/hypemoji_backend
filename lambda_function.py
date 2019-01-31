import json

import requests
from io import BytesIO


def lambda_handler(event, context):

    # # TODO implement
    return {
        'statusCode': 200,
        'body': requests.get('https://api.bitmoji.com/content/templates').json()
    }
