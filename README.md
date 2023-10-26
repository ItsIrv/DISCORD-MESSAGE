# DISCORD LAMBDA

This AWS Lambda Function is used to send messages to a Discord channel.

## Setup

The only set up needed is the .env file. If you're using the deploy Github script, you need to set up the AWS environtment variables.

## Functionality

To send a message to your discord webhook, you can send a POST request with the following JSON payload.

```json
    {
        "message": "<MESSAGE TO SEND TO CHAT>"
    }
```
