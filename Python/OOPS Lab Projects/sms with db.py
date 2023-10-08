import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class StudentManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x800")

        self.name = tk.StringVar()
        self.dob = tk.StringVar()
        self.roll_no = tk.StringVar()
        self.branch = tk.StringVar()
        self.cgpa = tk.StringVar()
        self.email = tk.StringVar()
        self.contact = tk.StringVar()

        title = tk.Label(self.root, text="Student Management System", bd=9, relief="groove", font="cursive 20 bold", bg="black", fg="white")
        title.pack(side="top", fill=tk.X)

        f = tk.Frame(self.root, bd=5, relief=tk.SUNKEN, bg="wheat")
        f.place(y=50, width=505, height=700)

        l1 = tk.Label(f, text="Student Info", bg="black", fg="white", bd=4, relief="raised", font="sans-serif 20 bold")
        l1.pack()
        l1.grid(row=0, columnspan=2, pady=15)

        name = tk.Label(f, text="Name: ", bg="silver", fg="black", font="lucida 15 bold")
        name.grid(row=1, column=1, sticky="w")
        name_input = tk.Entry(f, textvariable=self.name, font="cursive 20")
        name_input.grid(row=1, column=2, padx=5, pady=7)

        dob = tk.Label(f, text="DOB: ", bg="silver", fg="black", font="lucida 15 bold")
        dob.grid(row=2, column=1, sticky="w")
        dob_input = tk.Entry(f, textvariable=self.dob, font="cursive 20")
        dob_input.grid(row=2, column=2, padx=5, pady=7)

        Roll_no = tk.Label(f, text="Roll No: ", bg="silver", fg="black", font="lucida 15 bold")
        Roll_no.grid(row=3, column=1, sticky="w")
        Roll_no_input = tk.Entry(f, textvariable=self.roll_no, font="cursive 20")
        Roll_no_input.grid(row=3, column=2, padx=5, pady=7)

        branch = tk.Label(f, text="Branch: ", bg="silver", fg="black", font="lucida 15 bold")
        branch.grid(row=4, column=1, sticky="w")
        branch_input = tk.Entry(f, font="cursive 20", textvariable=self.branch)
        branch_input.grid(row=4, column=2, padx=5, pady=7)

        contactno = tk.Label(f, text="Contact No: ", bg="silver", fg="black", font="lucida 15 bold")
        contactno.grid(row=5, column=1, sticky="w")
        contactno_input = tk.Entry(f, font="cursive 20", textvariable=self.contact)
        contactno_input.grid(row=5, column=2, padx=5, pady=7)

        email = tk.Label(f, text="Email Id: ", bg="silver", fg="black", font="lucida 15 bold")
        email.grid(row=6, column=1, sticky="w")
        email_input = tk.Entry(f, font="cursive 20", textvariable=self.email)
        email_input.grid(row=6, column=2, padx=5, pady=7)

        gender = tk.Label(f, text="Gender: ", bg="silver", fg="black", font="lucida 15 bold")
        gender.grid(row=7, column=1, sticky="w")
        gender_combobox = ttk.Combobox(f, font="cursive 20", state="readonly", values=("Male", "Female", "Others"))
        gender_combobox.grid(row=7, column=2, pady=5, padx=5)

        btn = tk.Frame(f, bd=3, bg="grey", relief="sunken")
        btn.place(x=20, y=500, width=340)
        addbtn = tk.Button(btn, text="Add", width=20, command=self.add)
        addbtn.grid(row=0, column=0, padx=6, pady=7)
        addbtn2 = tk.Button(btn, text="Search", width=20)
        addbtn2.grid(row=0, column=1, padx=10, pady=7)

        d = tk.Frame(self.root, bd=5, relief=tk.SUNKEN, bg="silver")
        d.place(x=505, y=50, width=1000, height=700)

        search = tk.Label(d, text="Search by", bg="black", fg="white", font="lucida 20", relief=tk.GROOVE, width=8)
        search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo = ttk.Combobox(d, font="lucida", state="readonly", values=("Name", "Roll no", "Branch", "CGPA", "Email Id"))
        combo.grid(row=0, column=1, padx=20, pady=10)

        search_input = tk.Entry(d, font="cursive 20", width=20)
        search_input.grid(row=0, column=2, padx=5, pady=7)

        addbtn4 = tk.Button(d, text="Search", width=10)
        addbtn4.grid(row=0, column=3, padx=2, pady=10)

        t = tk.Frame(d, bd=5, relief=tk.SUNKEN, bg="aliceblue")
        t.place(y=50, width=850, height=630)
        scrollx = ttk.Scrollbar(t, orient=tk.HORIZONTAL)
        scrolly = ttk.Scrollbar(t, orient=tk.VERTICAL)

        self.table = ttk.Treeview(t, column=("name", "dob", "roll", "branch", "cgpa", "email", "contact"),
                                  xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)

        self.table.heading("name", text="Name")
        self.table.heading("dob", text="DOB")
        self.table.heading("roll", text="Roll No")
        self.table.heading("branch", text="Branch")
        self.table.heading("cgpa", text="CGPA")
        self.table.heading("email", text="Email Id")
        self.table.heading("contact", text="Contact No")

        self.table['show'] = 'headings'
        self.table.column("name", width=100)
        self.table.column("dob", width=100)
        self.table.column("roll", width=100)
        self.table.column("branch", width=100)
        self.table.column("cgpa", width=100)
        self.table.column("email", width=100)
        self.table.column("contact", width=100)

        self.table.pack(fill=tk.BOTH, expand=1)
        self.fetch()

    def add(self):
        if self.roll_no.get() == "" or self.name.get() == "":
            messagebox.showerror("Error", "All fields are required to be filled!")
        else:
            con = sqlite3.connect('StudentManagement.db')
            cur = con.cursor()

            cur.execute("insert into student values(?,?,?,?,?,?,?)",
                        (self.name.get(), self.dob.get(), self.roll_no.get(), self.branch.get(),
                         self.cgpa.get(), self.email.get(), self.contact.get()))
            con.commit()
            self.fetch()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted!")

    def fetch(self):
        con = sqlite3.connect('StudentManagement.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS student (
                        name TEXT,
                        dob TEXT,
                        roll_no TEXT PRIMARY KEY,
                        branch TEXT,
                        cgpa TEXT,
                        email TEXT,
                        contact TEXT
                    )''')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert('', tk.END, values=row)
            con.commit()
        con.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagement(root)
    root.mainloop()
