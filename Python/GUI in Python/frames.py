from tkinter import*
root=Tk()
root.geometry("500x250")
f1=Frame(root,bg="silver",borderwidth=2,relief=SUNKEN)
f1.pack(side="left",fill="y")

l=Label(f1,text="Pycharm",font="cursive 10 bold")
l.pack(pady=20)
f2=Frame(root,bg="black",borderwidth=4,relief=GROOVE)
f2.pack(fill=X)
l2=Label(f2,text="Project Tkinter")
l2.pack(fill=X)
root.mainloop()