import tkinter as tk
import tkinter.ttk as ttk

class COM_setter:
    def __init__(self,master):
        self.frame = ttk.LabelFrame(master,text='Выбор COM-порта')
        self.com_list=["COM"]*21
        for numcom in range(len(self.com_list)):
            self.com_list[numcom]+=str(numcom)
        self.com_list[0] = "Выберите COM-port"
        self.com_var = tk.StringVar(value=self.com_list[0])
        if __name__=='__main__':
            self.testLabel = ttk.Label(self.frame,textvariable=self.com_var)
        else:
            self.label_COM_name = ttk.Label(self.frame,text="Порт: ")
            self.label_COM_state = ttk.Label(self.frame,textvariable=self.com_var)
        self.com_set_Cb = ttk.Combobox(self.frame,textvariable=self.com_var,values=self.com_list)

        if __name__=='__main__':
            self.frame.pack(anchor='center')
            self.testLabel.grid(row=0,column=0)
            self.com_set_Cb.grid(row=1,column=0)
        else:
            self.frame.grid_anchor('center')
            self.label_COM_name.grid(row=0,column=0)
            self.label_COM_state.grid(row=0,column=1)
            self.com_set_Cb.grid(row=1,column=0,columnspan=2)
        
    
    
if __name__=='__main__':
    root = tk.Tk()
    root.geometry('500x500')

    cs = COM_setter(root)

    root.mainloop()