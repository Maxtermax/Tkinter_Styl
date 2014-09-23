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

json={
	"bg":"red",
	"fg":"white",
	"text":"Esneyder es la leche"
}

Esneyder=Label(ctx,json)

Esneyder.pack()
Esneyder.mainloop()

































	









































