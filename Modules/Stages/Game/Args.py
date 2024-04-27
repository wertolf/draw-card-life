'''
This module stores arguments used in Game.py.
'''

from ...Locals.Colors  import BLUE, DARKYELLOW, GREEN, RED
from ...Locals.Display import CENTERX, WINWIDTH

argList_topMargin = [
    dict(key='money', x=(   0,None,None),     y=(0, None, None)),
    dict(key='day'  , x=(None,CENTERX,None),  y=(0, None, None)),
    dict(key='status',x=(None,None,WINWIDTH), y=(0, None, None)),
    ]

argList_bars = [
    dict(char='体力', x=(0, None, None), y=(0, None, None), key='hunger', color=RED),
    dict(char='水分', x=(0, None, None), y=(40,None, None), key='thirst', color=BLUE),
    dict(char='精神', x=(0, None, None), y=(80,None, None), key='sanity', color=DARKYELLOW),
    ]

#column 1-3
COL1 = CENTERX - 160
COL2 = CENTERX
COL3 = CENTERX + 160
argList_items = [
    dict(y=( 20, None, None), x=(None, COL1, None), key='C级卡',  color=None),
    dict(y=( 20, None, None), x=(None, COL2, None), key='B级卡',  color=None),
    dict(y=( 20, None, None), x=(None, COL3, None), key='S级卡',  color=None),
    dict(y=( 60, None, None), x=(None, COL1, None), key='R级卡',  color=None),
    dict(y=( 60, None, None), x=(None, COL2, None), key='SR级卡', color=None),
    dict(y=( 60, None, None), x=(None, COL3, None), key='SSR级卡',color=RED),
    dict(y=(100, None, None), x=(None, COL1, None), key='食物卡', color=GREEN),
    dict(y=(140, None, None), x=(None, COL1, None), key='水卡',  color=GREEN),
    dict(y=(100, None, None), x=(None, COL2, None), key='抗感染卡',color=GREEN),
    dict(y=(140, None, None), x=(None, COL2, None), key='镇静剂卡',color=GREEN),
    dict(y=(100, None, None), x=(None, COL3, None), key='维生素卡',color=GREEN),
    dict(y=(140, None, None), x=(None, COL3, None), key='抗生素卡',color=GREEN),
]
