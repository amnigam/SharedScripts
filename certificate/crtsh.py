import requests 
from pprint import pprint as pp 
import crtobj
import argparse 
import os

url = 'https://crt.sh'

def makeRequest(query):
    r = requests.get(url,params=query) 
    data = r.text
    c = crtobj.Cert(data, args.output) 
    d = c.extractDomains()
    pp(d)
    return c 

def downloadCertificate(certObj):
    cont = input('Do you wish to continue to extract certificates? (y/Y)')
    if cont.upper() == 'Y':
        crtid = certObj.getcrtid()
        for cid in crtid:
            q = {
                "d":cid,        # To download certificate you need to send query parameter d with CRTID. 
            }
            basedir = os.path.abspath(os.path.dirname(__file__)) 
            outFolder = 'CRT-Output'
            path = os.path.join(basedir,outFolder,f'{cid}-cert.crt')    # Write inside CRT-Output folder in its own cert file. 

            r = requests.get(url, params=q, stream=True)    # Use STREAM to download. 
            if r.status_code == 200:
                with open(path, 'wb') as b:    # Write it into its own certificate file. 
                    b.write(r.raw.read())

# Setting up the script's options. 
parser = argparse.ArgumentParser(description='Script that crawls CRT.SH to obtain subdomains, certificates and other data.') 
parser.add_argument('-cn', '--commonName', type=str, help='Search on the basis of Common Name (CN)')
parser.add_argument('-i', '--identity', type=str, help='Search on the basis of Identity')
parser.add_argument('-e', '--expired', action='store_false', default=True, help='Exclude Expired certificates. By default, it is True. Setting this flag makes it False.') 
parser.add_argument('-o', '--output', type=str, default='domain-list.txt', help='Output File Name to capture domain list.')
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
    crt = makeRequest(q) 
    downloadCertificate(crt)

if args.identity:
    # The query structure is for a very basic query in JSON format for non-expired certificates for a supplied Identity Value. 
    if (args.expired):
        q = {
            "Identity": args.identity,
            "output": "json",
            "exclude": "expired"
        }
    else:
        q = {
            "Identity": args.identity,
            "output": "json"
        }
    crt = makeRequest(q) 
    downloadCertificate(crt)    