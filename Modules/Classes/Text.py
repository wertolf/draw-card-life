'''
This module stores classes and funcs relevant to text.
'''

##imports

#classes
from pygame import Surface

#constants
from pygame.locals import KEYUP, K_r, K_s, K_SPACE
from ..Locals.Basics  import TIPLIST_GAME
from ..Locals.Colors  import BGCOLOR, FGCOLOR, RED
from ..Locals.Display import CENTER, DISPLAY, WINWIDTH, WINHEIGHT, update
from ..Locals.Fonts   import LOADING, STORY, HINT
from ..Locals.Time    import DELAY

#modules
import random
from pygame import event, font, mixer, mouse

##classes
class Label:
    '''one line text widget.'''
    def __init__(self, family, size, text,
                 antialias=False, color=FGCOLOR):
        self.font_family = family
        self.size = size
        self.text = text
        self.antialias = antialias
        self.color = color
    def get_surf(self, hlcolor=None):
        '''return a surface with texts in the given color.'''
        if hlcolor:
            renderFormat = [self.text, self.antialias, hlcolor]
        else:
            #use self.color in default
            renderFormat = [self.text, self.antialias, self.color]

        fontObj = font.SysFont(self.font_family, self.size)
        surface = fontObj.render(*renderFormat)
        return surface

##functions
def show(surf, dest=(0, 0), *, speed=20, delay=DELAY):
    '''gradually appear, then stay for a while.'''
    surf = surf.copy()
    for alpha in range(0, 255, speed):
        DISPLAY.fill(BGCOLOR)
        surf.set_alpha(alpha)
        DISPLAY.blit(surf, dest)
        update()
    update(delay= delay)

def fade(surf, dest=(0, 0), speed=20, delay=DELAY):
    update(delay= delay)
    surf = surf.copy()
    for alpha in range(255, 0, -speed):
        DISPLAY.fill(BGCOLOR)
        surf.set_alpha(alpha)
        DISPLAY.blit(surf, dest)
        update()

def rollLines(text, **kwargs):
    '''
rollLines is based on showLines.
    '''
    filename = kwargs.get('filename', TIP)
    size     = kwargs.get('size', 40)
    delay    = kwargs.get('delay', 1000)
    isHalf   = kwargs.get('isHalf', False)

    centerx, centery = CENTER
    localSurf = DISPLAY.copy()

    lines = text.split('\n')
    count = len(lines)
    height = size*count
    lineTop= centery - height//2

    for line in lines:
        lineSurf = Label(filename, size, text=line).get_surf()
        lineRect = lineSurf.get_rect(centerx= centerx, top=lineTop)
        localSurf.blit(lineSurf, lineRect)

        lineTop += size

    localRect = localSurf.get_rect(centerx= centerx)

    dist = 16
    times= 2*WINHEIGHT//dist
    for i in range(times):
        DISPLAY.fill(BGCOLOR)

        localRect.bottom = 2*WINHEIGHT - i*dist
        DISPLAY.blit(localSurf, localRect)
        if localRect.bottom == WINHEIGHT:
            '''in the center of the screen.'''
            update(delay= delay)
            if isHalf: break
        else:
            update()

def showLines(text, **kwargs):
    '''
show lines of text at center simultaneously.

available keywords:
    surf=DISPLAY,
    dest=None,
    filename=STORY,
    size=30,
    dist=15, #dist is the distance between each line
    fgcolor=FGCOLOR,
    bgcolor=BGCOLOR,
    wait=False,
    skip=False,
    waitText='按r键返回，按空格键继续...',
    blitOnTheDisplay=True,
    updateTheDisplay=True,
    clearTheSurf=True,
    showLoading=False,

CAUTION:
    this function is used widely, beware of the default kwargs' values.
    '''
    #set keywords
    surf    = kwargs.get('surf'    , DISPLAY)
    dest    = kwargs.get('dest'    , None)
    filename= kwargs.get('filename', STORY)
    size    = kwargs.get('size'    , 30)
    dist    = kwargs.get('dist'    , 15)
    fgcolor = kwargs.get('fgcolor' , FGCOLOR)
    bgcolor = kwargs.get('bgcolor' , BGCOLOR)
    wait    = kwargs.get('wait'    , False)
    skip    = kwargs.get('skip'    , False)
    waitText= kwargs.get('waitText', '按r键返回，按空格键继续...')
    blitOnTheDisplay = kwargs.get('blitOnTheDisplay', True)
    updateTheDisplay = kwargs.get('updateTheDisplay', True)
    clearTheSurf = kwargs.get('clearTheSurf', True)
    showLoading  = kwargs.get('showLoading', False)

    #wait and skip are bound together
    #this func returns skip if wait==True, else None.
    if wait and skip: return skip

    if showLoading  == True: loading(surf= surf)
    if clearTheSurf == True: surf.fill(bgcolor)

    center = surf.get_rect().center
    centerx, centery= center
    lines = text.split('\n')
    count = len(lines) #count how many lines there are

    #lineTop is a loop variable below
    height = size*count + dist*(count-1)
    lineTop= centery - (height//2)

    for line in lines:
        '''blit line by line.'''
        lineSurf = Label(filename, size, text=line, color=fgcolor).get_surf()
        lineRect = lineSurf.get_rect(centerx= centerx, top= lineTop)
        surf.blit(lineSurf, lineRect)

        lineTop += (size+dist)
        #dist is the distance between each line.
    if blitOnTheDisplay and (surf != DISPLAY):
        assert dest != None, 'missing argument \'dest\'.'
        DISPLAY.blit(surf, dest)
    if updateTheDisplay: update()
    if wait:
        skip = pause(text=waitText)
        return skip

def typeLines(text, **kwargs):
    '''
similar to showLines.
type lines of text at center.
fullscreen.

available keywords:
    surf=DISPLAY,
    dest=None,
    center=CENTER,
    filename=STORY,
    size=40,
    dist=20, #dist is the distance between each line
    highlightIndexes=(), #highlightIndexes is a tuple, containing indexes that need to be highlighted, '\n' is not counted, '-1' is available
    highlightColor = RED,
    wait=True,
    skip=False,
    waitText='按s键跳过，按空格键继续...',
    soundOn=True,
    fps=10,
    '''
    surf = kwargs.get('surf', DISPLAY)
    dest = kwargs.get('dest', None)
    filename = kwargs.get('filename', STORY)
    size = kwargs.get('size', 40)
    dist = kwargs.get('dist', 20)
    highlightIndexes = kwargs.get('highlightIndexes', ())
    highlightColor = kwargs.get('highlightColor', RED)
    wait = kwargs.get('wait', True)
    skip = kwargs.get('skip', False)
    waitText = kwargs.get('waitText', '按s键跳过，按空格键继续...')
    soundOn = kwargs.get('soundOn', True)
    fps = kwargs.get('fps', 10)

    if wait and skip: return skip
    surf.fill(BGCOLOR)

    center = surf.get_rect().center
    centerx, centery = center

    lines = text.split('\n')
    chars = sum(len(line) for line in lines)
    count = len(lines)

    #charTop, offset are loop variables below
    height = size*count + dist*(count-1)
    charTop = centery - (height // 2)
    offset = 0

    if soundOn:
        # TYPE.play(loops=-1)
        pass

    for line in lines:
        '''print line by line.'''
        #the following rect is merely a reference for the following 'print char by char'
        referenceRect = Label(filename, size, text=line).get_surf().get_rect(centerx= centerx)

        #charLeft is a loop variable below
        charLeft = referenceRect.left
        for char in line:
            '''print char by char.'''
            ishighlighted = (
                (offset in highlightIndexes) or
                ((offset-chars) in highlightIndexes) #count from right, -1, -2, ...
                )
            if ishighlighted:
                charSurf = Label(filename, size, text=char, color=highlightColor).get_surf()
            else:
                charSurf = Label(filename, size, text=char).get_surf()
            charRect = charSurf.get_rect(left=charLeft, top=charTop)
            surf.blit(charSurf, charRect)
            if surf != DISPLAY:
                assert dest != None, 'missing argument \'dest\'.'
                DISPLAY.blit(surf, dest)
            update(fps= fps)

            #update the value of charLeft
            #the left of next char is the right of current char
            charLeft = charRect.right
            offset += 1

        #update the value of top
        #after one line is drew, move to next line(lineHeight == size)
        charTop += (size+dist)

    if soundOn:
        pass
        # TYPE.stop()

    if wait:
        skip = pause(text=waitText)
        return skip

def pause(family=STORY, size=40, text='按空格键继续...'):

    #draw 'CONTINUE'
    surf = Label(family, size, text).get_surf()
    rect = surf.get_rect(right=WINWIDTH, bottom=WINHEIGHT)
    DISPLAY.blit(surf, rect)
    update()
    while True:
        for case in event.get():
            if case.type == KEYUP:
                if case.key in (K_r, K_s): skip = True; return skip
                if case.key == K_SPACE: skip = False; return skip

def loading(delay=300, surf=DISPLAY):
    surf.fill(BGCOLOR)
    center = surf.get_rect().center
    
    localSurf = Label(LOADING, size=80, text='Loading...').get_surf()
    localRect = localSurf.get_rect(center= center)
    surf.blit(localSurf, localRect)
    update(delay= delay)#artificial delay if needed

def tip(text=None, tipList=TIPLIST_GAME, mode='showLines', size=30, dist=20, delay=0):
    '''
draw tips.
support multiline text.'''

    if text != None: pass
    else:
        #if no text are passed, choose randomly from TIPS
        text = random.choice(tipList)

    #create a blank surface, with its rect, Surface((width, height))
    width, height = 640, 160
    localSurf = Surface((width, height))
    localSurf.fill(BGCOLOR)
    localRect = localSurf.get_rect()

    ##draw text
    assert mode in ('showLines', 'typeLines'), 'invalid mode.'
    left, top = (WINWIDTH-width), 40

    if mode == 'showLines':
        showLines(
            text, surf=localSurf, dest=(left, top),
            filename=HINT, size= size, dist= dist,
            updateTheDisplay=False,
            )
    '''
    if mode == 'typeLines':
        typeLines(
            text, surf=localSurf, dest=(left, top),
            filename=HINT, size= size,
            wait=False,
            soundOn=False,
            )
    '''

    update(delay= delay)
