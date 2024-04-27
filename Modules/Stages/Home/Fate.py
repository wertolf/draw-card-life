'''
This module sets up Fate Page.
'''

#classes
from pygame import Rect, Surface
from ...Classes.Button import LabelButton, FateButton, drawButtons, moveAndClick
from ...Classes.Text   import Label, fade, tip, loading

#constants
from ...Locals.Basics  import FATE_KEYS, FATE_LEVEL_DICT, TIPLIST_FATE
from ...Locals.Colors  import BGCOLOR, GOLD, GREEN, PURPLE, RED
from ...Locals.Display import CENTER, DISPLAY, WINWIDTH, update
from ...Locals.Fonts   import BUTTON, MARGIN, FATE
from ...Locals.Time    import DELAY

#functions
from ...Data.Running   import loadTempUser, updateTempUser

#modules
import sys
from pygame import draw, event, mixer, mouse

def fate():

    loading(delay=0)
    DISPLAY.fill(BGCOLOR)

    ##position parameters
    COL1 = 160
    COL2 = 480
    COL3 = 800

    ##draw unchanged letters, similar to Game.letters()
    filename, size = FATE, 40

    text = '康健之魂'
    surf = Label(filename, size, text, color=GREEN).get_surf()
    rect = surf.get_rect(centerx=COL1, top=200)
    DISPLAY.blit(surf, rect)

    text = '操纵之魂'
    surf = Label(filename, size, text, color=RED).get_surf()
    rect = surf.get_rect(centerx=COL2, top=200)
    DISPLAY.blit(surf, rect)

    text = '攫取之魂'
    surf = Label(filename, size, text, color=GOLD).get_surf()
    rect = surf.get_rect(centerx=COL3, top=200)
    DISPLAY.blit(surf, rect)

    ##soul of health
    RESIST_HUNGER = FateButton()
    RESIST_THIRST = FateButton()
    RESIST_DISORD = FateButton()
    ABSORB_HUNGER = FateButton()
    ABSORB_THIRST = FateButton()
    ABSORB_SANITY = FateButton()

    RESIST_HUNGER.text = '耐受——空腹'
    RESIST_THIRST.text = '耐受——干燥'
    RESIST_DISORD.text = '耐受——疾病'
    ABSORB_HUNGER.text = '汲取——营养'
    ABSORB_THIRST.text = '汲取——水分'
    ABSORB_SANITY.text = '汲取——安宁'

    buttonList = [
        RESIST_HUNGER, RESIST_THIRST, RESIST_DISORD,
        ABSORB_HUNGER, ABSORB_THIRST, ABSORB_SANITY,
        ]

    for button in buttonList:
        button.x = (None, COL1, None)
        button.normalColor = GREEN

    RESIST_HUNGER.y= (None, 300, None)
    RESIST_THIRST.y= (None, 400, None)
    RESIST_DISORD.y= (None, 500, None)
    ABSORB_HUNGER.y= (None, 600, None)
    ABSORB_THIRST.y= (None, 700, None)
    ABSORB_SANITY.y= (None, 800, None)

    ##soul of manipulation
    FOOD   = FateButton()
    WATER  = FateButton()
    MEDI   = FateButton()
    SSR    = FateButton()

    FOOD .text = '感知——猎物'
    WATER.text = '感知——流动'
    MEDI .text = '感知——生命'
    SSR  .text = '感知——自由'

    FOOD  .x= (None, COL2, None)
    WATER .x= (None, COL2, None)
    MEDI  .x= (None, COL2, None)
    SSR   .x= (None, COL2, None)

    FOOD  .y= (None, 300, None)
    WATER .y= (None, 400, None)
    MEDI  .y= (None, 500, None)
    SSR   .y= (None, 600, None)

    buttonList = [
        FOOD, WATER, MEDI,
        ]

    for button in buttonList:
        button.normalColor = RED

    SSR.normalColor = PURPLE

    ##soul of grabbery
    DUST = FateButton()
    MONEY= FateButton()

    DUST .text = '索拿——命运'
    MONEY.text = '索拿——黄金'

    DUST .x= (None, COL3, None)
    MONEY.x= (None, COL3, None)

    DUST .y= (None, 300, None)
    MONEY.y= (None, 400, None)

    DUST .normalColor = GOLD
    MONEY.normalColor = GOLD

    ##
    BACK = LabelButton(filename=BUTTON, size=60, text='返回')
    BACK.config(
        x=(0, None, None),
        y=(None, None, WINWIDTH),
        )

    buttonList = [
        BACK,
        RESIST_HUNGER, RESIST_THIRST, RESIST_DISORD,
        ABSORB_HUNGER, ABSORB_THIRST, ABSORB_SANITY,
        FOOD, WATER, MEDI, SSR,
        DUST, MONEY,
        ]
    drawButtons(*buttonList)

    assert len(FATE_KEYS) == len(FATE_LEVEL_DICT.keys()), 'keys in fate not equal to FATE_LEVEL_DICT.keys().'

    user = loadTempUser()

    maxlevel = 3
    prices = {
        1:10, 2:20, 3:30, 4:99999999999999999999999999999,
        }
    #tip should be outside the 'while' loop below
    tip(tipList=TIPLIST_FATE, mode='showLines')
    #this mode is also used in Button.FateButton

    for (offset, button) in enumerate(buttonList[1:]):
        key = FATE_KEYS[offset]
        level = user['fate'][key]
        price = prices[level+1]
        if key == 'ssr': price *= 10
        button.tip = '当前等级：%d\n当前效果：%s\n下级效果：%s\n升级需要：%d点' % (
            level, FATE_LEVEL_DICT[key][level], FATE_LEVEL_DICT[key][level+1], price
            )

    mixer.music.load(FATEBGM)
    mixer.music.play(loops=-1)

    while True:
        showinfo(user)

        button = moveAndClick(*buttonList)
        if button == BACK:
            updateTempUser(user)
            mixer.music.fadeout(DELAY)
            fade(DISPLAY)
            return
        else:
            offset = buttonList[1:].index(button)
            key = FATE_KEYS[offset]
            level = user['fate'][key]
            if level == maxlevel:
                tip(text='已达到最高等级！', delay=DELAY)
            else:
                price = prices[level+1]
                if key == 'ssr': price *= 10
                if user['DustOfFate'] >= price:
                    level += 1
                    user['fate'][key] = level
                    user['DustOfFate'] -= price
                    price = prices[level+1]
                else: tip(text='你的点数不够！', delay=DELAY)
            button.tip = '当前等级：%d\n当前效果：%s\n下级效果：%s\n升级需要：%d点' % (
                level, FATE_LEVEL_DICT[key][level], FATE_LEVEL_DICT[key][level+1], price
                )

#other functions
def showinfo(user):
    width, height = 320, 160
    localSurf = Surface((width, height))
    localSurf.fill(BGCOLOR)

    filename, size = MARGIN, 40

    text = 'DustOfFate:'
    surf = Label(filename, size, text).get_surf()
    rect = surf.get_rect(left=0, top=40)
    localSurf.blit(surf, rect)

    text = '%.2f' % user['DustOfFate']
    surf = Label(filename, size, text).get_surf()
    rect = surf.get_rect(left=0, top=120)
    localSurf.blit(surf, rect)

    dest = (0, 0)
    DISPLAY.blit(localSurf, dest)
