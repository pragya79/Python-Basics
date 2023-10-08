from tkinter import*
root=Tk()
root.geometry("500x500")
# labels in GUI
# text->adds Text
# bd->adds background
# fg->foreground
# font->sets the font
# relief->border styling SUNKEN,RAISED,GROOVE,RIDGE
text_label=Label(text="Hello Pragya",bg="purple",fg="white",padx=20,pady=20,font=("sans-serif",14,"bold"),borderwidth=3,relief=GROOVE)
#Packs in GUI
# anchor=nw 
# side=top,bottom,left,right
text_label.pack()

root.mainloop()