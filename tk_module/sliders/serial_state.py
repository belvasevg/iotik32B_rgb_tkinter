import tkinter as tk
import tkinter.ttk as ttk

class SerialState:

    def __init__(self,master,com_setter):

        self.frame = ttk.LabelFrame(master, text= "Состояние порта")
        self.com_setter_state = com_setter
        self.current_value = tk.BooleanVar()
        self.label_state = ttk.Label(master=self.frame,width=20)

        self.set_serial_button = ttk.Checkbutton(master=self.frame,
                                            variable=self.current_value,
                                            command=self.check_serial)
        
        self.label_state.grid(row=0,column=0)
        self.set_serial_button.grid(row=0,column=1)

    def check_serial(self):
        var = self.get_check_value()
        state_com = self.com_setter_state()
        if state_com != "Выберите COM-port":
            if var:
                self.label_state['text'] = "Включен"
                self.label_state['background'] = 'green'
            if not(var):
                self.label_state['text'] = "Выключен"
                self.label_state['background'] = 'red'
        else:
            self.label_state['text'] = ""
            self.label_state['background'] = ''

    def get_check_value(self):
        return self.current_value.get()