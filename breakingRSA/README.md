# Breaking RSA Algorithm. 

## TLDR 
RSA algorithm is susceptible to compromise in case if the prime numbers chosen in developing the keys happen to be not sufficiently spaced apart. 
In such a situation, by leveraging Fermat's factorization method, one can arrive at the prime numbers initially chosen for the development of public & private keys.

In the context of RSA algorithm, this is catastrophic as it would lead to a complete compromise of the public & private keys.

## Associated Content & Material

This vulnerability has been documented under CVE-2022-26320 and is a critical vulnerability. 
I have also created a deliberately vulnerable web application to test and demonstrate the workings of this vulnerability. 

Web Application can be found here [link](https://github.com/amnigam/tutorials/tree/main/rsabreak)

And I have provided a detailed writeup on what this vulnerability is and how to use the exploit as well as the vulnerable app. 
You can find that here [writeup](https://medium.com/@king.amit95/breaking-rsa-algorithm-fermats-surprise-554768a707ea)

Hope this helps people interested in knowing more about this vulnerability and cryptography hacks. 
