# -*- coding: iso-8859-1 -*-

import json
from Tkinter import *
import ttk 
import tkFont
from Class_Form import *

with open('./styles/Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)

root.geometry("654x350+250+150")
root.maxsize(width=654,height=350)
root.minsize(width=654,height=350)


form = Form(root) #Instancia de la clase formulario 

form.Label( data["Title"],data["Title_pos"])
form.Label(data["Uname"],data["Uname_pos"])
form.Label(data["PassU"],data["PassU_pos"])


def Pass_Handler(input=""):
  #Do every you gonna do
  return input#end return the input 


def Name_Handler(input):
  #Do every you gonna do
  return input#end return the input 


def Submit_Handler(btn):
	#validate here if you wanna 
	def Over_Button(event):
		btn.config({"bg":"#016899"})
	#end Over_Button

	def Out_Button(event):
		btn.config({"bg":"#007cb6"})
	#end Out_Button
	
	def validate():
		print name.get() , "Nombre \n"
		name.config(bg="red")
		passW.config(bg="green")
		print passW.get() , "Contraseña"
	
	#end validate 

	#events 
	btn.bind("<Enter>",Over_Button)	
	btn.bind("<Leave>",Out_Button)	
	btn.bind("<FocusIn>",Over_Button)	
	btn.bind("<FocusOut>",Out_Button)	
	btn.config(command=validate)	
	#end events 



passW=form.Input(data["EPass"],data["EPass_pos"],Pass_Handler)

name=form.Input(data["Ename"],data["Ename_pos"],Name_Handler)

form.Button(data["entrar"],data["entrar_pos"],Submit_Handler)



form.Run({"bg":"white"})#config windows 


#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm 
