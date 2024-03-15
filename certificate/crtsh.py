import requests 
import json 
from pprint import pprint as pp 

def writeToFile(fname,listObj): 
    with open(fname,"w") as f:
        for item in listObj:
            if type(item) != 'str':
                f.write(str(item))
                f.write('\n')
            else: 
                f.write(item.strip())
                f.write('\n')

url = 'https://crt.sh'
cn = input('Please enter the common name you want to search for: ') 

# The query structure is for a very basic query in JSON format for non-expired certificates for a given Common Name. 
q = {
    "CN": cn,
    "output": "json",
    "exclude": "expired"
}

domains = []
id = []
r = requests.get(url,params=q) 
data = r.text
pp(json.loads(data))

# The below is a tricky line of code. It is a LIST COMPREHENSION. 
# It appends to domains list a domain that is not already present. Note, we use JSON.LOADS to convert string into python structure. 
[domains.append(x['name_value']) for x in json.loads(data) if x['name_value'] not in domains] 
[id.append(x['id']) for x in json.loads(data) if x['id'] not in id]

writeToFile('domain-list.txt', domains)
writeToFile('crt-id.txt', id) 

cont = input('Do you wish to continue to extract certificates? (y/Y)')
if cont.upper() == 'Y':
    with open('crt-id.txt','r') as f:
        crtid = f.readlines()
    
    for cid in crtid:
        x = cid.strip()
        q = {
            "id":int(x),
        }

        r = requests.get(url, params=q) 
        print(r.text)