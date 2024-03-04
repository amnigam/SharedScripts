import requests 
import ssl 
import socket

def makeRequest(cert):
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
    print(r.request.url)
    # print(r.request.body)
    print(r.request.headers)
    if NO_VULN in r.text: 
        print('[+] The Certificate & Public Key look good. ')
    else:
        print('[+] Insecure / Invalid key. ')
    # print(r.text) 

def testkey(domain,port=443):
    try:
        cert = ssl.get_server_certificate((domain,port)) 
        print(f'First => {cert}') 
        makeRequest(cert) 
    except ssl.SSLError as e:
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain,port)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    certDer = ssock.getpeercert(True) 
                    cert = ssl.DER_cert_to_PEM_cert(certDer) 
                    makeRequest(cert)
                    # print(f'Second => {cert}') 
        except Exception as e:
            print(f'Error {e}') 
    except Exception as e:
        print(f'Error Encountered..... {e}') 

# testkey('ey.com')
with open("domain-list.txt", "r") as f:
    domains = f.readlines() 

for dom in domains:
    x = dom.strip()
    if x:
        testkey(x)