from tkinter import *
import os
credits='tempfile.temp'
def signup():
    global pwordE
    global nameE
    global roots

    roots=Tk()
    roots.title={"Signup"}
    instruction=Label(roots,text="Please enter new Credentials\n")
    instruction.grid(row=0,column=0,sticky=E)

    namel=Label(roots,text="New Username")