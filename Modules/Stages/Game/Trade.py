'''
This module sets up Trade page.
'''

#classes
from pygame import Rect, Surface
from ...Classes.Button import LabelButton, TradeButton, drawButtons, moveAndClick
from ...Classes.Text   import Label, fade, tip

#constants
from ...Locals.Basics  import LIVINGCARDS, TIPLIST_TRADE
from ...Locals.Colors  import BGCOLOR, CYAN, FGCOLOR, RED
from ...Locals.Display import CENTER, DISPLAY, WINWIDTH, update
from ...Locals.Fonts   import BUTTON, MARGIN
from ...Locals.Time    import DELAY

#functions
from ...DebugTools import traceBug
from copy import deepcopy
from ...Data.Running   import loadTempPlayer, loadTempTrade, updateTempPlayer, updateTempTrade

#modules
import random, sys


def trade():

    DISPLAY.fill(BGCOLOR)

    ##draw unchanged letters, similar to __init__.letters()
    filename, size = MARGIN, 40
    surf = Label(filename, size, text='BUY').get_surf()
    rect = surf.get_rect(top=200)
    DISPLAY.blit(surf, rect)

    surf = Label(filename, size, text='SELL').get_surf()
    rect = surf.get_rect(top=440)
    DISPLAY.blit(surf, rect)

    ##
    CARD1= TradeButton()
    CARD2= TradeButton()
    CARD3= TradeButton()

    FOOD = TradeButton()
    WATER= TradeButton()
    VITA = TradeButton()
    ANTIB= TradeButton()
    ANTII= TradeButton()
    TRANQ= TradeButton()

    FOOD .text = '食物卡'
    WATER.text = '水卡'
    VITA .text = '维生素卡'
    ANTIB.text = '抗生素卡'
    ANTII.text = '抗感染卡'
    TRANQ.text = '镇静剂卡'

    TOP1 = 280
    TOP2 = 520
    TOP3 = 720
    COL1 = 160
    COL2 = 480
    COL3 = 800
    CARD1.x= (None, COL1, None)
    CARD1.y= (TOP1, None, None)
    CARD2.x= (None, COL2, None)
    CARD2.y= (TOP1, None, None)
    CARD3.x= (None, COL3, None)
    CARD3.y= (TOP1, None, None)
    FOOD .x= (None, COL1, None)
    FOOD .y= (TOP2, None, None)
    WATER.x= (None, COL2, None)
    WATER.y= (TOP2, None, None)
    VITA .x= (None, COL3, None)
    VITA .y= (TOP2, None, None)
    ANTIB.x= (None, COL1, None)
    ANTIB.y= (TOP3, None, None)
    ANTII.x= (None, COL2, None)
    ANTII.y= (TOP3, None, None)
    TRANQ.x= (None, COL3, None)
    TRANQ.y= (TOP3, None, None)

    BACK = LabelButton(filename=BUTTON, size=60, text='返回')
    BACK.config(
        x=(0, None, None),
        y=(None, None, WINWIDTH),
        )

    player = loadTempPlayer()

    #loading trade info
    try:
        '''try loading trade_info from TEMP first.'''
        trade_info = loadTempTrade()
        assert 0 < trade_info['day'] <= 30
        assert len(trade_info['cardsOnSell']) == len(trade_info['sellPrices']) == 3
        assert len(trade_info['buyPrices']) == 6

        assert trade_info['day'] == player['day'], 'need update.'
    except Exception:
        '''
in one case, TypeError occurs during loadTempTrade because there's no trade_info in TEMP,
in this case, create one.
        '''
        traceBug(location='TRADE')
        trade_info = create_trade_info(player)


    card1, card2, card3 = trade_info['cardsOnSell']
    Ecard1, Ecard2, Ecard3 = trade_info['cardsForExchange']
    sellPrice1, sellPrice2, sellPrice3 = trade_info['sellPrices']
    CARD1.text, CARD2.text, CARD3.text = card1, card2, card3
    buyPrice1, buyPrice2, buyPrice3, buyPrice4, buyPrice5, buyPrice6 = trade_info['buyPrices']


    buttonList = [BACK, CARD1, CARD2, CARD3, FOOD, WATER, VITA, ANTIB, ANTII, TRANQ]
    drawButtons(*buttonList)

    #tip should be outside the 'while' loop below
    tip(tipList=TIPLIST_TRADE, mode='showLines')
    #this mode is also used in Button.TradeButton

    while True:

        VEND.play(loops=-1)

        FOOD .tip = '你有%d张食物卡。\n今天的市场价是1张%d元。\n点击以出售。' % (player['食物卡'], buyPrice1)
        WATER.tip = '你有%d张水卡。\n今天的市场价是1张%d元。\n点击以出售。' % (player['水卡'], buyPrice2)
        VITA .tip = '你有%d张维生素卡。\n今天的市场价是1张%d元。\n点击以出售。' % (player['维生素卡'], buyPrice3)
        ANTIB.tip = '你有%d张抗生素卡。\n今天的市场价是1张%d元。\n点击以出售。' % (player['抗生素卡'], buyPrice4)
        ANTII.tip = '你有%d张抗感染卡。\n今天的市场价是1张%d元。\n点击以出售。' % (player['抗感染卡'], buyPrice5)
        TRANQ.tip = '你有%d张镇静剂卡。\n今天的市场价是1张%d元。\n点击以出售。' % (player['镇静剂卡'], buyPrice6)

        CARD1.tip = (
            '要获得1张%s，\n需要%d张%s来交换。\n你有%d张%s，点击以购买。' %
            (card1, sellPrice1, Ecard1, player[Ecard1], Ecard1)
            )
        CARD2.tip = (
            '要获得1张%s，\n需要%d张%s来交换。\n你有%d张%s，点击以购买。' %
            (card2, sellPrice2, Ecard2, player[Ecard2], Ecard2)
            )
        CARD3.tip = (
            '要获得1张%s，\n需要%d张%s来交换。\n你有%d张%s，点击以购买。' %
            (card3, sellPrice3, Ecard3, player[Ecard3], Ecard3)
            )

        choice = moveAndClick(*buttonList)

        if choice == BACK:
            VEND.fadeout(DELAY)
            updateTempPlayer(player)
            updateTempTrade (trade_info)
            fade(DISPLAY)
            return

        if choice == FOOD:
            if player['食物卡'] > 0:
                player['食物卡'] -= 1
                player['money'] += buyPrice1
                SELL.play()
            else:
                tip('你没有食物卡！', delay=DELAY)
        if choice == WATER:
            if player['水卡'] > 0:
                player['水卡'] -= 1
                player['money'] += buyPrice2
                SELL.play()
            else:
                tip('你没有水卡！', delay=DELAY)
        if choice == VITA:
            if player['维生素卡'] > 0:
                player['维生素卡'] -= 1
                player['money'] += buyPrice3
                SELL.play()
            else:
                tip('你没有维生素卡！', delay=DELAY)
        if choice == ANTIB:
            if player['抗生素卡'] > 0:
                player['抗生素卡'] -= 1
                player['money'] += buyPrice4
                SELL.play()
            else:
                tip('你没有抗生素卡！', delay=DELAY)
        if choice == ANTII:
            if player['抗感染卡'] > 0:
                player['抗感染卡'] -= 1
                player['money'] += buyPrice5
                SELL.play()
            else:
                tip('你没有抗感染卡！', delay=DELAY)
        if choice == TRANQ:
            if player['镇静剂卡'] > 0:
                player['镇静剂卡'] -= 1
                player['money'] += buyPrice6
                SELL.play()
            else:
                tip('你没有镇静剂卡！', delay=DELAY)

        if choice == CARD1:
            if player[Ecard1] >= sellPrice1:
                player[Ecard1] -= sellPrice1
                player[card1] += 1
                BUY.play()
            else:
                tip('你没有足够的%s！' % Ecard1, delay=DELAY)
        if choice == CARD2:
            if player[Ecard2] >= sellPrice2:
                player[Ecard2] -= sellPrice2
                player[card2] += 1
                BUY.play()
            else:
                tip('你没有足够的%s！' % Ecard2, delay=DELAY)
        if choice == CARD3:
            if player[Ecard3] >= sellPrice3:
                player[Ecard3] -= sellPrice3
                player[card3] += 1
                BUY.play()
            else:
                tip('你没有足够的%s！' % Ecard3, delay=DELAY)

#
def create_trade_info(player):
    '''
sell and buy is relative to the vending machine, not the consumer.
    '''
    print('creating trade info...')
    trade_info = dict(
        day=player['day'],
        cardsOnSell=[], cardsForExchange=[], sellPrices=[],
        buyPrices=[],
        )

    availableCards = deepcopy(LIVINGCARDS)
    exchangeCards  = ['C级卡', 'B级卡', 'S级卡', 'R级卡', 'SR级卡']
    for i in range(3):
        '''choose 3 cards non-repeatedly.'''
        card = random.choice(availableCards)
        trade_info['cardsOnSell'].append(card)
        Ecard = random.choice(exchangeCards)
        trade_info['cardsForExchange'].append(Ecard)
        if Ecard == 'C级卡':
            price = random.randint(10, 20)
        if Ecard == 'B级卡':
            price = random.randint(8, 18)
        if Ecard == 'S级卡':
            price = random.randint(5, 10)
        if Ecard == 'R级卡':
            price = random.randint(3, 8)
        if Ecard == 'SR级卡':
            price = random.randint(1, 5)

        if '大妈' in player['attrs']:
            price -= 3
            if price < 1 or '商人' in player['attrs']: price = 1
        trade_info['sellPrices'].append(price)

        availableCards.remove(card)
        exchangeCards.remove(Ecard)

    for i in range(6):
        price = random.randint(50, 100)
        if '商人' in player['attrs']:
            price *= 2
        trade_info['buyPrices'].append(price)

    print('trade info created.')
    return trade_info
