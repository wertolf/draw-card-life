
#classes
from pygame import PixelArray
from pygame.font import Font

#modules
from pygame import time

def signature():
    filename, size = XINGKAI, 80
    #in this case, rect.width=160, rect.height=89

    fontObj = Font(filename, size)
    surface = fontObj.render('白水', False, (255, 255, 255)).convert_alpha()

    pxarray = PixelArray(surface)

    #initialize
    for pos in gen_pos((160, ), (89, )):
        set_alp(pxarray, pos, color=(255, 255, 255, 0))

    ##白
    write(
        pxarray, 
        [(30, 45), (12, 25)],
        [(25, 36), (20, 28)],
        [(20, 32), (28, 32)],
        [(20, 28), (32, 35)],
        delay=0,
        )

    write(
        pxarray, 
        [(17, 25), (35, 50)],
        [(19, 27), (45, 60)],
        delay=100,
        )

    write(
        pxarray, 
        [(22, 32), (30, 40)],
        [(32, 40), (29, 37)],
        [(40, 48), (28, 37)],
        [(48, 64), (28, 37)],
        delay=100,
        )

    write(
        pxarray, 
        [(48, 64), (37, 46)],
        [(50, 64), (46, 58)],
        [(50, 64), (58, 68)],
        [(45, 50), (50, 68)],
        delay=100,
        )

    write(
        pxarray, 
        [(27, 40), (43, 50)],
        [(35, 48), (37, 48)],
        delay=100,
        )

    write(
        pxarray, 
        [(19, 27), (60, 70)],
        [(23, 35), (56, 68)],
        [(35, 45), (55, 65)],
        )

    ##水
    write(
        pxarray,
        [(112, 125), (7, 25)],
        [(115, 120), (25, 40)],
        [(115, 120), (40, 60)],
        [(115, 120), (60, 69)],
        [(105, 116), (50, 70)],
        )

    write(
        pxarray,
        [(80, 96), (25, 40)],
        [(84, 102), (20, 36)],
        [(102, 110), (30, 50)],
        [(84, 102), (40, 60)],
        [(110, 115), (30, 35)],
        delay=100,
        )

    write(
        pxarray,
        [(130, 140), (16, 38)],
        [(120, 130), (30, 37)],
        [(110, 120), (35, 40)],
        delay=100,
        )

    write(
        pxarray,
        [(120, 130), (37, 46)],
        [(130, 140), (37, 53)],
        [(140, 158), (40, 60)],
        )
    ##
    pxarray.close()

def gen_pos(rangex, rangey):
    for x in range(*rangex):
        for y in range(*rangey):
            yield (x, y)

def set_alp(pxarray, pos, color=(255, 255, 255)):
    x, y = pos
    if pxarray[x,y] != 0:
        pxarray[x,y] = color

def write(pxarray, *rangeList, delay=0):
    for (rangex, rangey) in rangeList:
        for pos in gen_pos(rangex, rangey):
            set_alp(pxarray, pos)

        update(pxarray)
        time.delay(50)

    time.delay(delay)
if __name__ == '__main__':
    import pygame
    from pygame.display import set_mode
    XINGKAI = r'..\..\Materials\Fonts\XINGKAI.TTF'
    from pygame.locals import QUIT, KEYUP

    def update(pxarray):
        DISPLAY.fill((0, 0, 0))
        DISPLAY.blit(pxarray.make_surface(), (0, 0))
        pygame.display.update()

    try:
        DISPLAY = set_mode((160, 89), pygame.FULLSCREEN)
        pygame.font.init()
        signature()

        while True:
            for event in pygame.event.get():
                if event.type in (KEYUP, QUIT):
                    raise SystemExit
    finally:
        pygame.quit()

else:
    '''
cwd == Login.py
imported by Home.Ack
    '''
    from pygame import Surface
    from Modules.Locals.Fonts   import XINGKAI
    from Modules.Locals.Display import DISPLAY
    from pygame import display

    def update(pxarray):
        localSurf = Surface((160, 89))
        localSurf.fill((0, 0, 0))
        localSurf.blit(pxarray.make_surface(), (0, 0))

        DISPLAY.blit(localSurf, (800, 800))
        display.update()
