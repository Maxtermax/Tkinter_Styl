# -*- coding: iso-8859-1 -*-
import json,sys,re
from Tkinter import *
sys.path.append("Form")
from Class_Form import *
from PIL import ImageTk
import Image

root = Tk()
root.geometry("654x350+250+150")
root.maxsize(width=654,height=350)
root.minsize(width=654,height=350)

with open('./styles/Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)

form = Form(root) #Instancia de la clase formulario 
form.Label( data["Title"],data["Title_pos"])
form.Label(data["Uname"],data["Uname_pos"])
form.Label(data["PassU"],data["PassU_pos"])


def Pass_Handler(input=""):
	#Events
#	input.bind("<Key>",val_max)	
	#End Events 
	return input
	#end return the input 


def Name_Handler(input=""):
	return input
	#end return the input 

def Submit_Handler(btn):
	img=ImageTk.PhotoImage(file="flecha.png")
	btn.config(image=img)

	def Over_Button(event):
		btn.config(bg="#016899",image=img)

	def Out_Button(event):
		btn.config(bg="#007cb6",image=img)

	def validate():
		if re.match("^[a-zA-Z0-9ñÑ]{10,15}$",passW.get()) and re.match("^[a-zA-Z0-9ñÑ]{8,}$",name.get()):
			print 'Bien pass'
		#contraseña que acepta minimo 10 y maximo 15 caracteres, numeros del 0 al 9 y letras a,z mayusculas t minusculas
		#nombre de usuario que acepta almenos 8caracteres, numeros del 0 al 9 y letras a,z mayusculas t minusculas
	#events 
	btn.bind("<Enter>",Over_Button)	
	btn.bind("<Leave>",Out_Button)	
	btn.bind("<FocusIn>",Over_Button)	
	btn.bind("<FocusOut>",Out_Button)	
	btn.config(command=validate)	
	#end events 

#form widgets 
name=form.Input(data["Ename"],data["Ename_pos"],Name_Handler)
passW=form.Input(data["EPass"],data["EPass_pos"],Pass_Handler)
form.Button(data["entrar"],data["entrar_pos"],Submit_Handler)

form.Run({"bg":"#fff"})#config windows 

#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm 
