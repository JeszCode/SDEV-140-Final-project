# This program is a GUI database where the user can input data and add the data into the database, Search for input data and delete data by input the number of the data into the Delete ID box.

#importing tkinter to use GUI
from ast import Delete
from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x400")
#Database

# Create or connect a database
conn = sqlite3.connect("address_book.db")

# Creating a cursor
Cursor_obj= conn.cursor()

#Create table

# table = """ CREATE TABLE addresses (
#         First_name text,
#         Last_name text,
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
    Cursor_obj.execute("INSERT INTO addresses VALUES(:F_name, :L_name, :Address_name, :City, :State, :Zipcode)",
                       {
                           'F_name': F_name.get(),
                           'L_name': L_name.get(), 
                           'Address_name': Adress_name.get(),
                           'City': City.get(), 
                           'State': State.get(),
                           'Zipcode': Zipcode.get()                          
                       }
                    )
    
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

#assemble a search function   
def query():
    # Create or connect a database
    conn = sqlite3.connect("address_book.db")
    # Creating a cursor
    Cursor_obj= conn.cursor()

    #searching the database, OID (object identifier)
    
    Cursor_obj.execute("select *, oid FROM addresses")
    records= Cursor_obj.fetchall()
   
   

    # LOOPING THROUGH RESULTS 
    print_records = ''
    for record in records:
        print_records +="\n" + str(record[6]) + " .  " +  str(record[0]) + '  ,  ' + str(record[1]) + '  ,  ' + str(record[2]) + '  ,  ' + str(record[3]) + '  ,  ' + str(record[4]) + '    ' + "\n" 

    query_label= Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan= 2)

    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

# Fuction to delete record from database
def delete():
      # Create or connect a database
    conn = sqlite3.connect("address_book.db")
    # Creating a cursor
    Cursor_obj= conn.cursor()

    # Delete a record
    Cursor_obj.execute("delete  From addresses WHERE oid = " + Delete_containers.get())
    Delete_containers.delete(0, END)

    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

    
    
#Creating Text boxes
F_name= Entry(root, width=30)
F_name.grid(row=0, column= 1, padx=20, pady=(10,0))

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

Delete_containers= Entry(root, width= 30)
Delete_containers.grid(row=8, column= 1, padx=5, pady=(5,0))

#Creating text box label
F_name_label= Label(root, text="First Name") 
F_name_label.grid(row=0, column=0, pady=(10,0))

L_name_label= Label(root, text="Last Name")
L_name_label.grid(row=1, column=0)

Address_name_label= Label(root, text="Address")
Address_name_label.grid(row=2, column=0)

City_label= Label(root, text="City")
City_label.grid(row=3, column=0)

State_label= Label(root, text="State")
State_label.grid(row=4, column=0)

Zipcode_label= Label(root, text="Zipcode")
Zipcode_label.grid(row=5, column=0)

Delete_containers_label = Label(root, text= "Delete ID")
Delete_containers_label.grid(row=8, column=0, pady=(10,0))

#Creating a Submit Botton
submit_btn =  Button (root, text="Add record to Database", command=submit )
submit_btn.grid(row =6, column = 1, columnspan= 2, padx = 10, ipadx=10, pady=10)
# submit_btn = Button(root,
#                        text = "Add record to Database").place(x = 40,
#                                               y = 130)

# Create a Search Button
Search_btn =  Button(root, text="Show Records", command= query)
Search_btn.grid(row=7,column=1, columnspan=2 ,padx=10, pady=10, ipadx=100)

# making a button to erase data from a database
delete_btn =  Button(root, text="Erase Records", command= delete)
delete_btn.grid(row=9,column=1, columnspan=2 ,padx=10, pady=10, ipadx=100)

#Commit Changes
conn.commit()

#Close Connection
conn.close()


root.mainloop()