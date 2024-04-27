'''
This module tests the encryption during the developing process.
Note: unlike other modules, this module should be run in top-level
so as to enable the following import statements.
'''


def special():
    #constants
    plainText = '012345.6789.'

    #functions
    from Cipher.Decrypt import caesarDecrypt
    from Cipher.Encrypt import caesarEncrypt

    #use pipes('|') in case there are spaces at the beginning or end of the text
    print('plainText:\t|%s|' % plainText)
    cipherText = caesarEncrypt(plainText, 8)
    print('cipherText:\t|%s|' % cipherText)
    plainText = caesarDecrypt(cipherText, 8)
    print('plainText:\t|%s|' % plainText)

def general():
    #constants
    D = {'money':100}
    plainText = str(D)

    #functions
    from Cipher.__init__ import decrypt
    from Cipher.__init__ import encrypt

    print('plainText:\t|%s|' % plainText)
    cipherText = encrypt(plainText)
    print('cipherText:\t|%s|' % cipherText)
    plainText = decrypt(cipherText)
    print('plainText:\t|%s|' % plainText)
if __name__ == '__main__':
    #special()
    general()
