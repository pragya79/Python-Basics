import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3

# Create a universal font variable
labelfont = ('Helvetica', 14)

# Create a connection to the database
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()

# Create the database table if it doesn't exist
connector.execute(
    "CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
    "NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT, YEAR TEXT, CGPA REAL, ROLL_NO TEXT)"
)

# Create the functions
def reset_fields():
    for var in [name_strvar, email_strvar, contact_strvar, gender_strvar, dob_strvar, stream_strvar, year_strvar, cgpa_strvar, roll_no_strvar]:
        var.set('')

def reset_form():
    tree.delete(*tree.get_children())
    reset_fields()

def display_records():
    tree.delete(*tree.get_children())
    curr = connector.execute('SELECT * FROM SCHOOL_MANAGEMENT')
    data = curr.fetchall()
    for records in data:
        tree.insert('', END, values=records)

def add_record():
    name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    dob = dob_strvar.get()
    stream = stream_strvar.get()
    year = year_strvar.get()
    cgpa = cgpa_strvar.get()
    # roll_no = roll_no_strvar.get()

    if not name or not email or not contact or not gender or not dob or not stream or not year or not cgpa or not roll_no:
        mb.showerror('Error!', 'Please fill in all the fields.')
    else:
        try:
            connector.execute(
                'INSERT INTO SCHOOL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM, YEAR, CGPA) '
                'VALUES (?,?,?,?,?,?,?,?,?)', (name, email, contact, gender, dob, stream, year, cgpa)
            )
            connector.commit()
            mb.showinfo('Record added', f'Record of {name} was successfully added')
            reset_fields()
            display_records()
        except:
            mb.showerror('Wrong type', 'The type of the values entered is not accurate. Please check your input.')

def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values['values']
        tree.delete(current_item)
        connector.execute('DELETE FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
        connector.commit()
        mb.showinfo('Done', 'The record was successfully deleted.')
        display_records()

def view_record():
    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values['values']
    dob = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
    name_strvar.set(selection[1])
    email_strvar.set(selection[2])
    contact_strvar.set(selection[3])
    gender_strvar.set(selection[4])
    dob_strvar.set_date(dob)
    stream_strvar.set(selection[6])
    year_strvar.set(selection[7])
    cgpa_strvar.set(selection[8])
    roll_no_strvar.set(selection[9])

# Initializing the GUI window
main = Tk()
main.title('Student Management System')
main.geometry('1200x600')
main.resizable(0, 0)

# Create background colors
lf_bg = 'aliceblue'  # bg color for the left_frame
cf_bg = 'aqua'  # bg color for the center_frame

# Create StringVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
dob_strvar = StringVar()
stream_strvar = StringVar()
year_strvar = StringVar()
cgpa_strvar = StringVar()
roll_no_strvar = StringVar()

# Create the main frame
main_frame = Frame(main, bg='white')
main_frame.place(x=0, y=0, relheight=1, relwidth=1)

# Create the left frame
left_frame = Frame(main_frame, bg=lf_bg)
left_frame.place(x=10, y=10, relheight=0.9, relwidth=0.25)

# Create the center frame
center_frame = Frame(main_frame, bg=cf_bg)
center_frame.place(x=250, y=10, relheight=0.9, relwidth=0.2)

# Create the right frame
right_frame = Frame(main_frame, bg='gray')
right_frame.place(x=490, y=10, relheight=0.9, relwidth=0.5)

# Create labels and entry widgets in the left frame
labels = ["Name", "Contact Number", "Email Address", "Gender", "Date of Birth (DOB)", "Stream", "Year", "CGPA", "Roll No"]
entries = [name_strvar, contact_strvar, email_strvar, gender_strvar, dob_strvar, stream_strvar, year_strvar, cgpa_strvar, roll_no_strvar]

for i, label in enumerate(labels):
    Label(left_frame, text=label, font=labelfont, bg=lf_bg).place(relx=0.15, rely=0.1 + i * 0.1)
    Entry(left_frame, width=20, textvariable=entries[i], font=labelfont).place(relx=0.3, rely=0.1 + i * 0.1)

# Create DateEntry widget for DOB
DateEntry(left_frame, width=19, textvariable=dob_strvar, font=labelfont).place(relx=0.3, rely=0.5)

# Create the 'Submit and Add Record' button
Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.15, rely=0.9)

# Create buttons in the center frame
buttons = ["Delete Record", "View Record", "Reset Fields", "Delete Database"]
commands = [remove_record, view_record, reset_fields, reset_form]

for i, button_text in enumerate(buttons):
    Button(center_frame, text=button_text, font=labelfont, command=commands[i], width=15).place(relx=0.1, rely=0.2 + i * 0.1)

# Create Treeview widget in the right frame
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=('Student ID', "Name", "Email Address", "Contact Number", "Gender", "Date of Birth", "Stream", "Year", "CGPA", "Roll No"))

# Create horizontal and vertical scrollbars for the Treeview
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

# Configure columns for Treeview
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)
tree.heading('Year', text='Year', anchor=CENTER)
tree.heading('CGPA', text='CGPA', anchor=CENTER)
tree.heading('Roll No', text='Roll No', anchor=CENTER)

# Set column widths for Treeview
for col in ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9']:
    tree.column(col, width=100, stretch=NO)

# Place Treeview widget
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

# Display records in the Treeview
display_records()

# Start the main loop
main.mainloop()
