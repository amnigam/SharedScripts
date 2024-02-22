# This script computes the modulo inverse that is required for generating the private key. 
# This is not my script. I have taken this from GITHUB GIST. 

def egcd(a,b):
    if a==0:
        return (b,0,1) 
    g, y, x = egcd(b%a, a) 
    return (g, x - (b//a)*y, y) 

def modinv(a,m):
    g, x, y = egcd(a,m) 
    if g!= 1:
        raise Exception('No Modular Inverse') 
    return x%m 
