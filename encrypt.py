# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:17:25 2020

@author: varma
"""

import json
import xmltodict
import os


os.getcwd()
with open("/Users/neerajkulshrestha/github/MyFirstProject/sample.json", 'r') as f:
    jsonString = f.read()

print('JSON input (sample.json):')
print(jsonString)

xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)

print('\nXML output(output.xml):')
print(xmlString)

with open('output.xml', 'w') as f:
    f.write(xmlString)

import pyAesCrypt
# encryption/decryption buffer size
bufferSize = 64 * 1024
password = "secret"
# encryption of file output.xml

pyAesCrypt.encryptFile("output.xml", "enoutput.xml.aes", password, bufferSize)
print('\n----------------------------------------------------------------------')
print('\nEncrypted file is saved in your system with name -  "enoutput.xml.aes"')
print('\n----------------------------------------------------------------------')


