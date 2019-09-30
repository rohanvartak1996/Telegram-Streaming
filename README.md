# Telegram Streaming

This is a python program to collect messages from various telegram channels. Here I make use of Telegram API to stream the messages from multiple channels of Telegram. Here I present both the Jupyter Notebook and Python program for streaming messages. The Python program can be run on a AWS machine continually to stream messages.

## Installing Requirements

Install telethon

```
pip install telethon
```
Create a application in telegram to obtain the API Id and Hash.

https://core.telegram.org/api/obtaining_api_id

Put API Id and Hash in the config.yml file.

You need to have MongoDb installed to connect and store the messages. Any other database can be used in place of it.

## Running the code

You need to have a Telegram account to run the code.

When you run the file in Jupyter, Telegram will ask you to login using your account information. You will recieve a code on your telegram which you need to enter.

Same login will be required when running the python file.

The 'me channel has been added to the list of telegram channels.

All the messages will be saved to your MongoDb. 

To run the python file:
```
python telegram-stream.py
```

## Testing

Send a message to yourself using the 'Saved Messages' on your telegram and the messages will be streamed instantly.


