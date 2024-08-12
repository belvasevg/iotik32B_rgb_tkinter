import tkinter as tk
import tkinter.ttk as ttk

class Slider:
    """
    Класс слайдера для управления значением цвета
    """
    def __init__(self,master,actColor,total_color:int=None,tcf=None):
        self.master = master
        self.total_label_color = total_color
        self.total_label_func = tcf

        self.colorForLabel = actColor
        self.current_value = tk.IntVar()
        self.colorLabel = ttk.Label(master, width=10)
        self.myscale = ttk.Scale(master=master,from_=255,to=0,command=self.slider_changed,variable=self.current_value,orient="vertical",value=0)
        self.mylabel = ttk.Label(master=master)

        self.colorLabel.grid(row=0,column=0)
        self.myscale.grid(row=1,column=0)
        self.mylabel.grid(row=2,column=0)

    def slider_changed(self,event):
            var = self.get_current_value()
            self.total_label_func(self.total_label_color,var)
            self.total_color = var
            self.mylabel['text'] = str(var)
            if (var) > 0:
                self.colorLabel["background"] = self.colorForLabel
            else:
                self.colorLabel["background"] = ""
            

    def get_current_value(self):
            return self.current_value.get()
    
    # def change_slider_color(self,event):
    #       pass
    # def slider_color(self):
    #       if (self.get_current_value()) > 0:
    #             return self.colorForLabel
    #       else:
    #             return "white"