import random
"""
    vedpratama x SGBTEAM
    vedasaa
"""
import requests
import json
import os
import time
import re
import html
import socket
import struct

def checking():
    url = 'https://api.trustlessbridge.io/api/estimate-withdraw-fee'

    h={
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
    }
    result = requests.post(url, json={"isBridgeLayer": False,"tcAddress":"0x60992096FfA675eb58ceDb4536C88259C5983f14","tcTokenID":"0x111808abe352c8003e0effcc04998eab26cebe3c"}, headers=h)
    return result

token = '6500087622:AAEpWkKybAcDhzeV685-Ht88njub6biTtbw'
userID = '648235175'
tele = f'https://api.telegram.org/bot{token}/sendMessage'
while True:
    #result = float(checking().json()["data"]["withdrawFee"])/1000000000000000000
    print(checking().text)
    target = 20000000000000/1000000000000000000
    
