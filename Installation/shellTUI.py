#!/usr/bin/env python
import sys
from time import sleep
clr0 = '\x1B[39m'
clr1 = '\x1B[38;5;130m'

def putText(x,y,text):
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
	sys.stdout.flush()

def setCursor(x,y):
	sys.stdout.write("\x1B[%d;%dH" % (y,x))
	sys.stdout.flush()

def systemCmd(cmd):
	sys.stdout.write(cmd)

def cls():
	print('\033c')

class Form(object):
	"""docstring for NewWin"""
	def __init__(self, text, x, y, dx, dy):
		super(Form, self).__init__()
		self.text = text
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.draw()
	def draw(self):
		_x1 = self.x
		_x2 = self.x+self.dx
		_y1 = self.y
		_y2 = self.y+self.dy
		putText(_x1,_y1,'+')
		for i in range(_x1+1, _x2-1):#draw hor. lines '='
			putText(i, _y1,'=')
			putText(i, _y2-1,'=')
		i+=1
		putText(i,_y1,'+')
		for i in range (_y1+1, _y2-1):#draw vert. lines '|'
			putText(_x1, i,'|')
			putText(_x2-1, i,'|')
		i+=1
		putText(_x1, i,'+')
		putText(_x2-1, i,'+')
		putText(_x1+2, _y1 , clr1+'['+self.text+']'+clr0)
		putText(_x2-5, _y1, '[-ox]')
class Edit(object):
	"""docstring for Edit"""
	#Edit premakne kurzor , tako da ga lahko uporabljas tudi, ce moras tja kaj izpisatu
	def __init__(self, text, x, y):
		super(Edit, self).__init__()
		self.text = text
		self.x = x
		self.y = y
		self.value = ''
		self.enabled = True
		self.draw()

	def draw(self):
		putText(self.x, self.y, clr1+self.text+clr0+':'+self.value)
		if self.enabled:
			sys.stdout.write("\x1B[%d;%dH" % (self.y,self.x+len(self.text)+1))
			sys.stdout.flush()

	def new_value(self,val):
		_val = self.value
		self.value  = val
		if len(_val)>len(val):
			for n in range(0,len(_val)):
				putText(self.x+len(self.text)+n+1,self.y,' ')
		self.draw()

	def set_new_value(self):
		self.new_value('')
		key = raw_input('')
		self.new_value(key)

class Text(object):
	"""docstring for Text"""
	def __init__(self, text, x, y):
		super(Text, self).__init__()
		self.text = text
		self.x = x
		self.y = y
		self.draw()
	def draw(self):
		putText(self.x, self.y, self.text)
	def new_text(self,val):
		self.text  = val
		self.draw()
