'''
This module provides access to button classes and funcs.
'''

##imports
#classes
from pygame import Rect, Surface
from .Text  import Label, showLines, tip

#constants
from pygame.locals import (
    K_ESCAPE, K_RETURN, K_DOWN, K_LEFT, K_RIGHT, K_UP,
    KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION,
    )
from ..Locals.Basics  import TIPLIST_FATE, TIPLIST_TRADE
from ..Locals.Colors  import AZURE, CYAN, FGCOLOR, GREY, GOLD, YELLOW
from ..Locals.Display import DISPLAY, update

#functions
from ..Patches import getRect

#utilities
from pygame import draw, event, mouse
import sys


##functions

#
def disableButtons(*buttonList):
    '''draw disabled buttons.'''
    drawButtons(*buttonList, color=GREY)

def drawButtons(*buttonList, color=None):
    '''draw buttons.'''
    for button in buttonList:
        if color: surf = button.get_surf(hlcolor=color)
        else    : surf = button.get_surf()
        rect = button.get_rect()
        DISPLAY.blit(surf, rect)

def moveAndClick(*buttonList):

    keyboardActivated = False
    INDEX_MIN = 0
    INDEX_MAX = len(buttonList)-1
    index = INDEX_MIN
    while True:
        ###mode 1: keyboard not activated
        if not keyboardActivated:
            for button in buttonList:
                #is mouse collided with rect?
                #sometimes the mouse is inside the rect, but does not move
                #so this part is outside the event handler
                rect = button.get_rect()
                isCollided = rect.collidepoint(mouse.get_pos())
                if isCollided and ((not button.isFocused) or (not button.enterEffectShown)):
                    button.enterEffect()
                    button.isFocused = True
                    button.enterEffectShown = True
                elif (not isCollided) and button.isFocused: #similar to the 'if' above
                    button.leaveEffect()
                    button.isFocused = False
                    button.enterEffectShown = False

            for case in event.get():
                '''to avoid name conflict, the iteration variable is renamed as 'case'.'''

                ##use mouse to select
                if case.type == MOUSEBUTTONDOWN:
                    for button in buttonList:
                        if button.get_rect().collidepoint(case.pos):
                            button.pressEffect()
                if case.type == MOUSEBUTTONUP: #change color when button up, reverse with down
                    for button in buttonList:
                        if button.get_rect().collidepoint(case.pos):
                            button.enterEffect()
                            button.isFocused = True

                            #before 'return', do something to debug for next loop
                            button.enterEffectShown = False
                            return button
                            #exit the function, there are no other ways to exit loop elsewhere

                if case.type == KEYDOWN and case.key != K_ESCAPE:
                    '''activate keyboard and reset focus.'''
                    keyboardActivated = True
                    for button in buttonList:
                        if button.isFocused:
                            '''lose and reset focus.'''
                            button.leaveEffect()
                            button.resetFocus()

                if case.type == KEYUP and case.key == K_ESCAPE:
                    '''exit is available in both modes.'''
                    raise SystemExit('FROM moveAndClick')

        ###mode 2: keyboard activated
        ##shortcut: use ENTER and ARROWs to access buttons in buttonList, but will reset after 'return'
        if keyboardActivated:
            for button in buttonList:
                '''up to 2 buttons are changed in this section.'''
                if button.isFocused and (not button.enterEffectShown):
                    button.enterEffect()
                    button.enterEffectShown = True
                elif (not button.isFocused) and button.enterEffectShown:
                    button.leaveEffect()
                    button.enterEffectShown = False

            currentFocusedButton = buttonList[index]
            for case in event.get():
                if case.type == KEYDOWN:
                    if case.key == K_RETURN:
                        currentFocusedButton.pressEffect()
                if case.type == KEYUP:
                    if case.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                        currentFocusedButton.isFocused = False
                        if case.key in (K_UP, K_LEFT):
                            if index == INDEX_MIN: index = INDEX_MAX
                            else: index -= 1
                        if case.key in (K_DOWN, K_RIGHT):
                            if index == INDEX_MAX: index = INDEX_MIN
                            else: index += 1
                        nextFocusedButton = buttonList[index]
                        nextFocusedButton.isFocused = True
                    if case.key == K_RETURN:
                        currentFocusedButton.enterEffect()
                        return currentFocusedButton
                if case.type == MOUSEMOTION:
                    keyboardActivated = False

                if case.type == KEYUP and case.key == K_ESCAPE:
                    '''exit is available in both modes.'''
                    raise SystemExit('FROM moveAndClick')

        update()

##classes
class Button:
    def __init__(self):
        self.isFocused = False
        self.enterEffectShown = False
    #effects are visual, those besides visuality are elsewhere, e.g. inside moveAndClick()
    def enterEffect(self):pass
    def leaveEffect(self): pass
    def pressEffect(self): pass
    def resetFocus(self):
        self.isFocused = False

class LabelButton(Button, Label):
    '''button implemented using Label.'''
    def __init__(self, filename, size, text, **kwargs):
        Button.__init__(self)
        Label .__init__(self, filename, size, text)
        self.cDict = dict(
                x=(0, None, None),
                y=(0, None, None),
                normal   =FGCOLOR,
                highlight=YELLOW,
                activate =CYAN,
                )
    #effects
    def enterEffect(self):
        # FOCUS.play()
        drawButtons(self, color=self.cDict['highlight'])
    def leaveEffect(self):
        drawButtons(self, color=self.cDict['normal'])
    def pressEffect(self):
        drawButtons(self, color=self.cDict['activate'])
    #other methods
    def get_rect(self, **kwargs):
        surf = self.get_surf()
        x, y = self.cDict['x'], self.cDict['y']
        return getRect(surf, x, y)
    def config(self, **kwargs):
        for key in self.cDict.keys():
            if key in kwargs.keys(): self.cDict[key] = kwargs[key]

class GameButton(LabelButton):
    '''buttons used in Game page.'''
    def __init__(self, filename, size, text):
        LabelButton.__init__(self, filename, size, text)
        self.tip = '在这里显示帮助。'
    def enterEffect(self):
        LabelButton.enterEffect(self)
        tip(text=self.tip)
    def leaveEffect(self):
        tip(text=None)
        LabelButton.leaveEffect(self)

class RectButton(Button):
    def __init__(self):
        Button.__init__(self)
        self.width = 160
        self.height= 160
        self.x = (0, None, None)
        self.y = (0, None, None)
        self.normalColor = FGCOLOR
        self.highlightColor = YELLOW
        self.activateColor = CYAN
        self.text = '(default)'
    #effects
    def enterEffect(self):
        FOCUS.play()
        drawButtons(self, color=self.highlightColor)
    def leaveEffect(self):
        drawButtons(self)
    def pressEffect(self):
        drawButtons(self, color=self.activateColor)
    #other methods
    def get_surf(self, hlcolor=None):
        width, height = self.width, self.height
        surf = Surface((width, height))
        rect = Rect(0, 0, width, height)
        if hlcolor:
            fgcolor = hlcolor
        else:
            fgcolor = self.normalColor

        draw.rect(surf, fgcolor, rect, 5)
        showLines(
            self.text,
            surf= surf, dest= rect,
            fgcolor= fgcolor,
            blitOnTheDisplay=False, updateTheDisplay=False,
            clearTheSurf=False, showLoading=False,
            )
        return surf
    def get_rect(self):
        surf = self.get_surf()
        x, y = self.x, self.y
        return getRect(surf, x, y)

class FateButton(RectButton):
    def __init__(self):
        RectButton.__init__(self)
        self.width, self.height = 240, 60
        self.normalColor = AZURE
        self.tip = '在这里显示帮助。'
    def enterEffect(self):
        RectButton.enterEffect(self)
        tip(text=self.tip, mode='showLines', size=25, dist=10)
        #this mode is also used in Stages.Fate
    def leaveEffect(self):
        RectButton.leaveEffect(self)
        #tip(tipList=TIPLIST_FATE, mode='showLines')
        #this mode is also used in Stages.Fate

class TradeButton(RectButton):
    def __init__(self):
        RectButton.__init__(self)
        self.width, self.height = 240, 120
        self.normalColor = GOLD
        self.tip = '在这里显示帮助。'
    def enterEffect(self):
        RectButton.enterEffect(self)
        tip(text=self.tip, mode='showLines')
        #this mode is also used in Stages.Game.Trade
    def leaveEffect(self):
        RectButton.leaveEffect(self)
        tip(tipList=TIPLIST_TRADE, mode='showLines')
        #this mode is also used in Stages.Game.Trade
