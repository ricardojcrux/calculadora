from tkinter import *
import keyboard

valor,i,termino = 0,0,''
z = 0
def block(x):
	return 'break'

def barrido(x):
	global z,i
	if z == 0:
		window.delete(0,END)

def funcion(x):
	barrido(0)
	global z
	z += 1
	window.insert(END,x)

def limpiar():
    global valor, i, termino, z
    valor, i, z, termino = 0,0,0,''
    window.delete(0,END)
    window.insert(0,0)
    
def suma():
	entrada = float(window.get())
	global valor, i, termino, z
	valor += entrada
	window.delete(0,END)
	i += 1
	z += 1
	termino = 'suma'
    
def resta():
	entrada = float(window.get())
	global valor, i, termino, z
	if i == 0:
		valor += entrada
	else:
		valor -= entrada
	window.delete(0,END)
	i += 1
	z += 1
	termino = 'resta'
            
def multiplicacion():
	entrada = float(window.get())
	global valor, i, termino, z
	if i == 0:
		valor += entrada
	else:
		valor *= entrada
	window.delete(0,END)
	i += 1
	z += 1
	termino = 'multiplicacion'

def division():
	entrada = float(window.get())
	global valor, i, termino, z
	if i == 0:
		valor += entrada
	else:
		valor = valor * (1 / entrada)
	window.delete(0,END)
	i += 1
	z += 1
	termino = 'division'

def igual():
	global termino, valor, i, z
	if termino == '':
		valor = int(window.get())
		window.insert(0,valor)
	elif termino == 'suma':
		suma()
	elif termino == 'resta':
		resta()
	elif termino == 'multiplicacion':
		multiplicacion()
	elif termino == 'division':
		division()
	window.delete(0,END)
	tag = abs(valor) - abs(int(valor))
	if tag == 0.0:
		window.insert(0,round(valor))
	else:
		window.insert(0,round(valor,5))
	valor,i,z = 0,0,0

calc = Tk()
calc.title('Calculadora con Python')
calc.geometry('400x750')
calc.resizable(width=False, height=False)

title=Label(calc, text='Calculadora', font=('Script MT Bold',40))
title.pack(pady=10)

window=Entry(calc)
window.config(width=40, font=('led calculator',30), bg='black', fg='white' ,justify=RIGHT)
window.insert(0,0)
window.bind('<Button-1>',barrido)
window.bind('<Key>',block)
window.pack(padx=25, pady=10)
    
first = Frame(calc)
second = Frame(calc)
third = Frame(calc)
last = Frame(calc)
first.pack(pady=10)
second.pack(pady=10)
third.pack(pady=10)
last.pack(pady=10)

siete = Button(first, text='7',font=('Arial',40), height=1, width=2, command = lambda: funcion(7))
siete.pack(padx=10,pady=10, side=LEFT)

ocho = Button(first, text='8',font=('Arial',40), height=1, width=2, command = lambda: funcion(8))
ocho.pack(padx=10,pady=10, side=LEFT)

nueve = Button(first, text='9',font=('Arial',40), height=1, width=2, command = lambda: funcion(9))
nueve.pack(padx=10,pady=10, side=LEFT)

mas = Button(first, text='+',font=('Arial',40), height=1, width=2, command=suma)
mas.pack(padx=10,pady=10, side=LEFT)

cuatro = Button(second, text='4',font=('Arial',40), height=1, width=2, command = lambda: funcion(4))
cuatro.pack(padx=10,pady=10, side=LEFT)

cinco = Button(second, text='5',font=('Arial',40), height=1, width=2, command = lambda: funcion(5))
cinco.pack(padx=10,pady=10, side=LEFT)

seis = Button(second, text='6',font=('Arial',40), height=1, width=2, command = lambda: funcion(6))
seis.pack(padx=10,pady=10, side=LEFT)

menos = Button(second, text='-',font=('Arial',40), height=1, width=2,command=resta)
menos.pack(padx=10,pady=10, side=LEFT)

uno = Button(third, text='1',font=('Arial',40), height=1, width=2, command = lambda: funcion(1))
uno.pack(padx=10,pady=10, side=LEFT)

dos = Button(third, text='2',font=('Arial',40), height=1, width=2, command = lambda: funcion(2))
dos.pack(padx=10,pady=10, side=LEFT)

tres = Button(third, text='3',font=('Arial',40), height=1, width=2, command = lambda: funcion(3))
tres.pack(padx=10,pady=10, side=LEFT)

por = Button(third, text='×',font=('Arial',40), height=1, width=2,command=multiplicacion)
por.pack(padx=10,pady=10, side=LEFT)

clear = Button(last, text='C',font=('Arial',40), height=1, width=2,command=limpiar)
clear.pack(padx=10,pady=10, side=LEFT)

cero = Button(last, text='0',font=('Arial',40), height=1, width=2, command = lambda: funcion(0))
cero.pack(padx=10,pady=10, side=LEFT)

igual = Button(last, text='=',font=('Arial',40), height=1, width=2, command= igual)
igual.pack(padx=10,pady=10, side=LEFT)

entre = Button(last, text='÷',font=('Arial',40), height=1, width=2, command= division)
entre.pack(padx=10,pady=10, side=LEFT)

calc.mainloop()