
'''
This module uses OOP to build up GUI interfaces.
'''

##imports

#classes
from tkinter import Toplevel
from tkinter import Frame
from tkinter import Button, Label, Entry
from tkinter import PhotoImage
from tkinter import BooleanVar, Radiobutton
from tkinter import StringVar, OptionMenu

#constants
from tkinter import BOTTOM, LEFT, RIGHT, TOP
from tkinter import E, W
from tkinter import FLAT, GROOVE, RAISED, RIDGE, SOLID, SUNKEN
from ..Locals.Paths import GIF, ICON

#functions
from tkinter.messagebox import showinfo
from ..Data.LoadSave import loadLoginData, saveLoginData
from ..Data.LoadSave import loadUserData

#modules
import time

####items in this module

###functions
def packButtons(*buttons, padx=10, side=LEFT, **options):
    '''
pack buttons.

defaultly from left to right.
buttons should be in the same frame.
    '''
    for button in buttons:
        button.pack(side= side, padx= padx, **options)
        #default: from left to right, 10(20?) pixels per button

###classes

##buttons

class ThemedButton(Button):
    colorD = '#a0a0a0' #dehighlight color
    colorH = '#0078d7' #highlight   color
    colorP = '#ff0000' #preeeed     color
    def __init__(self, master=None, **options):
        Button.__init__(self, master, **options)
        self.config(bd=1, height=1, width=10, font=('courier', 10, ''), relief=FLAT)
        self.config(activebackground=self.colorP, background=self.colorD)

        self.bind('<Enter>', self.highlight)
        self.bind('<Leave>', self.dehighlight)

    def dehighlight(self, event): self.config(bg=self.colorD)
    def highlight  (self, event): self.config(bg=self.colorH)

##frames
class BasicFrame(Frame):
    def __init__(self, master=None, **options):
        Frame.__init__(self, master, **options)
        self.pack(padx=10, pady=10, side=TOP)

class Form(BasicFrame):
    def __init__(self, master=None, **options):
        '''this is a frame, to get access to the entry inside it, use self.entry().'''
        BasicFrame.__init__(self, master, **options)
        
        self.label = Label(self)
        self.entry = Entry(self)

        self.label.config(width=10)
        self.entry.config(width=20)
        
        self.label.pack(side=LEFT)
        self.entry.pack(side=RIGHT)
        
class LoginFrame(Frame):
    def __init__(self, master=None, **options):
        Frame.__init__(self, master, **options)
        self.pack(padx=20)
        
        self.username = Form(self)
        self.password = Form(self)
        self.username.label.config(text='用户名')
        self.password.label.config(text='密码')
        self.username.entry.focus()
        self.password.entry.config(show='*')

        self.buttonFrame = BasicFrame(self)
        self.login = ThemedButton(self.buttonFrame, text='登录')
        self.signin= ThemedButton(self.buttonFrame, text='注册')
        packButtons(self.login, self.signin)
    def submitResult(self):
        '''
return a tuple (isValidSubmit, loginDict),
if isValidSubmit == False, then loginDict == None.
        '''
        loginDict = {}
        loginDict['username'] = self.username.entry.get()
        loginDict['password'] = self.password.entry.get()

        loginList = loadLoginData()
        if loginDict in loginList:
            showinfo('登录成功！', '欢迎！', parent=self)
            return (True, loginDict)
        else:
            showinfo('登录失败！', '请重试！')
            return (False, None)

class SigninFrame(Frame):
    '''SigninFrame shared LoginFrame.submit.'''
    def __init__(self, master=None, **options):
        '''
there is little but important difference between
username/password in LoginFrame and SigninFrame,
also, buttons in each frame are different.
        '''
        Frame.__init__(self, master, **options)
        self.pack(padx=20)

        self.username = Form(self)
        self.password = Form(self)
        self.username.label.config(text='用户名')
        self.password.label.config(text='密码')
        self.username.entry.focus()
        #this time, unlike LoginFrame, we do not need to set the password to '*'

        self.buttonFrame = BasicFrame(self)
        self.signin = ThemedButton(self.buttonFrame, text='注册')
        self.cancel = ThemedButton(self.buttonFrame, text='取消')
        packButtons(self.signin, self.cancel)

    def isValidSubmit(self):
        loginDict = {}
        loginDict['username'] = self.username.entry.get()
        loginDict['password'] = self.password.entry.get()

        loginList = loadLoginData()
        #check for name conflicts
        for existDict in loginList:
            if loginDict['username'] == existDict['username']:
                showinfo('注册失败！', '用户名已存在，请重试！')
                return False

        #if no name conflict occurs...
        loginList.append(loginDict)
        saveLoginData(loginList)
        showinfo('注册成功！', '欢迎你，%s！' % loginDict['username'])
        return True

class StartFrame(Frame):
    def __init__(self, loginDict, master=None, **options):
        '''
along with startWin.__init__, this __init__ method is obviously different from others,
for you must submit one argument--loginDict.
        '''
        Frame.__init__(self, master, **options)
        self.pack(padx=20, pady=20)

        ##
        self.userDict = loadUserData(loginDict['username'])
        Label(self, text='欢迎，%s' % self.userDict['username']).pack()

        currentLoginTime = time.time()
        struct_time = time.localtime(currentLoginTime)
        year, mon, mday, wday = struct_time.tm_year, struct_time.tm_mon, struct_time.tm_mday, struct_time.tm_wday
        wday = ['一', '二', '三', '四', '五', '六', '日'][wday]
        Label(
            self,
            text='今天是%d年%d月%d日，星期%s' % (year, mon, mday, wday)
            ).pack()
        lastLoginTime = self.userDict['lastLoginTime']
        assert lastLoginTime < currentLoginTime, 'lastLoginTime larger than currentLoginTime.'
        isNotSameDay = (
            (time.localtime(lastLoginTime).tm_year != year) or
            (time.localtime(lastLoginTime).tm_mon  != mon)  or
            (time.localtime(lastLoginTime).tm_mday != mday)
            )
        if isNotSameDay:
            '''everyday bonus.'''
            showinfo('新的一天！', '每日奖励：100点命运尘埃')
            self.userDict['DustOfFate'] += 100
        self.userDict['lastLoginTime'] = currentLoginTime

        ##settings
        self.setFrame= Frame(self)
        self.setFrame.pack(side=TOP, pady=20)
        self.varDict = dict(
            isFullScreen=BooleanVar(master=self, value=True),
            language=StringVar(master=self, value='CN'),
            )
        #radioFrame
        self.radioFrame = Frame(self.setFrame)
        self.radioFrame.pack(side=TOP)
        Label(master=self.radioFrame,
              text='显示').pack(anchor=W)
        for (text, value) in [('全屏', True),
                              ('窗口',False)]:
            Radiobutton(master=self.radioFrame, text= text,
                        variable=self.varDict['isFullScreen'],
                        value= value, state='disabled').pack(side=LEFT, anchor=W)
        #language
        Label(master=self.setFrame, text='语言').pack(anchor=W)
        self.langOption = OptionMenu(
            master=self.setFrame,
            variable=self.varDict['language'], value='CN',
            )
        self.langOption.pack(side=TOP, anchor=E)
        self.langOption.bind('<Button-1>', lambda event: showinfo('嘿！', '就一种语言，你还想有几种?'))
        ##
        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=TOP, pady=20)
        self.start= ThemedButton(self.buttonFrame, text='开始游戏')
        self.exit = ThemedButton(self.buttonFrame, text='退出')
        packButtons(self.start, self.exit)

##windows
class LoginWin(Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        '''
uses loginFrame as frame, along with a gif, and the window that holds them both.
        '''
        print('setting up LoginWin...')
        Toplevel.__init__(self, master, cnf, **kw)
        self.title('登录')
        self.iconbitmap(ICON)

        self.gif  =PhotoImage(file=GIF,       master=self)
        self.label=     Label(image=self.gif, master=self)
        self.label.pack(padx=10)

        self.loginFrame = LoginFrame(self)

class SigninWin(Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        '''
uses signinFrame as frame, along with a gif, and the window that holds them both.
        '''
        print('setting up SigninWin...')
        Toplevel.__init__(self, master, cnf, **kw)
        self.title('注册')
        self.iconbitmap(ICON)

        self.gif  =PhotoImage(file=GIF,       master=self) #same as LoginWin.__init__
        self.label=     Label(image=self.gif, master=self)
        self.label.pack(padx=10)

        self.signinFrame = SigninFrame(self)

class StartWin(Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        '''
uses startFrame as frame, along with a gif, and the window that holds them both.
        '''
        print('setting up StartWin...')
        Toplevel.__init__(self, master, cnf, **kw)
        self.title('开始游戏')
        self.iconbitmap(ICON)

    def setupViaLoginInfo(self, loginDict):
        '''
Unlike other two Win classes, StartWin does not finish its drawing immediately after __init__,
for the startFrame is built up according to info contained in loginDict.
        '''
        self.startFrame = StartFrame(loginDict, master=self)
