from configobj import ConfigObj
import requests
import json
from hashlib import sha1

config = ConfigObj("config.ini")
API_SECRET = config["Authorization"]["API_SECRET"]
APP_KEY = config["Authorization"]["APP_KEY"]
BASE_URL = config["Url"]["BASE_URL"]
AUTH_TOKEN = [APP_KEY, API_SECRET]


def signature(secret, key, data={}):
    str_ = secret + key + json.dumps(data, separators=(',', ':'))
    return sha1(str_.encode()).hexdigest()

def get(base_url, auth, uuid_):
    url_ = base_url + f"/api/v1/transactions/{uuid_}"
    headers = {
        "Application-id": auth[0],
        "Signature": signature(auth[1], auth[0]),
        "Content-Type": "application/json"
    }
    return requests.get(url_, headers=headers).json()

def put(base_url, auth, uuid_):
    url_ = base_url + f"/api/v1/transactions/{uuid_}"
    headers = {
        "Application-id": auth[0],
        "Signature": signature(auth[1], auth[0]),
        "Content-Type": "application/json"
    }
    return requests.put(url_, headers=headers).json()

def delete(base_url, auth, uuid_):
    url_ = base_url + f"/api/v1/transactions/{uuid_}"
    headers = {
        "Application-id": auth[0],
        "Signature": signature(auth[1], auth[0]),
        "Content-Type": "application/json"
    }
    return requests.delete(url_, headers=headers).json()

def post(base_url, auth, data):
    headers = {
        "Application-id": auth[0],
        "Signature": signature(auth[1], auth[0], data),
        "Content-Type": "application/json"
    }
    url_ = base_url + f"/api/v1/transactions"
    return requests.post(url_, headers=headers, json=data).json()