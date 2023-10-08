from tkinter import*
root=Tk()#includes all the gui logic 
#gui logic here
root.geometry("1000x500")#widthxheight
root.minsize(200,200)#width,height
root.maxsize(800,800)
root.title("GUI in Python")
first_root=Label(text="Welcome to GUI")
first_root.pack()#without this above text will not be shown on screen
#Inserting images using Label#tkinter does'nt support jpg/jpeg format
photo=PhotoImage(file="uiet.png")
img_label=Label(image=photo)
img_label.pack()
# #for jpg images
# image=Image.open()
# photo=ImageTk.PhotoImage(image)
bg_label=Label(text="UIET Chandigarh",fg="white",bg="black")
bg_label.pack()









root.mainloop()

