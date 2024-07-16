from mvc import controller, model, view
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculadora con Python')
        self.resizable(width=False,height=False)

        app_model = model.Model()

        app_view = view.View(self)
        app_view.grid(row = 0, column = 0)

        app_controller = controller.Controller(app_model, app_view)

        app_view.set_controller(app_controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()