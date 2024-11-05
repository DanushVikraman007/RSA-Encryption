import numpy as np
import math as m
p=int(input("Enter large prime value of p -:"))
q=int(input("Enter large prime value of q -:"))
e=int(input("Enter relatively samll prime value of e -:"))
orginal_word=input("Enter word to encrypt in capital -:")
original_data_list=list(orginal_word)
L=len(original_data_list)
Position_og=list()
for i in range(L):
    encrypted_word=ord(original_data_list[i])-64
    Position_og.insert(i,encrypted_word) 
n=p*q
encrypted_data_list=list()
position_encrypt=list()
for i in range(L):
    Ne=Position_og[i]
    Ne=(Ne**e)%n
    position_encrypt.insert(i,Ne)
    encrypted_data_list.insert(i,chr(Ne+64))
encrypted_word=''.join(encrypted_data_list)
print("The given word :",orginal_word)
print("The given word as a list :",original_data_list)
print("The positional data of the given word :",Position_og)
print("The encryted word :",encrypted_word)
print("The encrypted word as a list :",encrypted_data_list)
print("The positional data of the encrypted word :",position_encrypt)