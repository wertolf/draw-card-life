'''
This module handles data encoding and encryptions.
'''

#constants
from .Locals import CAESARELEMENTS as ELEMENTS

def caesarEncrypt(plainText, key):
    '''The Caesar cipher depends on the elements specified in ELEMENTS.'''
    length = len(ELEMENTS)
    cipherText = ''
    for char in plainText:
        
        if char not in ELEMENTS:
            char = char
        else:
            index = ELEMENTS.find(char)
            index += key; index %= length
            char = ELEMENTS[index]

        cipherText += char
    return cipherText
def reverseEncrypt(plainText):
    '''This is a \'while\' version reverse, see a better one in Decrypt.py.'''
    cipherText = ''
    i = len(plainText) - 1
    while i >= 0:
        cipherText += plainText[i]
        i -= 1
    return cipherText


def transpositionEncrypt(plainText, key):
    cipherText = [''] * key
    i = 0
    for char in plainText:
        cipherText[i] += char
        i += 1
        if i == key: i = 0
    return ''.join(cipherText)


def uniEncode(plainText):
    orderList = []
    for char in plainText:
        order = ord(char)
        orderList.append(str(order))
    cipherText = '.'.join(orderList)
    return cipherText
