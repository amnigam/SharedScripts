# This script I have snitched from the internet. It provides Factorization of an odd number. 
# This script factorizes based on the Fermat's theorem. 

def isqrt(n):
    x = n 
    y = (x+n//x)//2 
    while (y<x):
        x = y 
        y = (x+n//x)//2 
    return x 

def fermat(n):
    t0=isqrt(n) + 1
    counter = 0
    t = t0 + counter 
    temp = isqrt((t*t) - n) 
    while ((temp*temp) != ((t*t) -n)): 
        counter+=1 
        t=t0+counter 
        temp = isqrt((t*t)-n) 
    s= temp 
    p = t + s
    q = t - s
    return p, q 

# n = int(input('[+] Enter number to factor of the form (p x q): ')) 
# p,q = fermat(n) 

# print('[+] First Factor is: ', p)
# print('[+] Second Factor is: ', q) 