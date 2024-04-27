'''
This module print the story during run-time.
'''

#classes
from ...Classes.Text import fade, typeLines

#constants
from ...Locals.Basics  import DDL
from ...Locals.Display import DISPLAY
from ...Locals.Time    import DELAY

#modules
from pygame import mixer

def startStory():

    # mixer.music.load(STORYBGM)
    # mixer.music.play(loops=-1)

    skip = typeLines(
        '2419年，\n中国游戏业发展恶劣。'
        )
    skip = typeLines(
        '进口游戏被禁止，\n国产游戏类型单一，\n用在游戏中的商业模式\n被移植到社会的各个领域。',
        skip= skip,
        )
    skip = typeLines(
        '想吃巧克力冰激凌？\n对不起，不能直接买，\n需要花钱抽食物卡。',
        skip= skip,
        )
    skip = typeLines(
        '你有可能抽到\n香草口味，\n草莓口味，\n等等。',
        skip= skip,
        )
    skip = typeLines(
        '想买件衣服？\n试穿合适了直接掏钱？',
        skip= skip,
        )
    skip = typeLines(
        '不行，你得掏钱去店里抽卡。\n抽到那一套，才能给你。',
        skip= skip,
        )
    skip = typeLines(
        '这样，\n商家可以收获最大的利润，\n进一步，\n国家能造就更高的GDP。',
        skip= skip,
        )
    skip = typeLines(
        '甚至，\n当有人犯罪了被关在监狱里，\n每天的食物和水也需要通过抽卡获得，\n抽到吃饭，\n抽不到饿死。',
        skip= skip,
        )
    skip = typeLines(
        '在囚禁期间，\n重犯如果能抽到10张最稀有的卡，\n就可以免刑。',
        skip= skip,
        highlightIndexes=(13, 14, 15),
        )
    skip = typeLines(
        '......',
        skip= skip,
        )
    skip = typeLines(
        '我，\n被发现在世界卡池中作弊，\n这在现在是最严重的罪。',
        skip= skip,
        )
    #skip gap
    if skip: fade(DISPLAY)
    skip = False
    skip = typeLines(
        '在监狱里，\n只要我能用每天提供的有限金钱\n抽到10张最稀有的卡，\n我就能被无罪释放。',
        skip= skip,
        highlightIndexes=(21, 22, 23),
        )
    skip = typeLines(
        '我只有%s天的时间。' % DDL,
        skip= skip,
        highlightIndexes=(3, 4, 5),
        )
    skip = typeLines(
        '这太难了。',
        skip= skip,
        )
    skip = typeLines(
        '但是，\n我首先应该考虑的是\n会不会饿死，\n或者渴死，\n或者......',
        skip= skip
        )
    skip = typeLines(
        '我必须先活下去。',
        skip= skip,
        )

    mixer.music.fadeout(DELAY)
    fade(DISPLAY)

def dieStory():

    mixer.music.load(DIEBGM)
    mixer.music.play(loops=0)

    fps  = 8
    delay= 1000
    speed= 5

    skip = typeLines(
        '牢房内幽暗的灯光，\n仿佛鬼魂一般，\n不断闪烁着。',
        fps= fps,
        )
    skip = typeLines(
        '我看着它，\n发现它也正看着我，\n我们渐渐合为一体。',
        skip= skip,
        fps= fps,
        )
    skip = typeLines(
        '......',
        skip= skip,
        fps= fps,
        )

    mixer.music.fadeout(delay)
    fade(DISPLAY, speed= speed)

def killStory():
    DOOR.play()

    waitText = '按空格键继续...'
    typeLines(
        '门开了。',
        waitText= waitText,
        )
    typeLines(
        '\"坚持到今天，辛苦你了。\"\n那人说道。',
        waitText= waitText,
        )
    typeLines(
        '\"不过，\"\n他笑了。',
        waitText= waitText,
        )

    SHOT.play()
    typeLines(
        '......',
        wait=False,
        )
    fade(DISPLAY, speed=5)
def winStory():
    '''skip is not available here.'''
    speed = 5
    fps = 8
    mixer.music.load(WINBGM1)

    typeLines(
        '当我拾起最后一张SSR级卡时，\n门开了。',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    typeLines(
        '我重获自由。',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    mixer.music.play(loops=0)
    typeLines(
        '我看到成千上万的和我一样，\n在狱中挣扎，\n与幸运女神博弈。',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    typeLines(
        '这个时代，\n也许只有这一种罪了吧，\n我想。',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    typeLines(
        '走在久违的阳光下，\n我突然有些不知所措。\n',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    typeLines(
        '我看到大街上，商场里，\n人们为了得到自己想要的东西，\n绞尽脑汁，\n抽卡，交易，再抽卡。',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    typeLines(
        '他们，和狱中人，\n又有什么两样呢？',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    mixer.music.fadeout(2000)
    mixer.music.load(WINBGM2)
    mixer.music.play(loops=0)
    typeLines(
        '我顿时慌张起来。',
        wait=False,
        fps= fps,
        )
    fade(DISPLAY, speed= speed)
    typeLines(
        '哪儿，才是我的家呢？',
        size=80,
        wait=False,
        fps=5,
        )
    fade(DISPLAY, speed=5)
    mixer.music.fadeout(DELAY)
