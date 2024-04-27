'''

'''

#constants
from ...Locals.Paths import USERDATA
from ...Locals.Basics import K_PLAYER

#functions
from ..Build  import buildPlayerData
from ..Cipher import decrypt, encrypt

#modules
import os, sys

def findPlayerData(username):
    '''return path of playerData.txt.'''
    baseDir = USERDATA
    userDir = os.path.join(baseDir, username)
    playerFile = os.path.join(userDir, 'playerData.txt')
    return playerFile

def loadPlayerData(username):
    '''return (isValidSave, playerDict)'''
    print('loading player data...')

    playerFile = findPlayerData(username)

    try:
        with open(playerFile) as file:
            text = file.read()
            text = decrypt(text)
            playerDict = eval(text)
        if playerDict['status'] == 'die': raise KeyError('status')
        #check if any (key, value) is missing, if missing, raise KeyError automatically
        for key in K_PLAYER:
            value = playerDict[key]
    except Exception:
        '''known exceptions are FileNotFoundError, KeyError.'''
        exc_type, exc_value, tb = sys.exc_info()
        print('player data invalid.')
        print(exc_type, exc_value)
        isValidSave= False
        playerDict = None
    else:
        print('player data valid.')
        isValidSave = True
    finally:
        return (isValidSave, playerDict)

def savePlayerData(username, playerDict):
    '''to save data under user-specific directories, need argument \'username\'.'''
    text = str(playerDict)
    text = encrypt(text)
    playerFile = findPlayerData(username)
    with open(playerFile, 'w') as file: file.write(text)
