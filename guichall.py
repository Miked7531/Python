from tkinter import *
import tkinter as tk

import guichallmain
import guichall_func

def load_gui(self):
    
    self.lbl_fname = tk.Label(self.master,text='')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(50,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.sourcedirectory = StringVar()
    self.destinationdirectory = StringVar()

    self.txt_fname = tk.Entry(self.master,textvariable=self.sourcedirectory)
    self.txt_fname.grid(row=0,column=1,columnspan=5,padx=(30,50),pady=(50,0),sticky=W+E)
    self.txt_lname = tk.Entry(self.master,textvariable=self.destinationdirectory)
    self.txt_lname.grid(row=1,column=1,columnspan=5,padx=(30,50),pady=(10,0),sticky=W+E)
    

    #buttons
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: guichall_func.chooseSource(self))
    self.btn_browse1.grid(row=0,column=0,padx=(25,0),pady=(50,10),sticky=W)

    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: guichall_func.chooseDestination(self))
    self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(1,10),sticky=W)

    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: guichall_func.checkfiles(self))
    self.btn_check.grid(row=2,column=0,padx=(25,0),pady=(10,10),sticky=W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: guichall_func.ask_quit(self))
    self.btn_close.grid(row=2,column=5,padx=(50,0),pady=(10,10),sticky=E)

    self.master.columnconfigure(1,weight=3)
