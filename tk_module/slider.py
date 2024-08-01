import tkinter as tk
import tkinter.ttk as ttk

flag_test_slider = True
flag_run_slider = False
class Slider:
    global flag_test,flag_run_slider
    def __init__(self, master) -> None:
        
        if flag_test_slider:
            self.current_value = tk.IntVar()
            self.myscale = ttk.Scale(master=master,from_=0,to=255,command=self.slider_changed,variable=self.current_value)
            self.myscale.grid(row=0,column=0)
            self.mylabel = ttk.Label(master=master)
            self.mylabel.grid(row=1,column=0)

    if flag_test_slider:
        def slider_changed(self,event):
            self.mylabel['text'] = self.get_current_value()
        def get_current_value(self):
            return str(self.current_value.get())

if __name__=="__main__":
    if flag_test_slider:
        root = tk.Tk()
        testSW = Slider(root)
        root.mainloop()
    if flag_run_slider:
        pass