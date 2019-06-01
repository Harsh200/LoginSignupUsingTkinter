from tkinter import *
import os
credits='tempfile.temp'
def signup():
    global pwordE
    global nameE
    global roots

    roots=Tk()
    roots.title=("Signup")
    instruction=Label(roots,text="Please enter new Credentials\n")
    instruction.grid(row=0,column=0,sticky=E)

    namel=Label(roots,text="New Username")
    pwordl=Label(roots,text="New Password")
    namel.grid(row=1,column=1,sticky=w)
    pwordl.grid(row=2,column=0,sticky=w)

    nameE=Entry(roots)
    pwordE=Entry(roots,show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    signupButton=Button(roots,text="Signup",command=FSSignup)
    signupButton.grid(columnspan=2,sticky=w)
    root.mainloop()

def FSSignup():
    with open(credits,'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()
    roots.destroy()
    Login()

def Login():
    global nameEl
    global pwordEl
    global rootA

    rootA = Tk()
    rootA.title = ("Login")

    instruction = Label(rootA, text="Please Login\n")
    instruction.grid(sticky=E)

    namel = Label(rootA, text="Username")
    pwordl = Label(rootA, text="Password")
    namel.grid(row=1, column=1, sticky=w)
    pwordl.grid(row=2, column=0, sticky=w)

    nameEl = Entry(rootA)
    pwordEl = Entry(rootA, show='*')
    nameEl.grid(row=1, column=1)
    pwordEl.grid(row=2, column=1)


    LoginButton=Button(rootA,text="Signup",command=FSSignup)
    LoginButton.grid(columnspan=2,sticky=w)
    rmuser=Button(rootA,text="Delete User",fg="Red",command=DeleteUser)
    rmuser.grid(columnspan=2,sticky=w)

    rootA.mainloop()

def CheckLogin():
    with open(credits) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        pword=data[1].rstrip()

    if nameEl.get()==uname and pwordEl.get()==pword:
        r=Tk()
        r.title('tD')
        r.geometry('150x150')
        rlbl=Label(r,text='\n[+] Logged IN')
        rlbl.pack()
        r.mainloop()
    else:
        r=Tk()
        r.title('tD')
        r.geometry('150x150')
        rlbl=Label(r,text='\n[!] Invalid Login ')
        rlbl.pack()
        r.mainloop()

def DelUser():
    os.remove(credits)
    rootA.destroy()