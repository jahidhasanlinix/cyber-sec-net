#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:36:07 2021

@author: jahid
"""
def crypt_sys():
    original_msg='abcdefghijklmnopqrstuvwxyz !'
    value= original_msg[-1]+original_msg[0:-1]
    
    encrypt_Dict=dict(zip(original_msg, value))
    decrpt_Dict=dict(zip(value, original_msg))
    
    msg=input('Enter your secret message: ')
    mode=input('Please enter a mode: Encode(E) Or Decode(D)')
    
    if mode.upper() == 'E':
        new_msg = ''.join([encrypt_Dict[letter] for letter in msg.lower()])
    elif mode.upper() == 'D':
        new_msg = ''.join([decrpt_Dict[letter] for letter in msg.lower()])
    else:
        print('Enter a correct choise: ')
    return new_msg.capitalize()
print(crypt_sys())
    