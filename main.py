import requests
import random
import json
import time
import re
import threading
Proxies = []
tokens = []
channels = [] #if suggested enough, I will make a function for automatically grabbing server channel IDs
serverID = ''

with open('proxies.txt') as p:
    a = p.readlines()
    for proxy in a:
        Proxies.append('http://'+proxy.rstrip())

with open('tokens.txt') as p:
    a = p.readlines()
    for proxy in a:
        tokens.append(proxy.rstrip())

#messy code, threw it together quick in as little lines as possible

def request(proxies, token, channel):
    baseURL = f'https://discord.com/api/v8/channels/{channel}/invites'
    headers = {"Authorization": token, "User-Agent":"Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>",
            "Content-Type":"application/json"}
    POSTedJSON =  json.dumps({'max_age': random.randrange(4000, 86300), 'max_uses': 0,'target_type': None, 'temporary': False})
    time.sleep(1)
    a = requests.post(baseURL, headers = headers, proxies=proxies, data=POSTedJSON).json()
    print(a)

def run(proxies, token, channel):
    while True:
        time.sleep(3) #this will allow the tokens to generate invites in the most efficient way
        request(proxies, token, channel)

for token in tokens:
    proxies={"https":random.choice(Proxies)}
    x = threading.Thread(target=run, args=(proxies, token, random.choice(channels)))
    x.start()