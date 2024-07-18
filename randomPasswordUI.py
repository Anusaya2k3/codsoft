from tkinter import *
import string
import random
import pyperclip
import copy

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits  
    special_characters = string.punctuation


    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(lengthBox.get())


    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
    
 


    def copy():
        random_password=passwordField.get()
        pyperclip.copy(random_password)


   
    #Password=random.sample(all,password_length)
    #passwordField.insert(0,Password)

#object of tkinter
root=Tk()
root.config(bg="gray")
choice=IntVar()
Font=('arial',13,'bold')

#gui for password generator
#label name=passwordLabel
passwordLabel=Label(root,text="Password Generator",font=('times new roman',20,'bold'),bg='black',fg='white',width=40)
passwordLabel.grid()

weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=Font,width=20)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice,font=Font,width=20)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='strong',value=3,variable=choice,font=Font,width=20)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text="Password length",font=('times new roman',20,'bold'),bg='black',fg='white',width=40)
lengthLabel.grid(pady=5)

lengthBox=Spinbox(root,from_=5,to_=18,width=20,font=Font)
lengthBox.grid(pady=5)

generateButton=Button(root,text='Generate',font='Font',command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)

copyButton=Button(root,text='copy',font='Font',command=copy)
copyButton.grid(pady=5)



root.mainloop()
