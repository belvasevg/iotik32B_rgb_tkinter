import slider_frame
import tkinter as tk
import tkinter.ttk as ttk

class Sliders_main_frame:
      
      frames_names = ['R','G','B']
      colors = ['red','green','blue']
      def __init__(self,master,valueOfSliders):
            self.mainFrame = ttk.LabelFrame(master,text="RGB Control")
            
            # for lf in valueOfSliders:
            #       self.frameSlidersList.append(LocalFrame(self.mainFrame))
            self.frameSlidersList = [slider_frame.LocalFrame(self.mainFrame,self.colors[lf]) for lf in range(valueOfSliders)]
            if __name__=="__main__":  
                self.mainFrame.pack(anchor="center")
            for fs in range(len(self.frameSlidersList)):
                  self.frameSlidersList[fs].frame['text'] = self.frames_names[fs]
                  self.frameSlidersList[fs].frame.grid(row=0,column=fs)

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("500x500")
    mf = Sliders_main_frame(root,3)
    root.mainloop()