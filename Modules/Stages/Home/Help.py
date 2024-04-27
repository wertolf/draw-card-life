
#classes
from ...Classes.Text import Label, showLines, fade

#constants
from pygame.locals import KEYUP, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_r, K_ESCAPE
from ...Locals.Display import DISPLAY, WINWIDTH, WINHEIGHT, update
from ...Locals.Fonts   import HELP

#modules
from pygame import event

def help():
    kwargsList = []

    kwargsList.append(
        dict(
            text=(
'''
===== 写在前面 =====

感谢你打开这款游戏。

这里的"帮助"，将对游戏的功能作一说明。

你可以随时按R键返回，或按方向键翻页。
'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 万能键 =====

在大多数情况下，回车键都是可以使用的。

在大多数情况下，Esc键也都可以使用。
不过，对于某些界面而言，
通过Esc键退出游戏不会保存数据,
比如"命运"界面和"贸易"界面。

这同时也意味着，
如果你做出了令自己后悔的选择，
你有反悔的机会。

'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 命运界面 =====

你可以在"命运"界面永久提升各项能力，
想要取得最终的胜利，你不必升满所有。

'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 设置界面 =====

你可以在"设置"界面中选择
是否开启剧情，BGM等等。

'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 游戏界面 =====

----- ATTRIBUTE -----
代表玩家的属性，
在每局游戏的开始，你会随机获得5个不同的属性，
属性有好有坏，
你可以通过点击来查看属性的详细信息。

----- INVENTORY -----
代表玩家的物品栏，
这里显示了你所有的卡片。

'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 数据之gg判定 =====

有很多种gg方式：

体力为0时，你会饿死。
水分为0时，你会渴死。
精神值低于25时，你会失智而死，或者在抽到SSR后暴毙。
期限到时，你会受刑而死。

'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 数据之命运尘埃 =====

每局游戏结束时，命运尘埃的计算公式如下：

基础尘埃=
C级卡*0.01+B级卡*0.02+S级卡*0.05
+
R级卡*0.1+SR级卡*0.2
+
生存类卡*0.5+SSR级卡*1
+
存活天数*10

最终尘埃=基础尘埃*(1+命运加成)

'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
===== 如何获胜 =====

升级"命运"天赋。

合理使用自动售货机。

利用combo。
'''
                )
            )
        )

    kwargsList.append(
        dict(
            text=(
'''
已经是最后一页啦！
'''
                )
            )
        )

    for kwargs in kwargsList:
        kwargs['filename'] = HELP
        kwargs['wait'] = False
    offset= 0
    while True:
        showLines(**kwargsList[offset])
        key = pause()
        if key in (K_UP, K_LEFT):
            if offset > 0:
                offset -= 1
                fade(DISPLAY)
            else: ERROR.play()
        if key in (K_RIGHT, K_DOWN):
            if offset < len(kwargsList)-1:
                offset += 1
                fade(DISPLAY)
            else: ERROR.play()
        if key in (K_r, K_ESCAPE):
            fade(DISPLAY)
            return

def pause():
    '''this func is similar to Text.pause, with slight differences.'''
    surf = Label(family=HELP, size=40, text='按Esc键返回，按方向键翻页...').get_surf()
    rect = surf.get_rect(right=WINWIDTH, bottom=WINHEIGHT)
    DISPLAY.blit(surf, rect)
    update()
    while True:
        for action in event.get():
            if action.type == KEYUP and action.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT, K_r, K_ESCAPE):
                return action.key
