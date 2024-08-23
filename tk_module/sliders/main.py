import tkinter as tk
import tkinter.ttk as ttk

import result_color as rs
import main_slider_frame as msf
from com_set import COM_setter
from serial_state import SerialState

root = tk.Tk()
root.geometry("800x800")
canvas = tk.Canvas(root,bg='#FFFF00')
canvas.pack(fill=tk.BOTH, expand=True)
#root.configure(background='#FFFF00')
#color = root.configure(background='#FFFFFF')
#print(color)
#print(color['bg'])


ttk.Style().configure("TLabel", 
                      font="Times", 
                      foreground="#FFFFFF", 
                      padding=8, 
                      background="#8420e8") 
mc = rs.MainColor(canvas)

mmsf = msf.Sliders_frame(canvas,3,mc.get_colors(),mc.set_color)
mmsf = msf.Sliders_frame(canvas,3,mc.get_colors(),mc.set_color)
#mmsf = msf.Sliders_frame(root,3,mc.get_colors(),mc.set_color)

comChoise = COM_setter(canvas)
comSetter = SerialState(canvas,comChoise.get_com_var)

comChoise.frame.grid(row=0,column=0)
comSetter.frame.grid(row=0,column=1)

mc.frame.grid(row=1,column=0)
mmsf.mainFrame.grid(row=1,column=1)
canvas.grid_anchor('center')

root.mainloop()
