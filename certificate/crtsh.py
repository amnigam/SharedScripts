import requests 
from pprint import pprint as pp 
import crtobj
import argparse 

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

# Setting up the script's options. 
parser = argparse.ArgumentParser(description='Script that crawls CRT.SH to obtain subdomains, certificates and other data.') 
parser.add_argument('-cn', '--commonName', type=str, help='Common Name to be looked up')
parser.add_argument('-e', '--expired', action='store_false', default=True, help='Exclude Expired certificates. By default, it is True. Setting this flag makes it False.') 
parser.add_argument('-o', '--output', type=str, help='Output File Name')
args = parser.parse_args()

if args.commonName:
    # print(args.expired)
    # The query structure is for a very basic query in JSON format for non-expired certificates for a given Common Name. 
    q = {
        "CN": args.commonName,
        "output": "json",
        "exclude": args.expired
    }

    r = requests.get(url,params=q) 
    data = r.text
    c = crtobj.Cert(data) 
    d = c.extractDomains()
    # pp(json.loads(data))
    pp(d)

# [id.append(x['id']) for x in json.loads(data) if x['id'] not in id]

# writeToFile('domain-list.txt', domains)
# writeToFile('crt-id.txt', id) 

# cont = input('Do you wish to continue to extract certificates? (y/Y)')
# if cont.upper() == 'Y':
#     with open('crt-id.txt','r') as f:
#         crtid = f.readlines()
    
#     for cid in crtid:
#         x = cid.strip()
#         q = {
#             "id":int(x),
#         }

#         r = requests.get(url, params=q) 
#         print(r.text)