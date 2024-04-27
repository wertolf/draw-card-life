'''
This module sets up the game page.
'''

#classes
from pygame import Rect, Surface
from ...Classes.Text   import Label, show, fade, loading, tip, typeLines
from ...Classes.Button import drawButtons, disableButtons, moveAndClick

#constants
from ...Locals.Basics  import ATTR_HELP_DICT, DDL, LIVINGCARDS
from ...Locals.Colors  import BGCOLOR, BLUE, FGCOLOR, GREY, GOLD, RED, YELLOW
from ...Locals.Display import CENTER, CENTERX, CENTERY, DISPLAY, WINHEIGHT, WINWIDTH, update
from ...Locals.Fonts   import ATTRIBUTE, BARS, BUTTON, INVENTORY, MARGIN, NEXTDAY, HINT, TEXT
from ...Locals.Time    import DELAY
from .Args import argList_topMargin, argList_bars, argList_items
#see DRAWFUNCS at the end of part -- drawing

#functions
from .Notice import notice
from ...Data.Running  import loadTempPlayer, loadTempUser, updateTempPlayer
from ...Patches import getRect

#modules
from pygame import draw, mixer
import importlib, random

#run-time
from .Story import startStory, dieStory, killStory, winStory
from .Trade import trade

#top-level functions
def game():
    #CAUTION: RUN-TIME data are not run until called
    global player, user
    player = loadTempPlayer()
    user   = loadTempUser  ()

    global buttonList, disableList

    #the following import startments are put inside the function
    #for TEMP file is not created at the start of the whole program
    #but import starements are run at the beginning
    from . import _layout
    importlib.reload(_layout)
    buttonList, disableList, buttonDict = _layout.buttonList, _layout.disableList, _layout.buttonDict

    if player['isNewGame'] and user['storyOn']:
        # startStory()
        pass

    loading(delay=1000)

    #draw game page for the first time, calling all drawfuncs, do not need to update the display
    drawPage()
    show(DISPLAY)

    playBGM()

    while True:
        #save dynamically in case accident happens,
        #also, in this way, there is no need for a SAVE button.
        updateTempPlayer(player)

        #activate display changes approached by player actions below
        update()

        #handling events
        button = moveAndClick(*buttonList)

        #this statement is essential for the print(condition) statement below
        condition = 'alive'
        if button == buttonDict['draw'] : condition = drawCard()
        if button == buttonDict['eat']  : eat()
        if button == buttonDict['drink']: drink()
        if button == buttonDict['calm'] : calm()
        if button == buttonDict['cure'] : cure()
        if button == buttonDict['next'] : condition = nextDay()
        if button == buttonDict['trade']:
            fade(DISPLAY)
            trade()
            player = loadTempPlayer() #update info changed during trade
            drawPage()

        for key in ['attr1', 'attr2', 'attr3', 'attr4', 'attr5']:
            if button == buttonDict[key]:
                attr = player[key]
                notice(ATTR_HELP_DICT[attr])
                drawPage(items)

        print('condition:', condition)

        if 'die' in condition:
            '''game over, and, jump out of the game loop.'''
            break
        if 'win' in condition: break

    ##after exit
    fade(DISPLAY, speed=5)
    mixer.music.fadeout(DELAY)

    if 'die' in condition:
        if 'killed' in condition:
            if user['storyOn']: killStory()
            return '大限已到。'

        if user['storyOn']: dieStory()
        if 'hunger' in condition:
            return '你饿死了。' #reporting death reason
        if 'thirst' in condition:
            return '你渴死了。'
        if 'happy' in condition:
            return '乐极生悲。'
        if 'insane' in condition:
            return '你失了智。'

    if 'win' in condition:
        '''congratulations.'''
        winStory()
        return 'victory'

##drawing funcs
def drawPage(*drawfuncs):
    '''
top-level function of all drawing functions below.

After calling this function,
changes in display are activated using display.update() outside this function.
    '''
    if drawfuncs == ():
        '''if no arguments are given, default calling all funcs and clean the screen.'''
        drawfuncs = DRAWFUNCS #call all drawfuncs
        DISPLAY.fill(BGCOLOR)

    for func in drawfuncs: func()

#naming sequence of these functions follows drawing sequence
def topMargin():
    '''draw margin at the top.'''
    global player

    #create a surface and reset to bgcolor
    localSurf = Surface((WINWIDTH, 25))
    localSurf.fill(BGCOLOR)

    #border line
    draw.line(localSurf, FGCOLOR, (0, 25), (WINWIDTH, 25), 5)

    #contents
    filename, size = MARGIN, 20
    argList = argList_topMargin
    blitList = []
    for argDict in argList:
        text = Label(filename, size,
                    text='%s: %s' % (argDict['key'].upper(), player[argDict['key']]))
        if argDict['key'].upper() == 'STATUS' and player[argDict['key']] != 'NORMAL':
            '''you are ill'''
            text.color = RED
        surf = text.get_surf()
        rect = getRect(surf, argDict['x'], argDict['y'])
        blitList.append((surf, rect))
    localSurf.blits(blitList)
    DISPLAY.blit(localSurf, (0, 0)) #(left, top)

def bars():
    '''draw bars.'''
    global player
    for key in ('hunger', 'thirst', 'sanity'):
        '''check if any overflows.'''
        if player[key] < 0  : player[key] = 0
        if player[key] > 100: player[key] = 100

    #create a surface and reset to bgcolor
    localSurf = Surface((288, 120))
    localSurf.fill(BGCOLOR)

    filename, size = BARS, 20
    argList = argList_bars
    for argDict in argList:

        ##draw chars
        label= Label(filename, size, text=argDict['char'])
        surf = label.get_surf()
        rect = getRect(surf, argDict['x'], argDict['y'])
        localSurf.blit(surf, rect)

        ###draw bar
        MAX = 200
        
        ##draw rect
        bar = Rect(0, 0, MAX, 20)
        
        #aligning with chars
        bar.topleft = rect.topright
        
        #move a little rightward
        bar.left += 20
        
        draw.rect(localSurf, FGCOLOR, bar, 2)

        ##draw blood
        blood = bar.copy()

        #width is defined through portion
        blood.width = player[argDict['key']] * (MAX//100)
        draw.rect(localSurf, argDict['color'], blood)

        #draw number
        label.text = '%d/100' % player[argDict['key']]
        surf = label.get_surf()
        rect = surf .get_rect(center=bar.center)
        localSurf.blit(surf, rect)

    DISPLAY.blit(localSurf, (0, 40))

def letters():
    '''draw unchanged letters.'''

    filename, size = TEXT, 30

    #draw 'ATTRIBUTE'
    surf = Label(filename, size, text="天赋").get_surf()
    rect = surf.get_rect(centerx=CENTERX, top=270)
    DISPLAY.blit(surf, rect)

    #draw 'INVENTORY'
    surf = Label(filename, size, text="卡包").get_surf()
    rect = surf.get_rect(centerx=CENTERX, top=360)
    DISPLAY.blit(surf, rect)

def items():
    '''draw inventory.'''
    global player

    #create a surface and reset to bgcolor
    width, height = WINWIDTH, 240
    left, top = CENTERX - (width//2), 400
    dest = (left, top)
    localSurf = Surface((width, height))
    localSurf.fill(BGCOLOR)

    ##draw items
    filename = INVENTORY
    argList = argList_items    
    for argDict in argList:
        kwargs = dict(family=filename,
                      size=20,
                      text='%s %d' % (argDict['key'], player[argDict['key']]),
                      antialias=False)
        if argDict['color']:
            kwargs['color'] = argDict['color']
        
        surf = Label(**kwargs).get_surf()
        rect = getRect(surf, argDict['x'], argDict['y'])
            
        localSurf.blit(surf, rect)

    DISPLAY.blit(localSurf, dest)

def buttons(): 
    global player
    global buttonList, disableList
    #defined in game()

    drawButtons   (*buttonList)
    disableButtons(*disableList)

    for button in buttonList: button.resetFocus()

DRAWFUNCS = [topMargin, bars, letters, items, buttons, tip] #all drawfuncs

##player actions
def drawCard():
    global player

    def cardInfo(bgcolor, fgcolor):
        '''draw a info box in the center of the screen.'''
        #draw the reference rect
        RECT = Rect(0, 0, 400, 160)
        RECT.centerx = CENTERX
        RECT.top     = 440
        draw.rect(DISPLAY, bgcolor, RECT)

        filename = HINT
        label= Label(filename, size=48, text='获得：%s' % card)
        surf = label.get_surf(hlcolor=fgcolor)
        rect = surf .get_rect(centerx=RECT.centerx, bottom=RECT.centery)
        DISPLAY.blit(surf, rect)
        p = (deck.count(card) / len(deck))*100
        label.text = '(%.2f%s)' % (p, '%') #forcing a '%'
        surf = label.get_surf(hlcolor=fgcolor)
        rect = surf .get_rect(centerx=RECT.centerx, top=RECT.centery)
        DISPLAY.blit(surf, rect)

    def SSR():
        DISPLAY.fill(BGCOLOR)

        filename = BUTTON
        surf = Label(filename, size=96, text='获得：SSR级卡！！！').get_surf()
        rect = surf.get_rect(center=CENTER)
        DISPLAY.blit(surf, rect)

        update(delay=1000)

    #do you have enough money for a draw?
    if player['money'] < 10:
        notice('你没钱了!')
        drawPage(items)
        return 'alive drawCard'
    else: player['money'] -= 10

    #draw a card, using player['deck'] to control possibilities
    deck = player['deck']
    card = random.choice(deck)

    ##changes in data
    player[card] += 1
    
    #if you do not get a living card or SSR card, you will lose sanity in a random amount
    if card not in LIVINGCARDS+['SSR级卡']:
        sanity = random.randint(11, 20)
        if '股民' in player['attrs']:
            sanity -= 10
            if '银行家' in player['attrs']:
                '''combo'''
                sanity = 1
        player['sanity'] -= sanity

    ##changes in screen
    drawPage(topMargin, bars, items) #note the order, draw items first, then the cardInfo box
    if card == 'SSR级卡':
        SSR()
        if player['sanity'] <= 25 and ('僧侣' not in player['attrs']): return 'die happy'
        else: player['sanity'] += 20
        if player['SSR级卡'] == 10:
            '''then you win.'''
            return 'win'
        if player['SSR级卡'] == 5:
            '''change bgm.'''
            mixer.music.fadeout(DELAY)
            playBGM()
        drawPage()
        show(DISPLAY)
    else:
        if card not in LIVINGCARDS: cardInfo(bgcolor=GREY, fgcolor=FGCOLOR)
        if card in LIVINGCARDS: cardInfo(bgcolor=YELLOW, fgcolor=BLUE)

        update()

    return 'alive drawCard'

def eat():
    global player, user
    if player['食物卡'] == 0:
        notice('你没有食物卡！')
    else:
        player['食物卡'] -= 1
        player['hunger'] += 5*(1+user['fate']['absorb_hunger'])
    drawPage(bars, items)

def drink():
    global player, user
    if player['水卡'] == 0:
        notice('你没有水卡！')
    else:
        player['水卡'] -= 1
        player['thirst'] += 5*(1+user['fate']['absorb_thirst'])
    drawPage(bars, items)

def calm():
    global player, user
    if player['镇静剂卡'] == 0:
        notice('你没有镇静剂卡！')
    else:
        player['镇静剂卡'] -= 1
        player['sanity'] += 5*(1+user['fate']['absorb_sanity'])
    drawPage(bars, items)

def cure():
    global player
    if player['status'] == 'NORMAL':
        notice('你没病。')
    else:
        if player['status'] == 'FEVER':
            if player['抗生素卡'] == 0:
                notice('你没有抗生素卡！')
            else:
                player['抗生素卡'] -= 1
                player['status'] = 'NORMAL'
                notice('你恢复了健康。')
                playBGM()
        if player['status'] == 'INFECTION':
            if player['抗感染卡'] == 0:
                notice('你没有抗感染卡！')
            else:
                player['抗感染卡'] -= 1
                player['status'] = 'NORMAL'
                notice('你恢复了健康。')
                playBGM()
        if player['status'] == 'BADBLOOD':
            if player['维生素卡'] == 0:
                notice('你没有维生素卡！')
            else:
                player['维生素卡'] -= 1
                player['status'] = 'NORMAL'
                notice('你恢复了健康。')
                playBGM()
    drawPage(topMargin, items)

def nextDay():
    global player, user

    isIllLastDay = (player['status'] != 'NORMAL')
    player['day'] += 1

    ##loss/gain calculation
    attrs = player['attrs']

    #income
    income = random.randint(50, 150)
    if '银行家' in attrs: income += player['money']*0.3
    income *= (1+user['fate']['money']*0.1)
    player['money'] += int(income)
    
    #hunger
    #note: use if instead of elif, otherwise different effects cannot concatenate
    hunger = 50
    if '方丈' in attrs: hunger -= 10
    if '肥宅' in attrs: hunger += 10
    hunger -= user['fate']['resist_hunger']*10
    if '酒鬼' in attrs and '肥宅' in attrs: hunger = 5
    player['hunger'] -= hunger

    #thirst
    thirst = 50
    if '酒鬼' in attrs: thirst += 10
    thirst -= user['fate']['resist_thirst']*10
    if player['status'] == 'FEVER': thirst += 20
    if '酒鬼' in attrs and '肥宅' in attrs: thirst = 5
    player['thirst'] -= thirst

    #sanity
    #note: sanity recovers if you are healthy
    sanity = 10
    if '股民' in attrs: sanity += 10
    if player['status'] != 'NORMAL': sanity -= 30
    player['sanity'] += sanity

    ##
    filename, size = NEXTDAY, 64
    text  = ''
    text += 'DAY: %d' % player['day']
    text += '\n'
    text += '距离行刑还有%d天' % (DDL+1-player['day'])
    typeLines(
        text,
        filename= filename, size= size, dist=160,
        highlightIndexes=(-1, -2),
        waitText='按空格键继续...',
        )

    updateTempPlayer(player)

    ##death penalty
    isImmune = ('方丈' in player['attrs']) and ('僧侣' in player['attrs'])

    if DDL+1-player['day']== 0:
        return 'die killed'
    if player['hunger'] <= 0:
        if not isImmune:
            return 'die hunger'
    if player['thirst'] <= 0:
        if not isImmune:
            return 'die thirst'
    if player['sanity'] <=25:
        if '僧侣' not in player['attrs']:
            return 'die insane'

    ##next day begins
    drawPage()

    ##acquire illness
    if player['status'] == 'NORMAL':
        '''if you are ill already, skip'''
        disord_list = ['FEVER', 'INFECTION', 'BADBLOOD']*3
        for i in range(user['fate']['resist_disord']): disord_list += ['NORMAL']*9
        player['status'] = random.choice(disord_list)
        if player['status'] != 'NORMAL':
            notice('你生病了：\t%s.' % player['status'])
    else: pass

    notice('你获得了%d块钱！' % income)
    drawPage(topMargin, items)
    if player['status'] != 'NORMAL' and not isIllLastDay: playBGM()
    return 'alive nextDay'

##other funcs
def playBGM():
    global player, user

    return

    if user['bgmOn']:
        if 0 <= player['SSR级卡'] < 5: mixer.music.load(GAMEBGM1)
        if 5 <= player['SSR级卡'] < 10:mixer.music.load(GAMEBGM2)
        if player['status'] != 'NORMAL': mixer.music.load(ILLBGM)
        mixer.music.play(loops=-1)
