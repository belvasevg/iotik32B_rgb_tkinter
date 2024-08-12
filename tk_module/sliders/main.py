import tkinter as tk
import tkinter.ttk as ttk

import result_color as rs
import main_slider_frame as msf

root = tk.Tk()
root.geometry("500x500")
mc = rs.MainColor(root)

mmsf = msf.Sliders_frame(root,3,mc.get_colors(),mc.set_color)

mc.frame.grid(row=0,column=0)
mmsf.mainFrame.grid(row=0,column=1)
root.grid_anchor('center')

root.mainloop()