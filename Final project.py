#importing tkinter to use GUI
from collections import Counter
from logging import root
from re import sub
from sre_parse import State
from tkinter import *
import sqlite3

root =Tk()
root.geometry("400x400")
#Database

# Create or connect a database
conn = sqlite3.connect("address_book.db")

# Creating a cursor
Cursor_obj= conn.cursor()

#Create table

# table = """ CREATE TABLE addresses (
#         First_name text,
#         Last_name text
#         Address text,
#         City text,
#         State text,
#         Zipcode integer
#     ); """

# Cursor_obj.execute(table)

# Create Submit function
def submit():
    # Create or connect a database
    conn = sqlite3.connect("address_book.db")
    # Creating a cursor
    Cursor_obj= conn.cursor()
    
    #insert into the sqLITE TABLE
    Cursor_obj.execute("INSERT INTO addresses VALUES(:f_name, :L_name, :Address, :City, :State, :Zipcode)",
                       {
                           'f_name': F_name.get(),
                           'L_name': L_name.get(), 
                            'Address': Adress_name.get(),
                           'City': City.get(), 
                            'State': State.get(),
                           'Zipcode': Zipcode.get(),                           
                       })
    
    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()
    
    
    
    
    
    #Clearing the Text boxes upon clicking submit
    F_name.delete(0,END)
    L_name.delete(0,END)
    Adress_name.delete(0,END)
    City.delete(0,END)
    State.delete(0,END)
    Zipcode.delete(0,END)
    
#Creating Text boxes
F_name= Entry(root, width=30)
F_name.grid(row=0, column= 1, padx=20)

L_name= Entry(root, width=30)
L_name.grid(row=1, column= 1)

Adress_name= Entry(root, width=30)
Adress_name.grid(row=2, column= 1)

City= Entry(root, width=30)
City.grid(row=3, column= 1)

State= Entry(root, width=30)
State.grid(row=4, column= 1)

Zipcode= Entry(root, width=30)
Zipcode.grid(row=5, column= 1)

#Creating text box label
F_name_label= Label(root, text="First Name")
F_name.grid(row=0, column=0)

L_name_label= Label(root, text="First Name")
L_name.grid(row=1, column=0)

Address_name_label= Label(root, text="First Name")
Adress_name.grid(row=2, column=0)

City_label= Label(root, text="First Name")
City.grid(row=3, column=0)

State_label= Label(root, text="First Name")
State.grid(row=4, column=0)

Zipcode_label= Label(root, text="First Name")
Zipcode.grid(row=5, column=0)

#Creating a Submit Botton
# submit_btn =  Button (root, text="Add record to Database", command=submit )
# submit_btn.grid(row = 0, column = 3, padx = 100)
submit_btn = Button(root,
                       text = "Add record to Database").place(x = 40,
                                              y = 130)

#Commit Changes
conn.commit()

#Close Connection
conn.close()


root.mainloop()