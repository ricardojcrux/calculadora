class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.first_operation = True # When I start to use calculator, it turn to False. 
        self.new_operation = True
        self.number_active = False
        self.active_operation = ''
        self.window_text = ''
        self.sumatory = 0
        self.number = 0

    def button_action(self, argument):
        if argument in list(range(0,10)):
            if not self.number_active:
                self.window_text = ''

            if len(self.window_text) < 10:
                self.number_active = True
                self.window_text += str(argument)
            
        elif argument in ['+','-','∗','÷']:
            if self.number_active:
                self.number_active = False
                self.number = int(self.window_text)

            if self.first_operation or self.new_operation:
                self.sumatory = self.number
            else:
                if self.active_operation != argument:
                    self.active_operation = argument
                elif argument == '+':
                    self.sumatory += self.number
                elif argument == '-':
                    self.sumatory -= self.number
                elif argument == '∗':
                    self.sumatory *= self.number
                else:
                    if self.number != 0:
                        self.sumatory *= 1/self.number
                    else:
                        self.sumatory = 0
            
            self.active_operation = argument
            self.window_text = self.rounded_number(str(self.sumatory))
            self.new_operation = False
            self.first_operation = False
        
        elif argument == '=':
            if not self.new_operation:
                self.button_action(self.active_operation)
            self.active_operation = ''
            self.new_operation = True
            self.number_active = False
            self.number = self.sumatory

        elif argument == 'C':
            self.number_active = False
            self.active_operation = ''
            self.new_operation = True
            self.sumatory = 0
            self.window_text = ''
            self.number = 0
                
    def rounded_number(self, number: str):
        if len(number) > 9:
            new_number = "{:.4e}".format(float(number))
            if str(new_number)[-2:] == '00':
                return number
            elif len(str(new_number)) > 9:
                return "{:.3e}".format(float(number))
            return new_number

        if '.' in number:
            int_number, decimal = number.split('.')
            if decimal == '0':
                return int_number
            else:
                return number
        else:
            return number

    def set_window_text(self):
        return self.window_text