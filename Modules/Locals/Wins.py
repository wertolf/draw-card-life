'''
This module stores themed standard streams.
'''

#classes
from tkinter import Frame, Scrollbar, Text
from tkinter import Tk

#constants
from tkinter import LEFT, RIGHT
from tkinter import Y
from tkinter import END, INSERT
from tkinter import YES
from tkinter import BOTH

#modules
import sys

class FramedText(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH)

        ##
        sbar = Scrollbar(self)
        text = Text(
            master=self,
            background='#000000', foreground='#ffffff',
            insertbackground='#ffff00', insertwidth=2,
            font=('courier', 16, 'bold'),
            width=50, height=10,
            )
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT)
        
        text.insert(END, '===== Themed standard output stream =====\n\n')
        text.mark_set(INSERT, END)
        text.focus()

        self.text = text
        ##

    def write(self, text):
        self.text.insert(END, text)

    def readline(self):
        return 'hello'

STDOUT = FramedText(ROOT)
