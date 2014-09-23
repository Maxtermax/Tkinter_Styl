import json
from Tkinter import *



Canvas=Tk()

with open('./styles/Style.json') as Archivo_Styl:    
    data= json.load(Archivo_Styl)

'''
def Saluda():
	Esneyder["text"]="___________TEXTO CAMBIADO XD_____________" 
	print "Soy", Esneyder["text"]



boton=Button(Canvas,data["boton"],command=Saluda)
boton.pack()

'''


Config_Ventana=Frame(Canvas)#Configuracion del ventana 
Config_Ventana.grid(column=0,row=0,padx=(70,70),pady=(100,100))
Config_Ventana.columnconfigure(0,weight=1)
Config_Ventana.rowconfigure(0,weight=1)


def ObtenerValor():
	print Name.get()


Esneyder=Button(Config_Ventana,data["boton"],command=ObtenerValor)
Esneyder.grid(column=2,row=30)


v=""
Name=Entry(Config_Ventana,width=40,textvariable=v)
Name.grid(column=3,row=1)




Canvas.mainloop()



































	









































