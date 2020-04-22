# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:46:42 2020

@author: varma
"""

import pyAesCrypt
# encryption/decryption buffer size
bufferSize = 64 * 1024
password = "secret"

# decryption of file data.aes

pyAesCrypt.decryptFile("enoutput.xml.aes", "dnewoutput.xml", password, bufferSize)
