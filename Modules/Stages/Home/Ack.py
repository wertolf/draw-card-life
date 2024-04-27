'''
This module sets up page for acknowledgement.
'''

#classes
from ...Classes.Text import Label, fade, rollLines

#constants
from ...Locals.Display import DISPLAY, WINWIDTH, WINHEIGHT, update
from ...Locals.Fonts   import XINWEI
from ...Locals.Time    import DELAY

#functions
from ...Signature import signature

#modules
from pygame.mixer import music

def ack():
    argList = []

    argList.append(
        dict(
            text=(
'''
一部作品的诞生，
需要很多人的帮助。

即便是这样一个简单的小游戏，
也是如此。
'''
                ),
            delay=2000,
            )
        )

    argList.append(
        dict(
            text=(
'''
因此，在这里，
我要向帮助过我的人
表示感谢。
'''
                ),
            delay=1000,
            )
        )

    argList.append(
        dict(
            text=(
'''
感谢@caodg
带我走入了python的世界

感谢Mark Lutz
引领我更深入地了解这门语言

感谢Al Sweigart
教我如何使用pygame
'''
                ),
            delay=3000,
            )
        )

    argList.append(
        dict(
            text=(
'''
感谢@人生如寄
向我描绘最初的梦想

感谢@奥克西博士
给我开发这款游戏的冲动

感谢@DoubleS和@朱学长
在开发过程中与我交流
'''
                ),
            delay=3000,
            )
        )

    argList.append(
        dict(
            text=(
'''
感谢@汪汪 @zzf @ttc @V
试玩了这款游戏
并给出反馈
'''
                ),
            delay=3000,
            )
        )

    argList.append(
        dict(
            text=(
'''
最后，
特别感谢@nikonikonikoni
在我想要放弃的时候，
和你的交谈，
给了我继续下去的勇气。
'''
                ),
            isHalf=True,
            )
        )

    music.load(ACKBGM)
    music.play(loops=-1)

    filename, size = XINWEI, 60
    for kwargs in argList:
        kwargs['filename'] = filename
        kwargs['size'] = size
        rollLines(**kwargs)

    update(delay=1000)
    signature()

    music.fadeout(2000)
    fade(DISPLAY, speed=5, delay=2000)
