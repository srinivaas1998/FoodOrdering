from tkinter import *
from mongo import *
from Menu import menu
root = Tk()
root.title('FooGo')
root.geometry('450x550')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def signUp():
    def register():
        frame = Frame(root, bg='lightgrey')
        create_record_button = Button(
            frame, text='Create Account', bg='black', fg='white', padx=10, pady=10,
            command=insert_data(name_entry.get(),phone_entry.get(),password_entry.get(),lat_entry.get(),long_entry.get()))

        create_record_button.grid(row=4, padx=120, pady=15)


    ##############################
    # Customer registration frame
    ##############################
    register_frame = Frame(root, bg='lightgrey')
    register_label = Label(register_frame, text='Registration',
                           font=('bold', 20), bg='lightgrey')
    name = Label(register_frame, text='Name :',
                        font=('bold', 10), bg='lightgrey')
    name_entry = Entry(register_frame, width=30)
    phone = Label(register_frame, text='phone :',
                         font=('bold', 10), bg='lightgrey')
    phone_entry = Entry(register_frame, width=30)

    password = Label(register_frame, text='Password :',
                  font=('bold', 10), bg='lightgrey')
    password_entry = Entry(register_frame, width=30)
    lat = Label(register_frame, text='Latitude :',
                     font=('bold', 10), bg='lightgrey')
    lat_entry = Entry(register_frame, width=30)
    long = Label(register_frame, text='Longitude :',
                     font=('bold', 10), bg='lightgrey')
    long_entry = Entry(register_frame, width=30)

    register_frame.grid(row=0, column=0, sticky='NSEW')
    register_label.grid(row=0, column=0, padx=100, pady=20)
    name.grid(row=1, column=0,padx=15, pady=15, sticky='W')
    name_entry.grid(row=1, column=0,pady=15, sticky='E')
    phone.grid(row=2, column=0,padx=15, pady=15, sticky='W')
    phone_entry.grid(row=2, column=0, pady=15, sticky='E')
    password.grid(row=3, column=0,padx=15, pady=15, sticky='W')
    password_entry.grid(row=3, column=0, pady=15, sticky='E')
    lat.grid(row=4, column=0, padx=15, pady=15, sticky='W')
    lat_entry.grid(row=4, column=0, pady=15, sticky='E')
    long.grid(row=5, column=0, padx=15, pady=15, sticky='W')
    long_entry.grid(row=5, column=0, pady=15, sticky='E')

    register_button = Button(register_frame, text='Register', bg='black',
                             fg='white', padx=10, pady=10, command=register)

    register_button.grid(row=6, column=0, padx=120, pady=15)
    finish_button = Button(
        register_frame, text='Finish', bg='black', fg='white', padx=10, pady=10, command=root.destroy)

    finish_button.grid(row=7,column =0, padx=120, pady=15)


def signIn():
    def login():
        c=select_data(phone_entry.get(), password_entry.get())
        print(c)
        if(c==1):
            menu()
        else:
            top1 = Toplevel();
            frame_inner1 = LabelFrame(top1, text="", padx=50, pady=50)
            frame_inner1.pack(padx=50, pady=50)
            innerLabel = Label(frame_inner1, text="Wrong ")
            innerLabel.pack()

        """create_record_button = Button(
                frame, text='Create Account', bg='black', fg='white', padx=10, pady=10,
                command=select_data(phone_entry.get(), password_entry.get()))

        create_record_button.grid(row=4, padx=120, pady=15)
"""
    ##############################
    # Customer registration frame
    ##############################
    signin_frame = Frame(root, bg='lightgrey')
    signin_label = Label(signin_frame, text='Sign In',
                               font=('bold', 20), bg='lightgrey')
    phone = Label(signin_frame, text='phone :',
                      font=('bold', 10), bg='lightgrey')
    phone_entry = Entry(signin_frame, width=30)

    password = Label(signin_frame, text='Password :',
                 font=('bold', 10), bg='lightgrey')
    password_entry = Entry(signin_frame, width=30)

    signin_frame.grid(row=0, column=0, sticky='NSEW')
    signin_label.grid(row=0, column=0, padx=100, pady=20)
    password.grid(row=3, column=0,padx=50, pady=15, sticky='W')
    password_entry.grid(row=3, column=0, pady=15, sticky='E')
    phone.grid(row=2, column=0,padx=70, pady=15, sticky='W')
    phone_entry.grid(row=2, column=0, pady=15, sticky='E')

    signin_button = Button(signin_frame, text='SignIn', bg='black',
                             fg='white', padx=10, pady=10, command=login)

    signin_button.grid(row=4, column=0, padx=120, pady=15)


home_frame = Frame(root, bg='lightgrey')
title_label = Label(
    home_frame, text='FooGo', font=('bold', 20), bg='lightgrey')
signup_button = Button(
    home_frame, text='SignUp', bg='black', fg='white', padx=10, pady=10, command=signUp)
signin_button = Button(
    home_frame, text='SignIn', bg='black', fg='white', padx=10, pady=10, command=signIn)

home_frame.grid(row=0, column=0, sticky='NSEW')
title_label.grid(row=1, column=0, sticky='NSEW', padx=150, pady=30)
signup_button.grid(row=2, padx=150, pady=15)
signin_button.grid(row=3, padx=150, pady=15)







root.mainloop()


