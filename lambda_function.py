import sys
from json import dumps, loads
from os import environ

sys.path.append('./packages')

import requests   # noqa: E402


def lambda_handler(event, context):
    """
    Posts a message to a Discord webhook URL.

    Args:
        url (str): The Discord webhook URL.
        message (str): The message to post.

    Returns:
        None
    """

    if 'body' in event:
        event = loads(event['body'])

    url = environ.get('DISCORD_WEBHOOK_URL')

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=dumps(event))

    return {
        'statusCode': 200 if response.status_code == 204 else response.status_code,
        'body': dumps(event)
    }
