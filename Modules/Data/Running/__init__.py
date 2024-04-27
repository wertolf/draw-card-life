'''
This module reads TEMP file for ARBITRARY times.
it is not run until __init__.game are called.
'''

#constants
from ...Locals.Paths import TEMP

HEAD_PLAYER = 'HEAD_PLAYER\n'
TAIL_PLAYER = '\nTAIL_PLAYER'

HEAD_USER = 'HEAD_USER\n'
TAIL_USER = '\nTAIL_USER'

HEAD_TRADE = 'HEAD_TRADE\n'
TAIL_TRADE = '\nTAIL_TRADE'

#
def findText(text, head, tail):

    #head and tail are handled separately
    start = text.find(head)
    if start == -1:
        print('head not found.')
        return None
    text = text[start:]
    text = text[len(head):] #use slicing, not str.strip() in case head and tail are overlapped

    end = text.find(tail)
    if end == -1:
        print('tail not found.')
        return None
    text = text[:end].rstrip(tail)

    return text

def loadTemp(head, tail, dataType='custom'):
    print('loading %s data in TEMP...' % dataType)
    with open(TEMP) as file: text = file.read()
    text = findText(text, head, tail)
    data = eval(text)
    return data

def loadTempPlayer(): return loadTemp(HEAD_PLAYER, TAIL_PLAYER, dataType='player')
def loadTempUser  (): return loadTemp(HEAD_USER  , TAIL_USER  , dataType='user')
def loadTempTrade (): return loadTemp(HEAD_TRADE , TAIL_TRADE , dataType='trade')

def updateTemp(data, head, tail, dataType='custom'):
    '''
update custom data into TEMP without changing other data.
    '''
    print('updating %s data in TEMP...' % dataType)
    try:
        '''open existing data first.'''
        with open(TEMP) as file: text = file.read()
    except FileNotFoundError:
        '''if TEMP is not created'''
        text = ''
    old = findText(text, head, tail)
    new = str(data)
    if old == None:
        '''no player data found in TEMP, just add the new one at the end of TEMP.'''
        with open(TEMP, 'a') as file:
            file.write('\n')
            #need to add head and tail
            file.write(head + new + tail)
    else:
        '''replace old with new, with other part of TEMP unchanged.'''
        #no need to change head and tail

        #CAUTION:
        #str is immutable, calling method returns a changed str
        #leaving the str who calls the method unchanged
        text = text.replace(old, new)
        with open(TEMP, 'w') as file:
            file.write(text)

def updateTempPlayer(player): updateTemp(player, HEAD_PLAYER, TAIL_PLAYER, dataType='player')
def updateTempUser  (user  ): updateTemp(user  , HEAD_USER  , TAIL_USER  , dataType='user')
def updateTempTrade (info  ): updateTemp(info  , HEAD_TRADE , TAIL_TRADE , dataType='trade')
