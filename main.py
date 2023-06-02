from tkinter import *

class calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora con Python')
        self.geometry('400x700')
        self.resizable(width=False,height=False)

        self.cantidad = 0
        self.empty_window = True
        self.first = True
        self.buttons = [7,8,9,'+',4,5,6,'-',1,2,3,'∗','C',0,'=','÷']
        self.last_operation = ''

        self.title = Label(self, text='Calculadora',font=('Script MT Bold',40))
        self.title.pack(pady=10)

        self.window = Entry(self,width=40,font=('led calculator',30),bg='black',fg='white',justify=RIGHT)
        self.window.pack(padx=25,pady=10)
        self.window.insert(0,0)
        self.window.bind('<Key>', lambda widget: 'break')

        self.botones = Frame(self)
        self.botones.pack(pady=10)

        for i in range(4):
            for j in range(4):
                x = self.buttons[i*4+j]
                boton = Button(self.botones, text=f'{x}', font=('Arial',40),height=1,width=2, command= lambda x=x: self.accion_boton(x))
                boton.grid(padx=10,pady=10,row=i,column=j)
    
    def final_number(self, number:float):
        if abs(number) - abs(int(number)) == 0.0:
            return round(number)
        else:
            return round(number,4)

    def switch(self, cantidad, argument):
        self.window.delete(0,END)
        self.window.insert(0,cantidad)
        self.empty_window = True
        self.last_operation = argument

    def accion_boton(self, argument):
        number = list(range(0,10))
        if argument in number:
            if self.empty_window is True:
                self.window.delete(0,END)
                self.window.insert(0,argument)
            else:
                self.window.insert(END,argument)
            self.empty_window = False
            return
        valor = self.final_number(float(self.window.get()))
        if argument == '+':
            if self.first is True:
                self.cantidad = valor
                self.first = False
            else:
                self.cantidad += valor
            self.switch(self.cantidad, argument)
            
        elif argument == '-':
            if self.first is True:
                self.cantidad = valor
                self.first = False
            else:
                self.cantidad -= valor
            self.switch(self.cantidad, argument)    
        elif argument == '∗':
            if self.first is True:
                self.cantidad = valor
                self.first = False
            else:
                self.cantidad *= valor
            self.switch(self.cantidad, argument)
        elif argument == '÷':
            if self.first is True:
                self.cantidad = valor
                self.first = False
            else:
                self.cantidad *= 1/valor
                self.cantidad = self.final_number(self.cantidad)
            self.switch(self.cantidad, argument)
        elif argument == 'C':
            self.cantidad = 0
            self.first = True
            self.switch(self.cantidad, argument)
        elif argument == '=':
            self.accion_boton(self.last_operation)
            self.first = True

calc = calculator()
calc.mainloop()