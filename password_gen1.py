#To install pyperclip library, use command in cmd: pip install pyperclip

#importing Libraries
from tkinter import *
import random , string
import pyperclip

#initialize window
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PROJECT - PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
heading2 = Label(root, text = 'PASSWORD LENGTH' , font ='arial 8 bold').pack()
password_length = IntVar()

#to set password length
sp = Spinbox(root, from_=8, to = 32, textvariable = password_length).pack()
password = StringVar()

#Function to generate a password
def Generator():
    password_gen = ''
    x = password_length.get()
    for i in range (x):
        password_gen = password_gen + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    password.set(password_gen)

#Generate password button
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

#Text box will show password here
Entry(root, textvariable = password).pack()

#Function to copy generated password to clipboard
def Copy():
    pyperclip.copy(password.get())

#Copy to clipboard button
Button(root, text = "COPY TO CLIPBOARD " , command = Copy ).pack(pady= 5)

#Run
root.mainloop()











