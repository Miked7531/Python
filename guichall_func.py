import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import guichallmain
import guichall
import time
import shutil
from tkinter import messagebox

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #closes app
        self.master.destroy()
        os._exit(0)


def chooseSource(self):
    sourceFolder =  filedialog.askdirectory()
    self.sourcedirectory.set(sourceFolder)
    

def chooseDestination(self):
    sourceFolder =  filedialog.askdirectory()
    self.destinationdirectory.set(sourceFolder)

def checkfiles(self):
    src = self.sourcedirectory.get()
    dst = self.destinationdirectory.get()
    now = time.time()
    SECONDS_IN_DAY = 24 * 60 * 60
    before = now - SECONDS_IN_DAY
    for fname in os.listdir(src):
        src_fname = os.path.join(src, fname)
        last_mod_time = os.path.getmtime(src_fname)
        if last_mod_time > before:
            dst_fname = os.path.join(dst, fname)
            shutil.move(src_fname, dst_fname)

