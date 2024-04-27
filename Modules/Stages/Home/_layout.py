'''
This module stores button instances.
'''

#classes
from ...Classes.Button import LabelButton

#constants
from ...Locals.Colors  import CYAN, YELLOW
from ...Locals.Display import CENTERX, CENTERY, DISPLAY, WINHEIGHT, WINWIDTH
from ...Locals.Fonts   import BUTTON

#basic
filename, size = BUTTON, 30
LOAD   = LabelButton(filename, size, text='继续人生')
NEW    = LabelButton(filename, size, text='新的人生')
HELP   = LabelButton(filename, size, text='帮助')
QUIT   = LabelButton(filename, size, text='退出')
ACK    = LabelButton(filename, size, text='鸣谢')
SET    = LabelButton(filename, size, text='设置')
ACHIEVE= LabelButton(filename, size, text='成就')
FATE   = LabelButton(filename, size, text='命运')

EXTRA = LabelButton(BUTTON, size, text="额外演示")

#position
LOAD   .config(x=(None, CENTERX, None), y=(CENTERY-60, None, None))
NEW    .config(x=(None, CENTERX, None), y=(CENTERY-20, None, None))
HELP   .config(x=(None, CENTERX, None), y=(CENTERY+20, None, None))
QUIT   .config(x=(None, CENTERX, None), y=(CENTERY+60, None, None))
ACK    .config(x=(0   , None,    None), y=(None, None, WINHEIGHT-40))
SET    .config(x=(0   , None,    None), y=(None, None, WINHEIGHT))
ACHIEVE.config(x=(None, None,WINWIDTH), y=(None, None, WINHEIGHT-40))
FATE   .config(x=(None, None,WINWIDTH), y=(None, None, WINHEIGHT))

EXTRA.config(x=(None, CENTERX, None), y = (None, None, WINHEIGHT-100))
