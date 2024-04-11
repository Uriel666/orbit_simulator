import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *




class App():
    def __init__(self) -> None:
        self.window = ttk.Window()
        self.optionFrame = tk.Frame(master=self.window)
    
    def SetWidgets(self):
        pass
    

    def ActionButton(self):
        pass

    def StartApp(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.StartApp()