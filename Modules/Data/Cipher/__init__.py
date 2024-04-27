'''
This module stores the current plan for encryption.
'''

#constants
from .Locals import caesarKey, transpositionKey

#functions
from .Encrypt import caesarEncrypt, reverseEncrypt, transpositionEncrypt, uniEncode
from .Decrypt import caesarDecrypt, reverseDecrypt, transpositionDecrypt, uniDecode

def decrypt(cipherText):
    '''note:'''
    '''beware the sequence of decrypting and decoding'''
    '''is the symmetry of the sequence of coding and encrypting.'''
    '''changing the sequence will cause error.'''
    print('decrypting data...')

    #decrypting
    cipherText = caesarDecrypt(cipherText, caesarKey)
    cipherText = transpositionDecrypt(cipherText, transpositionKey)
    code = reverseDecrypt(cipherText)

    #decoding, the result is called 'text', compared with 'code'
    plainText = uniDecode(code)

    return plainText

def encrypt(plainText):
    print('encrypting data...')
    
    #coding, the result is called 'code', compared with 'text'
    code = uniEncode(plainText)
    
    #encrypting
    cipherText = reverseEncrypt(code)
    cipherText = transpositionEncrypt(cipherText, transpositionKey)
    cipherText = caesarEncrypt(cipherText, caesarKey)

    return cipherText
