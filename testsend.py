import requests
import os

# GroupMe Bot ID
botID = "93ea5208d4fb6bdfb5386ab2a3"  # insert your Bot ID here

# construct and send the post
postData = {'bot_id': botID,
            'text': "This is a test message :)"}

r = requests.post('https://api.groupme.com/v3/bots/post', data=postData)
print(r)