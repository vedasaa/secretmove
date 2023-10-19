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

def getTarget(handle):
    url = "https://api.starsarena.com/user/handle?handle="+handle

    h={
        "Accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiODc5ZWRjZGUtYzQyYy00NGViLWEyYjYtYWU5YzMzNWY2ZGY5IiwidHdpdHRlcklkIjoiODQ1MzcwMTE3ODY1MTQ0MzIwIiwidHdpdHRlckhhbmRsZSI6ImRpbDJ6dnBuY3Rhd3YiLCJ0d2l0dGVyTmFtZSI6IlNlcnZhbnQgdGlwIiwidHdpdHRlclBpY3R1cmUiOiJodHRwczovL3Bicy50d2ltZy5jb20vcHJvZmlsZV9pbWFnZXMvMTcxMjU3NTU0MjQyNjQ5NzAyNC9IeHJhQzdYc19ub3JtYWwuanBnIiwiYWRkcmVzcyI6IjB4ZDUyMmZkZjA1MDgxOERGQTgzQjE2RWI4MkE3MWY5N2ZjOTJBMDlhNiJ9LCJpYXQiOjE2OTc2MDg5OTcsImV4cCI6MTcwNjI0ODk5N30.VHDbWLyFYxgMwIkIG0x9RKgVL-0WbcrqAM-vZwJAQWKwhW5-U5DREmVQNO5ltQUOpcwNTGkB4BaSWEI8OsJ8pz-idQtiLfokMpZuho9opxlcRvEoLo6yOsDsoUwz8tpcjHfxnPjLPSK5afdc_QmYVK9J0839d9H5q6sCh_rHROT3sg5sd_QK1SdpldeLkDg1xY1A0Nujnh1TmBumuiFnBPtXIZQTJ4-PcBat9IPJi9-DiQQvDktWvcei5heLzfDwneYcSACF0loTeVMdrRAo5noHfAw9oBmfcP6dkssf7OVnQHKYrULHW5RQKUH2Fja_3uj4UlFp5O2pKTdusIeCz_2yJTNDJVpXDK-B3Xd-TB05BRpJLwEEgcloQBhc66Ik_i5VbgrNgeV5pNKtspK_Y9Zx9Cu4YXc9ZFM1NelbLhhs5U7LVE4TCV93oVJCEnP3aCrdWtgoIZHS8cc5AYa7Tv8HM6dePUJqgxct5ixMtFKvexoTdj-j1Xcc9ZwwyyO2b-nVBAug4ufsUYJRktmLoi8jT5hiIYIBkwqO6m8YfWCk4q_-YFJUBxXu9Say-K50zPKJuj-aCjbiNIY6W-9xckNHtQtk26O2f79zXxpzF5jooCBnwqOWnsV2iMl18vRrL8yB0Wb1HoPiClKHBbCTwmaGPlaJGB1cHACFDp-abxI",
        "Referer": "",
        "Sec-Ch-Ua": '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
    }

    result = requests.get(url, headers=h)
    return result

def getBuy(address):
    url = "https://api.starsarena.com/trade/buy"

    h = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiODc5ZWRjZGUtYzQyYy00NGViLWEyYjYtYWU5YzMzNWY2ZGY5IiwidHdpdHRlcklkIjoiODQ1MzcwMTE3ODY1MTQ0MzIwIiwidHdpdHRlckhhbmRsZSI6ImRpbDJ6dnBuY3Rhd3YiLCJ0d2l0dGVyTmFtZSI6IlNlcnZhbnQgdGlwIiwidHdpdHRlclBpY3R1cmUiOiJodHRwczovL3Bicy50d2ltZy5jb20vcHJvZmlsZV9pbWFnZXMvMTcxMjU3NTU0MjQyNjQ5NzAyNC9IeHJhQzdYc19ub3JtYWwuanBnIiwiYWRkcmVzcyI6IjB4ZDUyMmZkZjA1MDgxOERGQTgzQjE2RWI4MkE3MWY5N2ZjOTJBMDlhNiJ9LCJpYXQiOjE2OTc2MDg5OTcsImV4cCI6MTcwNjI0ODk5N30.VHDbWLyFYxgMwIkIG0x9RKgVL-0WbcrqAM-vZwJAQWKwhW5-U5DREmVQNO5ltQUOpcwNTGkB4BaSWEI8OsJ8pz-idQtiLfokMpZuho9opxlcRvEoLo6yOsDsoUwz8tpcjHfxnPjLPSK5afdc_QmYVK9J0839d9H5q6sCh_rHROT3sg5sd_QK1SdpldeLkDg1xY1A0Nujnh1TmBumuiFnBPtXIZQTJ4-PcBat9IPJi9-DiQQvDktWvcei5heLzfDwneYcSACF0loTeVMdrRAo5noHfAw9oBmfcP6dkssf7OVnQHKYrULHW5RQKUH2Fja_3uj4UlFp5O2pKTdusIeCz_2yJTNDJVpXDK-B3Xd-TB05BRpJLwEEgcloQBhc66Ik_i5VbgrNgeV5pNKtspK_Y9Zx9Cu4YXc9ZFM1NelbLhhs5U7LVE4TCV93oVJCEnP3aCrdWtgoIZHS8cc5AYa7Tv8HM6dePUJqgxct5ixMtFKvexoTdj-j1Xcc9ZwwyyO2b-nVBAug4ufsUYJRktmLoi8jT5hiIYIBkwqO6m8YfWCk4q_-YFJUBxXu9Say-K50zPKJuj-aCjbiNIY6W-9xckNHtQtk26O2f79zXxpzF5jooCBnwqOWnsV2iMl18vRrL8yB0Wb1HoPiClKHBbCTwmaGPlaJGB1cHACFDp-abxI",
        "Referer": "",
        "Sec-Ch-Ua": '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
    }

    result = requests.post(url, json={"address": address, "amount": "6600000000000000"}, headers=h)
    return result

option = False
while option != True :
    handleTarget = input("Masukan Target : ")
    addressTarget = getTarget(handleTarget).json()["user"]["address"]
    buyTarget = getBuy(addressTarget).json()
    print(buyTarget)
    optionuser = input("Mau run lagi tidak (y/n) : ")
    if optionuser == "y":
        option = False
    else:
        option = True
        print("See you . . . ")