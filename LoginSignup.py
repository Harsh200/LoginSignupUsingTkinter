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
    pwordl=Label(roots,text="New Password")
    namel.grid(row=1,column=1,sticky=w)
    pwordl.grid(row=2,column=0,sticky=w)

    nameE=Entry(roots)
