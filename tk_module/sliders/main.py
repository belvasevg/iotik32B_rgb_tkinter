import tkinter as tk
import tkinter.ttk as ttk

import result_color as rs
import main_slider_frame as msf
from com_set import COM_setter

root = tk.Tk()
root.geometry("500x500")
mc = rs.MainColor(root)

mmsf = msf.Sliders_frame(root,3,mc.get_colors(),mc.set_color)

comSetter = COM_setter(root)

comSetter.frame.grid(row=0,column=0,columnspan=2)
mc.frame.grid(row=1,column=0)
mmsf.mainFrame.grid(row=1,column=1)
root.grid_anchor('center')

root.mainloop()