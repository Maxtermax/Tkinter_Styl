import json
from Tkinter import *



ctx=Tk()

with open('./styles/Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)


Config_Ventana=Frame(ctx)#Configuracion del ventana 
Config_Ventana.grid(column=0,row=0,padx=(70,70),pady=(100,100))
Config_Ventana.columnconfigure(0,weight=1)
Config_Ventana.rowconfigure(0,weight=1)


'''
def ObtenerValor():
	print Name.get()

Esneyder=Button(Config_Ventana,data["boton"],command=ObtenerValor)
Esneyder.grid(column=2,row=30)


v=""
Name=Entry(Config_Ventana,width=40,textvariable=v)
Name.grid(column=3,row=1)
'''

menu=Menu(ctx)

ctx.config(menu=menu)

Sub=Menu(menu)
menu.add_cascade(label="Archivo",menu=Sub)
Sub.add_command(label="abrir")
Sub.add_command(label="configuracion")
Sub.add_command(label="cerrar")

menu2=Menu(ctx)
menu2.add_cascade(label="Archivo",menu=menu2)
menu2.add_command(label="abrir")
menu2.add_command(label="configuracion")
menu2.add_command(label="cerrar")




ctx.mainloop()




































	









































