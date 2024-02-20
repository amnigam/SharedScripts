# The purpose of this script is to download the certificate of a website and extract the crypto components from the certificate.

import socket 
import ssl 
from Cryptodome.PublicKey import RSA 
from Cryptodome.PublicKey import ECC
from cryptography import x509 
from cryptography.hazmat.primitives.asymmetric import rsa 

def getPublicKeyAlg(cert):
    cert = x509.load_pem_x509_certificate(cert.encode('utf-8'))
    alg = isinstance(cert.public_key(),rsa.RSAPublicKey)
    # print(alg)
    return alg 

def cryptoExtract(cert): 
    # Initializing Cryptographic Elements to be extracted from certificate. 
    n=0
    e=0
    key_len=0

    key = RSA.import_key(cert)      # Load the key for the certificate. 
    # Extract cryptographic primitives from the retrieved certificate. 
    n = key.n   # value of n for the certificate 
    e = key.e   # value of e used for the certificate 
    key_len = n.bit_length()    # Tell the key length. 

    # Print values retrieved from the certificate. 
    print(f'[+] The Value of n = {n}') 
    print(f'[+] The value of e = {e}') 
    print(f'[+] The key length = {key_len}') 

def writeCert(cert):
    with open("cert.pem", "w") as f:
        f.write(cert) 

def extract(domain,port=443):   # Default port of 443. Else, whatever value passed in port parameter.
    # Extract the certificate from the server. 
    try:
        cert = ssl.get_server_certificate((domain,port))    # This certificate is a STRING right now. 
        if (getPublicKeyAlg(cert)):
            writeCert(cert)
            cryptoExtract(cert) 
        else: 
            print('Certificate does not use RSA algorithm.') 
    except ssl.SSLError as e:
        try:  
            context = ssl.create_default_context()
            with socket.create_connection((domain,port)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    certDER = ssock.getpeercert(True)      # This CERT is in DER format. 
                    cert = ssl.DER_cert_to_PEM_cert(certDER)    # Convert it into PEM format. 
                    if (getPublicKeyAlg(cert)):
                        cryptoExtract(cert) 
                        writeCert(cert)
                    else:
                        print('Certificate does not use RSA algorithm.') 
        except Exception as e:
            print(f'SSL Error encountered... {e}') 
    except Exception as e:
        print(f'An Error Occurred while retrieving certificate... {e}') 

extract('tryhackme.com')
extract('snyk.io')
extract('ey.com') 
