from tkinter import *
import tkinter as tk

import guichall
import guichall_func

#tkinter frame
class PWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame. __init__(self, master, *args, **kwargs)

        #frame config
        self.master = master
        self.master.minsize(500,170) #height and width
        #second bar
        self.master.maxsize(500,170)
        #centers the app to user's screen
        guichall_func.center_window(self,500,300)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        #method built into tkinter to catch if user closes window
        self.master.protocol("WM_DELETE_WINDOW", lambda: guichall_func.ask_quit(self))
        arg = self.master

        #keep code clutter free
        guichall.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = PWindow(root)
    root.mainloop()
