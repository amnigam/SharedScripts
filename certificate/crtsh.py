import requests 
import json 
from pprint import pprint as pp 

url = 'https://crt.sh'
cn = input('Please enter the common name you want to search for: ') 

# The query structure is for a very basic query in JSON format for non-expired certificates for a given Common Name. 
q = {
    "CN": cn,
    "output": "json",
    "exclude": "expired"
}

domains = []
r = requests.get(url,params=q) 
data = r.text

# The below is a tricky line of code. It is a LIST COMPREHENSION. 
# It appends to domains list a domain that is not already present. Note, we use JSON.LOADS to convert string into python structure. 
[domains.append(x['name_value']) for x in json.loads(data) if x['name_value'] not in domains] 

with open("domain-list.txt", "w") as f:
    for d in domains:
        f.write(d.strip())
        f.write('\n') 
