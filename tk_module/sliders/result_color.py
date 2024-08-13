import tkinter as tk
import tkinter.ttk as ttk

class MainColor:
    "класс для вывода значения и самого цвета, получаемого со слайдеров"
    def __init__(self,master) -> None:

        self.RV,self.GV,self.BV = 0,0,0
        
        self.colors = ['#','00','00','00']

        self.frame = ttk.LabelFrame(master,text="Total color")

        self.color_name_code = ttk.Label(self.frame,text="Color code: ")

        self.color_code_label = ttk.Label(self.frame,text='#000000',width=20)

        self.total_color_label = ttk.Label(self.frame,background='#000000',width=20)
        if __name__=='__main__':
            self.frame.pack(anchor='center')
        self.color_name_code.grid(row=0,column=0)
        self.color_code_label.grid(row=0,column=1)
        self.total_color_label.grid(row=4,column=0,columnspan=2)
    
    def set_color(self,color,value):
        match color:
            case 'r':
                self.RV=value
            case 'g':
                self.GV=value
            case 'b':
                self.BV=value
        self.colors = ['#','%02x'%(self.RV),'%02x'%(self.GV),'%02x'%(self.BV)]
        self.color_code_label['text'] = ''.join(self.colors).upper()
        self.total_color_label["background"] = ''.join(self.colors)
    
    def get_colors(self):
        return ('r','g','b')
    

if __name__=="__main__":
    root = tk.Tk()
    mc = MainColor(root)
    root.mainloop()