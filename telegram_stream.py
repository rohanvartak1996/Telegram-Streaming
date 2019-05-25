from telethon import TelegramClient, events
from pymongo import MongoClient
import datetime
import pandas as pd
import yaml
import os

channels = pd.read_csv('telegram_channels.csv')
channels = tuple(channels['Channels'])

if os.path.isfile("config.yml"):
    with open("config.yml", 'r') as ymlfile:
        config_file = yaml.load(ymlfile)
        
        
api_id = config_file['API_ID']
api_hash = config_file['API_HASH']

mongo_client = MongoClient('mongodb://localhost/telegramdb')
db = mongo_client.telegramdb
collection = db.my_collection

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    print(event.raw_text)                        # to check if the message is recived
    collection.insert_one({'id':event.message.id, 'text':event.message.message})   # inserting into mongodb
    

await client.start()
await client.run_until_disconnected()

