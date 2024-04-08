import requests 
import ssl 
import socket
import os 
from Cryptodome.PublicKey import RSA
from cryptography import x509 
from cryptography.hazmat.primitives.asymmetric import rsa 
import json 

basedir = os.path.abspath(os.path.dirname(__file__)) 
outFolder = 'CRT-Output'
keyOut = 'KeyDiagnostics.txt' 

def getPublicKeyData(cert,domain):
    keyData = {}
    keyData['domain'] = domain 
    c = x509.load_pem_x509_certificate(cert.encode('utf-8')) 
    alg = isinstance(c.public_key(),rsa.RSAPublicKey)
    if alg: 
        keyData['algorithm'] = 'RSA Algorithm'
        key = RSA.import_key(cert) 
        n = key.n 
        e = key.e 
        key_length = n.bit_length() 
        keyData['key-length'] = key_length
        print(f'[+] Key Length is: {key_length} ')
        if key_length < 2048:
            keyData['NIST-approved-length'] = 'No'
            return keyData
        else:
            keyData['NIST-approved-length'] = 'Yes'
            return keyData
    else:
        keyData['algorithm'] = 'Elliptic Curve'
        return keyData

def makeRequest(cert,keyinfo):
    NO_VULN = 'This key is not affected by any of the vulnerabilities that we can detect!' 
    url = 'https://badkeys.info/check/'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'Accept-Language: en-US,en;q=0.5'
    }
    formData = {
        "inkey": cert
    }
    r = requests.post(url, headers=headers, data=formData) 
    if NO_VULN in r.text: 
        print('[+] The Certificate & Public Key look good. ')
        keyinfo['vulnerability'] = 'Not Vulnerable'         # keyinfo is a dictionary passed by reference. Change will reflect in original.
    else:
        print('[+] Insecure / Invalid key. ')
        keyinfo['vulnerability'] = 'Vulnerable'
    # print(r.text) 

def writeCertToFile(domain,cert,l):
    certPath = os.path.join(basedir,outFolder,f'{domain}-cert.txt')
    keylen = l['key-length'] 
    with open(certPath,"w") as f:
        if l.get("key-length") < 2048:
            f.write(f'[+] Primary Key Length ({keylen}) extracted from certificate for domain {domain} is less than 2048 bits.\n')
        else:
            f.write(f'[+] Primary Key Length ({keylen}) extracted from certificate for domain {domain} is NIST approved.\n')
        f.write(cert)       
    keyPath = os.path.join(basedir,outFolder,keyOut)
    with open(keyPath,"a") as f:
        f.write('*'*60 + '\n')
        f.write(f'[+] Key Data for Domain {domain} \n')
        f.write(json.dumps(l,indent=2) + '\n') 
        f.write('*'*60 + '\n')

def testkey(domain,port=443):
    try:
        cert = ssl.get_server_certificate((domain,port)) 
        l = getPublicKeyData(cert,domain)
        # print(f'First => {cert}') 
        makeRequest(cert,l)     
        writeCertToFile(domain,cert,l) 
    except ssl.SSLError as e:
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain,port)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    certDer = ssock.getpeercert(True) 
                    cert = ssl.DER_cert_to_PEM_cert(certDer) 
                    l = getPublicKeyData(cert,domain)
                    makeRequest(cert,l)
                    writeCertToFile(domain,cert,l)
                    # print(f'Second => {cert}') 
        except Exception as e:
            print(f'Error {e}') 
    except Exception as e:
        print(f'Error Encountered..... {e}') 

# testkey('ey.com')
fname = input('[+] Enter the file containing domain list: ')
path = os.path.join(basedir,outFolder,f'{fname}')
with open(path, "r") as f:
    domains = f.readlines() 

for dom in domains:
    x = dom.strip()
    if x:
        print(f'[+] Testing Certificate for domain {x}')
        testkey(x)
        print('*'*60)