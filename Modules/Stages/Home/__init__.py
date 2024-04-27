'''
This module provides access to the home page.
'''

#classes
from ...Classes.Text   import Label, show, fade, showLines
from ...Classes.Button import disableButtons, drawButtons, moveAndClick

#constants
from ...Locals.Colors  import BGCOLOR
from ...Locals.Display import CENTER, CENTERX, CENTERY, DISPLAY, \
                              WINWIDTH, WINHEIGHT
from ...Locals.Fonts   import BUTTON, COPYRIGHT, TEXT
from ...Locals.Paths   import TEMP
from ...Locals.Time    import DELAY

#functions
from ...Data.Build    import buildPlayerData
from ...Data.LoadSave import loadPlayerData, loadUserData
from ...Data.Running  import loadTempUser, updateTempPlayer, updateTempUser

#instances
from ._layout import *

#modules
from pygame import mixer

#pages
from .Ack   import ack
from .Help  import help
from .Fate  import fate
from .Achievement import achievement
from ..Game     import game
from ..Settings import settings

#run-time
# from .Die import die

#top-level function
def home():
    '''The top-level function in this module.'''
    while True:
        print('-'*32)
        print('loop restarted.')
        print('clearing screen...')
        DISPLAY.fill(BGCOLOR)

        ##loading user data
        print('accessing user data from TEMP...')
        try:
            user = loadTempUser()
        except FileNotFoundError:
            print('user data invalid.')
            print('logging in as guest...')
            user = loadUserData(username='Guest')
        finally:
            updateTempUser(user)

        ##load player data
        isValidSave, player = loadPlayerData(user['username'])

        ##the buttonList and disableList is bound with whether player data exist or not
        buttonList = [LOAD, NEW, HELP, QUIT, ACK, SET, ACHIEVE, FATE]
        buttonList.append(EXTRA)
        disableList = []

        if not isValidSave: #disable LOAD
            buttonList. remove(LOAD)
            disableList.append(LOAD)

        disableList.extend([LOAD, ACK, SET, ACHIEVE, FATE])
        
        ##redraw the screen each time a new loop starts
        print('drawing on screen...')
        #welcome
        surf = Label(TEXT, size=30, text='WELCOME,').get_surf()
        rect = surf.get_rect(left=0, top=0)
        DISPLAY.blit(surf, rect)
        surf = Label(TEXT, size=30, text=user['username'].upper()).get_surf()
        rect = surf.get_rect(left=0, top=40)
        DISPLAY.blit(surf, rect)

        # title
        surf = Label(TEXT, size=60, text='抽卡人生').get_surf()
        rect = surf.get_rect(top=100, centerx=CENTERX)
        DISPLAY.blit(surf, rect)

        # copyright
        surf = Label(COPYRIGHT, size=30, text='Copyright%s2019 OurDreams Studio' % chr(169)).get_surf()
        rect = surf.get_rect(bottom=WINHEIGHT, centerx=CENTERX)
        DISPLAY.blit(surf, rect)

        #buttons
        drawButtons   (*buttonList )
        disableButtons(*disableList)
        show(DISPLAY, delay=0)

        ##BGM-play
        if user['bgmOn']:
            print('restarting bgm...')
            # mixer.music.load(HOMEBGM)
            # mixer.music.play(loops=-1)

        print('initialization completed.')

        ##handling events
        button = moveAndClick(*buttonList)
        mixer.music.fadeout(DELAY)
        fade(DISPLAY)

        if button == QUIT:
            raise SystemExit('FROM HOME')
            
        if button in (NEW, LOAD):
            print('-'*32)
            if button == NEW:
                print('starting new game...')
                player = buildPlayerData(user)
                player['isNewGame'] = True

            if button == LOAD:
                '''this situation is also ok when LOAD is disabled.'''
                print('resuming last game...')
                player['isNewGame'] = False

            updateTempPlayer(player)

            #reason means 'death reason'
            reason = game()
            die(reason)
            #die disables LOAD when next loop starts

        if button == ACK:
            ack()

        if button == SET:
            settings()

        if button == ACHIEVE:
            achievement()

        if button == FATE:
            fate()

        if button == HELP:
            help() # not the built-in function
        
        if button == EXTRA:
            extra()
