#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/13 15:53
# @Author: K
# @File: LearnImage.py

from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alterButton = Button(self, text='Hello', command = self.hello)
		self.alterButton.pack()
	def hello(self):
		name = self.nameInput.get() or 'www'
		messagebox.showinfo('Message', 'Hello, %s' % name)
	
app = Application()
app.master.title('Hello')
app.mainloop()