# importing necessary libraries
import tkinter as tk
import string
import random
from tkinter import messagebox

# create a tkinter window
root = tk.Tk()
#set the geometry(widthxheight)
root.geometry('544x335')
root.minsize(400,250)

# root window title
root.title("Password Generator")

# widgets
# creating a label 
heading = tk.Label(root,text="Password Generator",font=("Georgia",20,"bold"))
heading.pack(pady=30)

# the label for the length of the password
label = tk.Label(root,text="Enter the length of the password",font=("Helvetica",11))
label.pack(pady=15)

# creating an entry for the length of the password
entry = tk.Entry(root,width=10)
entry.pack()

# function to generate a strong password with specified length
def generateStrongPassword(length):
    upper = string.ascii_uppercase     # uppercase letters
    lower = string.ascii_lowercase     # lowercase letter
    digits = string.digits             # numeric digits
    symbols = string.punctuation       # punctuation symbols

    # password contains atleast one character from each character set
    pw = [random.choice(upper),random.choice(lower),random.choice(digits),random.choice(symbols)]
    
    remainingLength = length-4
    characterslist = list(upper+lower+digits+symbols)

    # extend the pw list with random characters from characterslist
    for i in range(remainingLength):
        pw.extend(random.choice(characterslist))

    return "".join(pw)

# function to handle button click event and generate the password
def onClick():
    len = entry.get()
    if len == '':
        # display error message in case of an empty input
         messagebox.showerror('Error','Please provide an input')
    else:
        try:
            length = int(len)
            if length < 6:
                # display a warning if the password length is too short
                messagebox.showwarning('Warning','Minimum length of the password should be 6')
            else:
                password = generateStrongPassword(length)
                msg = "Password is : "+password
                label.configure(text=msg)

                # hiding the input field and button
                entry.pack_forget()
                button.pack_forget()

                # display the new button with added padding
                newButton.pack(pady=10)
                
        except:
            # display an error message if the input is not a number i.e a string or a character
            messagebox.showerror('Error','Invalid input! Please enter a valid number')

# creating button
button = tk.Button(root,text="Generate",foreground="blue",command = onClick)
button.pack(pady=4)

newButton = tk.Button(root,text="Generate another password",foreground="blue",command = onClick)

# execute Tkinter
root.mainloop()