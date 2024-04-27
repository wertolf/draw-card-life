'''
This module stores button instances for __init__.py
it is not run until __init__.game is called.
'''

##imports
#classes
from ...Classes.Button import GameButton

#constants
from ...Locals.Colors  import RED
from ...Locals.Display import CENTERX, WINWIDTH, WINHEIGHT
from ...Locals.Fonts   import BUTTON

#CAUTION: run-time data, it is not run until __init__.game is called
from ...Data.Running import loadTempPlayer
player = loadTempPlayer()

filename, size = BUTTON, 30

##action buttons
DRAW = GameButton(filename, size, text='抽卡')
EAT  = GameButton(filename, size, text='进食')
DRINK= GameButton(filename, size, text='喝水')
CALM = GameButton(filename, size, text='冷静')
CURE = GameButton(filename, size, text='治疗')
NEXT = GameButton(filename, size, text='下一天')
TRADE = GameButton(filename, size, text='交易')

DRAW .tip = '1张抽卡券的价格是10元。'
EAT  .tip = '使用1张食物卡，恢复10点体力。'
DRINK.tip = '使用1张水卡，恢复10点水分。'
CALM .tip = '使用1张镇静剂卡，恢复10点精神。'
CURE .tip = '使用相应的医疗类卡，治愈你的疾病。'
NEXT .tip = '睡觉。\n迎接下一天的到来。'
TRADE.tip = '牢房里有一台自动售货机。'

COL1 = CENTERX - 160
COL2 = CENTERX
COL3 = CENTERX + 160

ROW3 = WINHEIGHT - 40
ROW2 = ROW3 - 40
ROW1 = ROW2 - 40

DRAW.config(
    x=(None, COL2, None),
    y=(None, ROW1, None),
)
EAT.config(
    x=(None, COL1, None),
    y=(None, ROW2, None),
)
DRINK.config(
    x=(None, COL2, None),
    y=(None, ROW2, None),
)
CALM.config(
    x=(None, COL3, None),
    y=(None, ROW2, None),
)
CURE.config(
    x=(None, COL1, None),
    y=(None, ROW3, None),
)
NEXT.config(
    x=(None, COL2, None),
    y=(None, ROW3, None),
)
TRADE.config(
    x=(None, COL3, None),
    y=(None, ROW3, None),
)

##attribute buttons
#text are not set yet, set in __init__.py

size  = 30
ATTR1 = GameButton(filename, size, text=player['attr1'])
ATTR2 = GameButton(filename, size, text=player['attr2'])
ATTR3 = GameButton(filename, size, text=player['attr3'])
ATTR4 = GameButton(filename, size, text=player['attr4'])
ATTR5 = GameButton(filename, size, text=player['attr5'])

attribute_row = 320
col_offset = [-320, -160, 0, 160, 320]

ATTR1.config(
    y=(None, attribute_row, None),
    x=(None, CENTERX+col_offset[0], None),
)
ATTR2.config(
    y=(None, attribute_row, None),
    x=(None, CENTERX+col_offset[1], None),
)
ATTR3.config(
    y=(None, attribute_row, None),
    x=(None, CENTERX+col_offset[2], None),
)
ATTR4.config(
    y=(None, attribute_row, None),
    x=(None, CENTERX+col_offset[3], None),
)
ATTR5.config(
    y=(None, attribute_row, None),
    x=(None, CENTERX+col_offset[4], None),
)

buttonList  = [DRAW, EAT, DRINK, CALM, CURE, NEXT, TRADE]
disableList = []

buttonDict = dict(
    draw=DRAW, eat=EAT, drink=DRINK, calm=CALM, cure=CURE, next=NEXT, trade=TRADE,
    )

for i in range(1, 6):
    self = eval('ATTR%d' % i)
    key = 'attr%d' % i

    self.tip = '点击以查看详细信息。'
    self.config(highlight=RED)

    buttonList.append(self)
    buttonDict[key] = self
