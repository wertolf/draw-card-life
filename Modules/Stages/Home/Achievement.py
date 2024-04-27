'''
This module sets up achievement page.
'''


#classes
from ...Classes.Text   import Label
from ...Classes.Button import LabelButton, drawButtons, moveAndClick

#constants
from ...Locals.Colors  import GREY
from ...Locals.Display import CENTERX, DISPLAY, WINHEIGHT, update
from ...Locals.Fonts   import *

#functions
from ...Data.Running import loadTempUser

def achievement():
    user = loadTempUser()

    filename, size = ARVO, 60

    surf = Label(filename, size, 'ACHIEVEMENTS').get_surf()
    rect = surf.get_rect(centerx=CENTERX, top=40)
    DISPLAY.blit(surf, rect)

    filename, size = SOUL43, 60

    TOP, LEFT, RIGHT = 200, 200, 800
    surf = Label(filename, size, '饥寒交迫 I', color=GREY).get_surf()
    rect = surf.get_rect(left=LEFT, top=TOP)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '未达成', color=GREY).get_surf()
    rect = surf.get_rect(right=RIGHT, top=TOP)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '饥寒交迫 II', color=GREY).get_surf()
    rect = surf.get_rect(left=LEFT, top=TOP+80)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '未达成', color=GREY).get_surf()
    rect = surf.get_rect(right=RIGHT, top=TOP+80)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '精神病人 I', color=GREY).get_surf()
    rect = surf.get_rect(left=LEFT, top=TOP+160)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '未达成', color=GREY).get_surf()
    rect = surf.get_rect(right=RIGHT, top=TOP+160)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '精神病人 II', color=GREY).get_surf()
    rect = surf.get_rect(left=LEFT, top=TOP+240)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '未达成', color=GREY).get_surf()
    rect = surf.get_rect(right=RIGHT, top=TOP+240)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '寿终正寝', color=GREY).get_surf()
    rect = surf.get_rect(left=LEFT, top=TOP+320)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '未达成', color=GREY).get_surf()
    rect = surf.get_rect(right=RIGHT, top=TOP+320)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '逆天改命', color=GREY).get_surf()
    rect = surf.get_rect(left=LEFT, top=TOP+400)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '未达成', color=GREY).get_surf()
    rect = surf.get_rect(right=RIGHT, top=TOP+400)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, '此功能尚未开通，敬请期待！').get_surf()
    rect = surf.get_rect(centerx=CENTERX, top=760)
    DISPLAY.blit(surf, rect)

    filename, size = SOUL43, 60
    BACK    = LabelButton(filename, size, text='返回')
    BACK.config(
        x=(0, None, None),
        y=(None, None, WINHEIGHT)
        )

    drawButtons(BACK)
    while True:
        button = moveAndClick(BACK)
        if button == BACK: return

        update()
