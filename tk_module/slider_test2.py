import tkinter as tk
import tkinter.ttk as ttk

class Slider:

    def __init__(self,master):
        self.current_value = tk.IntVar()
        self.myscale = ttk.Scale(master=master,from_=0,to=255,command=self.slider_changed,variable=self.current_value,orient="vertical")
        self.myscale.grid(row=0,column=0)
        self.mylabel = ttk.Label(master=master)
        self.mylabel.grid(row=1,column=0)
    def slider_changed(self,event):
            self.mylabel['text'] = self.get_current_value()
    def get_current_value(self):
            return str(self.current_value.get())


class LocalFrame:
    def __init__(self, master):
          self.frame = ttk.LabelFrame(master)
          self.frameSlider = Slider(self.frame)
          #self.frame.grid(row=0,column=position)
        #   self.frameSlider.myscale.grid(row=0,column=0)
        #   self.frameSlider.mylabel.grid(row=1,column=0)


class MainFrame():
      def __init__(self,master,valueOfSliders):
            self.mainFrame = ttk.LabelFrame(master,text="RGB Control")
            # for lf in valueOfSliders:
            #       self.frameSlidersList.append(LocalFrame(self.mainFrame))
            self.frameSlidersList = [LocalFrame(self.mainFrame) for lf in range(valueOfSliders)]
            if __name__=="__main__":  
                self.mainFrame.pack(anchor="center")
            for fs in range(len(self.frameSlidersList)):
                  self.frameSlidersList[fs].frame.grid(row=0,column=fs)

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("500x500")

    mf = MainFrame(root,3)
    # frame1 = LocalFrame(root)
    # frame2 = LocalFrame(root)
    # frame3 = LocalFrame(root)

    root.mainloop()


            