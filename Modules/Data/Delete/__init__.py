'''
This module deletes data.
'''

#constants
from ...Locals.Paths import SAVE, TEMP

#functions
from ..LoadSave import findPlayerData
#modules
import os

def deletePlayerData(username):
    playerFile = findPlayerData(username)
    os.remove(playerFile)
    print('playerFile removed.')

def deleteTEMP():
    print('removing temp file...')
    os.remove(TEMP)
