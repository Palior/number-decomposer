from tkinter import *
formulario = Tk()
formulario.geometry("300x300")
entrada = Entry(formulario)
entrada.pack()
entrada.place(x=70, y=0)
texto1=Label(formulario, text="UNIDAD: ")
texto1.pack()
texto1.place(x=100, y=30)
texto2=Label(formulario, text="DECENA: ")
texto2.pack()
texto2.place(x=100, y=60)
texto3=Label(formulario, text="CENTENA: ")
texto3.pack()
texto3.place(x=100, y=90)
def calcularCentena():
    numero=entrada.get()
    numero=int(numero)
    return (numero//100)
def calcularDecena():
    numero=entrada.get()
    numero=int(numero)
    dec=numero-(100*calcularCentena())
    return (dec//10)
def calcularUnidad():
    numero=entrada.get()
    numero=int(numero)
    dec=numero-(100*calcularCentena())
    return (dec-(10*calcularDecena()))
def mostrar():
    numero=entrada.get()
    numero=int(numero)
    if (int(numero)<1000 and int(numero)>=0):
        if (numero<10):
            unidad = Label(formulario, text=calcularUnidad())
            unidad.pack()
            unidad.place(x=160,y=30)
        elif(numero<100):
            unidad = Label(formulario, text=calcularUnidad())
            unidad.pack()
            unidad.place(x=160,y=30)
            decena = Label(formulario, text=calcularDecena())
            decena.pack
            decena.place(x=160, y=60)
        else:
            unidad = Label(formulario, text=calcularUnidad())
            unidad.pack()
            unidad.place(x=160,y=30)
            decena = Label(formulario, text=calcularDecena())
            decena.pack
            decena.place(x=160, y=60)
            centena = Label(formulario, text=calcularCentena())
            centena.pack()
            centena.place(x=160,y=90)
    else:
        print ("Ingrese un numero valido POSITIVO de entre 1 y 3 digitos")
boton=Button(formulario, text='Mostrar', command=mostrar)
boton.pack()
boton.place(x=210, y=0)
formulario.mainloop()
