'''
This module stores button constants used in __init__.py
'''

#classes
from ...Classes.Button import LabelButton

#constants
from ...Locals.Display import CENTERX, WINHEIGHT
from ...Locals.Fonts   import SETTING


filename, size = SETTING, 60

storyOn = LabelButton(filename, size, text='ON' )
storyOff= LabelButton(filename, size, text='OFF')
bgmOn   = LabelButton(filename, size, text='ON' )
bgmOff  = LabelButton(filename, size, text='OFF')
BACK    = LabelButton(filename, size, text='返回')

storyOn.config(
    x=(CENTERX, None, None),
    y=(160, None, None)
    )
storyOff.config(
    x=(CENTERX+160, None, None),
    y=(160, None, None)
    )
bgmOn.config(
    x=(CENTERX, None, None),
    y=(240, None, None)
    )
bgmOff.config(
    x=(CENTERX+160, None, None),
    y=(240, None, None)
    )
BACK.config(
    x=(0, None, None),
    y=(None, None, WINHEIGHT)
    )
