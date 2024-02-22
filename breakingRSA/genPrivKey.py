# This script generates the private key based on the key primitives provided to it. 

from Cryptodome.PublicKey import RSA        # Cryptodome is the library that is used. 

def genkey(n,e,d,p,q):          # n, e, d, p, q should be passed to it. 
    private_key = RSA.construct((n,e,d,p,q),consistency_check=True) 
    private_key = private_key.export_key(format='PEM').decode()     # Convert the key object into PEM format and decode into UTF8 
    return private_key