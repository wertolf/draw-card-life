'''
This module stores the DISPLAY,
along with some relevant parameters,
including WINWIDTH, WINHEIGHT and CENTER.

and some useful functions.
'''

from patches.display import resolution

##imports
#constants
from pygame.locals import FULLSCREEN, RESIZABLE
from .Time import CLOCK, FPS
#modules
from pygame import display, time

##constants
WINWIDTH, WINHEIGHT = resolution
DISPLAY = display.set_mode((WINWIDTH, WINHEIGHT), RESIZABLE)
'''The flags argument controls which type of display you want.
There are several to choose from,
and you can even combine multiple types using the bitwise or operator,
(the pipe "|" character).'''
display.set_caption('抽卡人生')

CENTERX = WINWIDTH // 2
CENTERY = WINHEIGHT // 2
CENTER = (CENTERX, CENTERY)

##functions
def update(delay=0, fps=FPS):
    display.update()
    time.delay(delay)
    CLOCK.tick(fps)
