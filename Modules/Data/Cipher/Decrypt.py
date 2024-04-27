'''
This module handles data decodeing and decryptions.
'''

#built-in modules
import math

#constants
from .Locals import CAESARELEMENTS as ELEMENTS
from .Encrypt import caesarEncrypt

def caesarDecrypt(cipherText, key):
    '''The caesar cipher depends on the elements specified in ELEMENTS.'''
    length = len(ELEMENTS)
    key = length - key
    return caesarEncrypt(cipherText, key)
    
def reverseDecrypt(cipherText):
    plainText = ''
    for char in cipherText:
        plainText = char + plainText
    return plainText


def transpositionDecrypt(cipherText, key):
    c = math.ceil(len(cipherText)/key)
    r = key
    numOfShadedBoxes = r*c - len(cipherText)

    plainText = [''] * c
    x = y = 0
    for char in cipherText:
        plainText[x] += char
        x += 1
        if x == c or (x == c-1 and y >= r - numOfShadedBoxes):
            x = 0
            y += 1
    return ''.join(plainText)


def uniDecode(data):
    orderList = data.split('.')
    charList = []
    for (i,order) in enumerate(orderList):
        try:
            order = int(order)
        except ValueError:
            print([i, order])
            raise ValueError
        char = chr(order)
        charList.append(char)
    data = ''.join(charList)
    return data



