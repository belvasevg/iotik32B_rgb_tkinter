import slider 
import tkinter as tk
import tkinter.ttk as ttk

class LocalFrame:
    def __init__(self, master,color="white"):
          self.frame = ttk.LabelFrame(master)
          self.frameSlider = slider.Slider(self.frame,color)