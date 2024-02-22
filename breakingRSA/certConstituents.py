# The purpose of this script is to download the certificate of a website and extract the crypto components from the certificate.
# Additionally, one can provide just the key and it will provide the cryptographic elements of that key back. 

import socket 
import ssl 
from Cryptodome.PublicKey import RSA 
from Cryptodome.PublicKey import ECC
from cryptography import x509 
from cryptography.hazmat.primitives.asymmetric import rsa 

# This function takes in a CERTIFICATE and checks whether the public key is RSA or not. 
def getPublicKeyAlg(cert):
    cert = x509.load_pem_x509_certificate(cert.encode('utf-8'))
    alg = isinstance(cert.public_key(),rsa.RSAPublicKey)        # Check if public key is RSA. (True or False)
    return alg 

# This function takes a CERTICATE and extracts the cryptographic elements of its public key.
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
    return n, e 

# Function will write the downloaded certificate in a PEM file. 
def writeCert(cert):
    with open("cert.pem", "w") as f:
        f.write(cert) 

# Accepts a PUBLIC KEY and will extract PUBLIC KEY cryptographic elements. 
def keyExtract(key): 
    key = RSA.import_key(key) 
    n = key.n 
    e = key.e 
    key_len = key.size_in_bits()
    return n , e, key_len 

# This function establishes a connection to the DOMAIN and downloads its CERTIFICATE. 
def extract(domain,port=443):   # Default port of 443. Else, whatever value passed in port parameter.
    # Extract the certificate from the server by querying DOMAIN. 
    try:
        cert = ssl.get_server_certificate((domain,port))    # This certificate is a STRING right now. 
        if (getPublicKeyAlg(cert)):
            writeCert(cert)
            n, e = cryptoExtract(cert) 
        else: 
            print('Certificate does not use RSA algorithm.') 
            return 0,0      # Return 0 since it didn't work. 
    except ssl.SSLError as e:
        # It is possible that a server might host multiple websites. (CDN). In such a situation you need to provide HOSTNAME for SNI. 
        try:  
            context = ssl.create_default_context()      
            with socket.create_connection((domain,port)) as sock:   # Establish a SOCKET connection as well. 
                with context.wrap_socket(sock, server_hostname=domain) as ssock:        # Notice, we provide the HOSTNAME this time for SNI lookup. 
                    certDER = ssock.getpeercert(True)      # This CERT is in DER format. 
                    cert = ssl.DER_cert_to_PEM_cert(certDER)    # Convert it into PEM format. 
                    if (getPublicKeyAlg(cert)):
                        n, e = cryptoExtract(cert) 
                        writeCert(cert)
                    else:
                        print('Certificate does not use RSA algorithm.') 
                        return 0,0      # Return 0 since it didn't work. 
        except Exception as e:
            print(f'SSL Error encountered... {e}') 
    except Exception as e:
        print(f'An Error Occurred while retrieving certificate... {e}') 
    else:
        return n, e 