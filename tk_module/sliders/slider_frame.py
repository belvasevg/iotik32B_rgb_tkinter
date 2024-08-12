import slider 
import tkinter as tk
import tkinter.ttk as ttk

class LocalFrame:
    """
    Класс для обработки локальной рамки слайдера
    """
    def __init__(self, master,color="white",total_color:int=None,tcf=None):
          self.frame = ttk.LabelFrame(master)
          self.frameSlider = slider.Slider(self.frame,color,total_color,tcf)