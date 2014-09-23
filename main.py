from pymongo import MongoClient
from Tkinter import *
import subprocess as comandos
from gridfs import GridFS
import sys 
import re 

fs = open("Style.txt","r")#read , write 
Test=fs.readlines()
fs.close()
ctx=Tk()


class algo:
	def __init__(self,ctx):
		self.context=ctx

	def crear(self,key,val):
		self.titulo=Label(self.context)
		self.titulo["text"]="fewfge"
		self.titulo[key]=val
		self.titulo.pack()
	def run(self):
		self.context.mainloop()

ins=algo(ctx)

json={
	"bg":"red",
	"fg":"white",
	"text":"Esneyder es la leche"
}

Esneyder=Label(ctx,json)

Esneyder.pack()
Esneyder.mainloop()

































	









































