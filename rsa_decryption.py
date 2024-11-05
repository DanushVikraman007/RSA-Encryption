import numpy as np
import math as m
p=int(input("Enter large prime value of p -:"))
q=int(input("Enter large prime value of q -:"))
e=int(input("Enter relatively samll prime value of e -:"))
encrypted_word=input("Enter word to encrypt in capital -:")
encrypted_data_list=list(encrypted_word)
L=len(encrypted_data_list)
Position_encryted=list()
for i in range(L):
    decrypted_word=ord(encrypted_data_list[i])-64
    Position_encryted.insert(i,decrypted_word) 
n=p*q
phi=(p-1)*(q-1)
for i in range(1 ,20):
    if(((1+i*(phi))%e==0)):
        d=(1+i*(phi))/e
        break
decrypted_data_list=list()
position_decrypt=list()
for i in range(L):
    Ne=Position_encryted[i]
    Ne=(int(Ne**d)%n)
    position_decrypt.insert(i,Ne)
    decrypted_data_list.insert(i,chr(Ne+64))
decrypted_word=''.join(decrypted_data_list)
print("The given word :",encrypted_word)
print("The given word as a list :",encrypted_data_list)
print("The positional data of the given word :",Position_encryted)
print("The decrypted word :",decrypted_word)
print("The encrypted word as a list :",decrypted_data_list)
print("The positional data of the encrypted word :",position_decrypt)