'''
Enter module descriptions here...
'''

#constants
from ...Locals.Basics import FATE_KEYS, K_USER
from ...Locals.Paths import USERDATA

#modules
import os

#functions
from ..Build  import buildUserData
from ..Cipher import decrypt, encrypt

def loadUserData(username):
    '''the path where user data is is definated by username.'''
    baseDir = USERDATA
    userDir = os.path.join(baseDir, username) #use username as folder name
    userFile= os.path.join(userDir, 'userData.txt')
    print('loading user data...')
    try:
        with open(userFile) as file:
            text = file.read()
            text = decrypt(text)
            userDict = eval(text)
        #check if any keys are missing
        for key in K_USER:
            value = userDict[key] #if missing, raise KeyError automatically
        for key in FATE_KEYS:
            assert type(userDict['fate'][key]) == type(0), 'value invalid.'
        return userDict
    except FileNotFoundError:
        if not os.path.isdir(baseDir):
            print('baseDir not found.')
            print('building baseDir...')
            os.mkdir(baseDir)
        if not os.path.isdir(userDir):
            print('userDir not found.')
            print('building userDir...')
            os.mkdir(userDir)
        if not os.path.isfile(userFile):
            print('userFile not found.')
            userDict = buildUserData(username)
            saveUserData(userDict)
            return userDict
    except (AssertionError, KeyError):
        '''if KeyError, data was invalid, rebuild one.'''
        print('userData invalid, rebuilding...')
        return buildUserData(username)

def saveUserData(userDict):
    '''same as loadUserData.'''
    baseDir = USERDATA
    userDir = os.path.join(USERDATA, userDict['username'])
    userFile= os.path.join(userDir, 'userData.txt')
    print('saving user data...')
    text = str(userDict)
    text = encrypt(text)
    with open(userFile, 'w') as file:
        file.write(text)
    print('user data saved.')
