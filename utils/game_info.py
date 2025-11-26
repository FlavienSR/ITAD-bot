import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") 

def game_id(name):
    req = requests.get("https://api.isthereanydeal.com/games/lookup/v1",params={"key": API_KEY,"title":name})
    return req.json()["game"]["id"]

def game_info(name):
    gid=game_id(name)
    req = requests.get("https://api.isthereanydeal.com/games/info/v2",params={"key": API_KEY,"id":gid})
    return req.json()
