import requests 
from dotenv import load_dotenv 
import os 
import json 

load_dotenv() 

API_KEY = os.environ.get('API_KEY') 
API_ENDPOINT = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

def check_url_safety(urls : list):
    """
    Checks a list of URLs against the Google Safe Browse API.
    Args:
        urls (list): A list of URLs (strings) to check.
    Returns:
        dict: A dictionary containing the API response.
              Returns an empty dict if no matches are found.
    """
    if not isinstance(urls, list):      # If entered argument is not a list make it.
        urls = [urls] # Ensure it's always a list

    threat_entries = [{"url": url} for url in urls]     # Get it in the format Google wants.
    request_body = {
        "client": {
            "clientId": "PhishingTester", # Replace with your application's name
            "clientVersion": "1.0.0"             # Replace with your application's version
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE",      # Keeping this value for drive by malwares. 
                "SOCIAL_ENGINEERING", # This is for phishing links
                # "UNWANTED_SOFTWARE",                      # Commented it out for this use case. 
                # "POTENTIALLY_UNWANTED_APPLICATION"        # Commented it out for this use case.
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": threat_entries
        }
    }
    headers = {"Content-type": "application/json"}

    try:
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(request_body))
        # print(response.status_code)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        
        response_data = response.json()
        return response_data

    except requests.exceptions.HTTPError as err_h:
        print(f"HTTP Error: {err_h}")
    except requests.exceptions.ConnectionError as err_c:
        print(f"Error Connecting: {err_c}")
    except requests.exceptions.Timeout as err_t:
        print(f"Timeout Error: {err_t}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    
    return {} # Return empty on error