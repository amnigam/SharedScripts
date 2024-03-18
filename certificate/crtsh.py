import requests 
from pprint import pprint as pp 
import crtobj
import argparse 

url = 'https://crt.sh'

# Setting up the script's options. 
parser = argparse.ArgumentParser(description='Script that crawls CRT.SH to obtain subdomains, certificates and other data.') 
parser.add_argument('-cn', '--commonName', type=str, help='Common Name to be looked up')
parser.add_argument('-e', '--expired', action='store_false', default=True, help='Exclude Expired certificates. By default, it is True. Setting this flag makes it False.') 
parser.add_argument('-o', '--output', type=str, help='Output File Name')
args = parser.parse_args()

if args.commonName:
    # The query structure is for a very basic query in JSON format for non-expired certificates for a given Common Name. 
    if (args.expired):
        q = {
            "CN": args.commonName,
            "output": "json",
            "exclude": "expired"
        }
    else:
        q = {
            "CN": args.commonName,
            "output": "json"
        }

    r = requests.get(url,params=q) 
    data = r.text
    c = crtobj.Cert(data) 
    d = c.extractDomains()
    pp(d)

    cont = input('Do you wish to continue to extract certificates? (y/Y)')

    if cont.upper() == 'Y':
        crtid = c.getcrtid()
        for cid in crtid:
            q = {
                "d":cid,        # To download certificate you need to send query parameter d with CRTID. 
            }

            r = requests.get(url, params=q, stream=True)    # Use STREAM to download. 
            if r.status_code == 200:
                with open(f'{cid}-cert.crt', 'wb') as b:    # Write it into its own certificate file. 
                    b.write(r.raw.read())