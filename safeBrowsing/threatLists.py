import requests 
from dotenv import load_dotenv 
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY') 
print(API_KEY)

url = f'https://safebrowsing.googleapis.com/v4/threatLists?key=API_KEY'
header = {
    "Content-type": "application/json"
}

r = requests.get(url) 
print(r.text) 