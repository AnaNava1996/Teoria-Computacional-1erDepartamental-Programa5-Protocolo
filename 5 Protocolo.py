from time import sleep
from random import randint
from tkinter import *


def Graficar():
    ventana = Tk()
    c = Canvas(ventana,width=500,height=500)
    ventana.geometry("500x500")

    c.create_oval(48,71,305,156)
    c.create_oval(256,81,341,146)
    c.create_oval(256,81,341,146)

    c.create_oval(41,71,126,156,fill="pink")####
    c.create_oval(226,71,311,156,fill="pink")#arri dere

    c.create_line(5,110,41,110)
    c.create_oval(38,107,44,112,fill="black")
    c.create_oval(107,145,116,154,fill="black")
    c.create_oval(240,74,250,83,fill="black")
    c.create_oval(290,145,300,154,fill="black")
    start=Label(ventana,text="start",font="Helvetica 11").place(x=7,y=80)
    estado0=Label(ventana,text="ready",bg="pink",font="Helvetica 16").place(x=58,y=100)
    estado0=Label(ventana,text="sending",bg="pink",font="Helvetica 16").place(x=230,y=100)
    datain=Label(ventana,text="data in",font="Helvetica 13").place(x=150,y=45)
    datain=Label(ventana,text="back",font="Helvetica 13").place(x=153,y=157)
    cadenas=Label(ventana,text="50 cadenas",font="Helvetica 13").place(x=226,y=45)
    seg=Label(ventana,text="1 seg",font="Helvetica 13").place(x=342,y=100)

    c.place(x=0,y=0)
    ventana.mainloop()


c=input("Intentar(v),grafico(g), salir(s): ")
while(c!='s'):
    if(c=='v'):
        onOff=randint(0,1)
        if(str(onOff)=='1'):
            for i in range(0,50):#genera 50 cadenas
                cad3=""
                for h in range(0,32):#32 caracteres
                    cad2=str(randint(0,1))#ceros y 1's random
                    cad3=str(cad3+cad2)#concatenando en la cadena
                    if(h==31):#para que no imprima piramedes
                        print(str(cad3))
                        f=open('Cadena.txt','a')
                        f.write(str(cad3)+"\n")
                        f.close()
            c=input("Intentar(v),grafico(g), salir(s): ")
            sleep(1)
            l=open('Cadena.txt','r+')
            for line in l.readlines():
                estado=0
                for k in line:
                    w=k
                    if(k=='1'):
                        if(estado==0):
                            estado=1
                        elif(estado==1):
                            estado=0
                        elif(estado==3):
                            estado=2
                        else:
                            estado=3
                    elif(k=='0'):
                        if(estado==0):
                            estado=2
                        elif(estado==2):
                            estado=0
                        elif(estado==1):
                            estado=3
                        else:
                            estado=1
                if(estado==0):
                    ar=open('Analisis.txt','a+')
                    for w in line:
                        ar.write(str(w))
                    ar.close()

            l.close()
        else:
            print("Apagado")
            c=input("Intentar(v),grafico(g), salir(s): ")
    elif(c=='g'):
        Graficar()
        c=input("Intentar(v),grafico(g), salir(s): ")
    else:
        print("invalido")
        c=input("Intentar(v),grafico(g), salir(s): ")
        
