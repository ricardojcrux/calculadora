from tkinter import *

class View(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.config(bg="#151922")

        self.buttons = [[7,8,9,'+'],
                        [4,5,6,'-'],
                        [1,2,3,'∗'],
                        ['C',0,'=','÷']]
        
        self.window = Frame(self)
        self.window.pack(fill=X)

        self.number_windows = Label(self.window, font=('led calculator',35), width=10, anchor=E)
        self.number_windows.config(bg="#151922", fg= "white")
        self.number_windows.pack(padx=10, pady=10)

        self.array_buttons = Frame(self)
        self.array_buttons.pack()

        for i in range(4):
            for j in range(4):
                button = Button(self.array_buttons, bg = "#151922", height = 1, width = 3)
                button.config(text = f'{self.buttons[i][j]}', font = ('Arial',30), fg="white")
                button.config(relief = RIDGE, anchor= N)
                button.config(command = lambda x = self.buttons[i][j] : self.button_action(x))
                button.grid(row = i, column = j)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def button_action(self, argument):
        if self.controller:
            self.controller.button_action(argument)
            
            self.number_windows.config(text= self.controller.set_window_text())