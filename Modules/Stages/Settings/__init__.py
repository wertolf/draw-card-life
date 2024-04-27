'''
This module sets up the settings page.
'''

#classes
from ...Classes.Text   import Label, fade
from ...Classes.Button import disableButtons, drawButtons, moveAndClick

#constants
from ...Locals.Colors  import BGCOLOR
from ...Locals.Display import DISPLAY, update

#functions
from ...Data.Running  import loadTempUser, updateTempUser

#instances
from ._layout import *

#utilities
from pygame import display

def settings():
    '''settings is bound with user.'''
    global buttonList, disableList

    user = loadTempUser()
    DISPLAY.fill(BGCOLOR)

    #labels, filename and size are imported from .Buttons
    surf = Label(filename, size, text='剧情').get_surf()
    rect = surf .get_rect(right=CENTERX-160, top=160)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, text='BGM').get_surf()
    rect = surf.get_rect(right=CENTERX-160, top=240)
    DISPLAY.blit(surf, rect)

    buttonList = [storyOn, storyOff, bgmOn, bgmOff, BACK]
    disableList = []

    #initialize buttonList and disableList according to userData
    if user['storyOn']: buttonList.remove(storyOn); disableList.append(storyOn)
    elif not user['storyOn']: buttonList.remove(storyOff); disableList.append(storyOff)
        
    if user['bgmOn']: buttonList.remove(bgmOn); disableList.append(bgmOn)
    elif not user['bgmOn']: buttonList.remove(bgmOff); disableList.append(bgmOff)

    while True:            
        drawButtons   (*buttonList)
        disableButtons(*disableList)

        #get presses button
        button = moveAndClick(*buttonList)

        #event handler
        if button == storyOn:
            user['storyOn'] = True
            _disable(storyOn)
            _enable (storyOff)
        if button == storyOff:
            user['storyOn'] = False
            _disable(storyOff)
            _enable (storyOn)
        if button == bgmOn:
            user['bgmOn'] = True
            _disable(bgmOn)
            _enable (bgmOff)
        if button == bgmOff:
            user['bgmOn'] = False
            _disable(bgmOff)
            _enable (bgmOn)
        if button == BACK:
            updateTempUser(user)
            fade(DISPLAY)
            return

        update()

#beware the subtle difference between 'remove' and 'append'
def _disable(button):
    global buttonList, disableList
    buttonList .remove(button)
    disableList.append(button)

def _enable(button):
    global buttonList, disableList
    buttonList .append(button)
    disableList.remove(button)
