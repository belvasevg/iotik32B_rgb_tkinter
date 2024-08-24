import slider_frame
import tkinter as tk
import tkinter.ttk as ttk

class Sliders_frame:
      
      frames_names = ['R','G','B']
      colors = ['red','green','blue']
      
      def __init__(self,master,
                   valueOfSliders,
                   total_color:tuple = None,
                   tcf = None,
                   serial_set:function = None):
            self.mainFrame = ttk.LabelFrame(master,text="RGB Control")
            self.serial_func = serial_set
            # for lf in valueOfSliders:
            #       self.frameSlidersList.append(LocalFrame(self.mainFrame))
            if __name__=="__main__":
                self.frameSlidersList = [slider_frame.LocalFrame(self.mainFrame,
                                                             self.colors[lf]) 
                                     for lf in range(valueOfSliders)]
                self.mainFrame.pack(anchor="center")
                for fs in range(len(self.frameSlidersList)):
                    self.frameSlidersList[fs].frame['text'] = self.frames_names[fs]
                    self.frameSlidersList[fs].frame.grid(row=0,column=fs)
            
            if __name__!="__main__":
                self.frameSlidersList = [slider_frame.LocalFrame(self.mainFrame,
                                                             self.colors[lf],
                                                             total_color[lf],
                                                             tcf) 
                                     for lf in range(valueOfSliders)]
                #добавить добавление значения rgb в список
                for fs in range(len(self.frameSlidersList)):
                    self.frameSlidersList[fs].frame['text'] = self.frames_names[fs]
                
                #обозначение имён рамок слайдеров, из которых можно получить значение целевого цвета
                #при передаче массива по Serial

                for fs in range(len(self.frameSlidersList)):
                    self.frameSlidersList[fs].frame.grid(row=0,column=fs)

            
            
                 

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("500x500")
    mf = Sliders_frame(root,3)
    root.mainloop()