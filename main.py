# -*- coding: iso-8859-1 -*-

import json
from Tkinter import *
from pymongo import *
import re
import ttk 
import tkFont

conx = Connection()
db = conx.data
coll = db.Colecion

with open('./styles/Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)

root = Tk()
root.geometry("654x350+250+150")

root.maxsize(width=654,height=350)
root.minsize(width=654,height=350)

Title = Label(root,data["Title"])
Title.place(data["Title_pos"])

#d = {"name": "pepito-perez",
#"pass":"perez"}
#coll.insert(d)

expU = '[a-z]+-?[a-z]+'
expP = '[a-z]+-?[a-z]+' #'/(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d){6,20}.+$)/'

def validar():
	name = Ename.get()
	passw = EPass.get()
	initU = str(db.Colecion.find_one({"name":name})["name"])
	initP = str(db.Colecion.find_one({"pass":passw})["pass"])
	if re.findall(expU,name) == [initU]:
		if re.findall(expP,passw) == [initP]:
			print "Bienvenido"
		else:
			print "Pass Err"
			print initP
	else:
		print "Name Err"

Uname = Label(root,data["Uname"])
Uname.place(data["Uname_pos"])



Ename = Entry(root,data["Ename"])
Ename.place(data["Ename_pos"])


PassU = Label(root,data["PassU"])
PassU.place(data["PassU_pos"])

EPass = Entry(root,data["EPass"])
EPass.place(data["EPass_pos"])


Entrar = Button(root,data["entrar"], command= validar)
Entrar.place(data["entrar_pos"])
Entrar.config(cursor="spraycan")


'''
photo = PhotoImage(file="Bat.gif")
w = Label(root, image=photo,width=280,height=245)
w.photo = photo
w.place(x=350,y=40)
'''

root.title("Iniciar sesion")


root.config(bg="#fff")
root.mainloop()






































	









































