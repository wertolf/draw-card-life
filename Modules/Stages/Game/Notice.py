'''
This module stores function notice().
'''

#classes
from pygame import Rect, Surface
from ...Classes.Text   import showLines
from ...Classes.Button import LabelButton, drawButtons, moveAndClick

#constants
from ...Locals.Colors  import GREY
from ...Locals.Display import CENTERX, DISPLAY, WINWIDTH, update
from ...Locals.Fonts   import NOTICE


#modules
from pygame import draw

def notice(text):
    #Rect(left, top, width, height)
    width, height = 640, 240
    destRect = Rect(160, 400, width, height)
    localSurf= Surface((width, height))

    filename = NOTICE
    if text.count('\n') == 0: size, dist = 36, 20
    elif text.count('\n') == 1: size, dist = 36, 16
    elif text.count('\n') == 2: size, dist = 32, 16
    else:
        size, dist = 28, 12

    text += '\n'
    showLines(
        text,
        surf=localSurf, dest=destRect,
        filename= filename, size= size, dist= dist,
        bgcolor=GREY,
        )

    filename, size = NOTICE, 36
    OK = LabelButton(filename, size, text='我知道了')
    OK.config(
        x=(None, destRect.centerx, None),
        y=(None, None, destRect.bottom),
        )
    drawButtons(OK)
    update()

    button = moveAndClick(OK)
    if button == OK: return
    #remember to call drawPage after calling this function
