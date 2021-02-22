#Made By Ayush shete  #First year student fo Ramdeobaba College of Engineering and Management 

import sys
import os
import key_generator
import random
import string
import time
import datetime as dt
import tkinter.messagebox as tmsg
from tkinter import *
from books import Books
from PIL import Image, ImageTk
from Login_Email_Details import Email_Accounts
from Login_username_Details import Username_Accounts
from tkcalendar import Calendar, DateEntry
import urllib.request
from SecrData import *


import win32gui
import win32con       

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        Footer_Value.set('◉ Online\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t © Central Library (Made By Ayush Shete)')
        return True
       
    except:
        Footer_Value.set('◯ Offline\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t © Central Library (Made By Ayush Shete)')
        return False




def Restart_Login():
    Root.destroy()
    os.startfile("main_Login.py")


def center_window(w=300, h=200):
    # get screen width and height
    ws = Root.winfo_screenwidth()
    hs = Root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    Root.geometry('%dx%d+%d+%d' % (w, h, x, y))


num_for_Avai_book = 0
num_for_Borrow_book = 0
num_for_history = 0
Guest_Count = 0
count = 0
ABC = 0

date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y , %H:%M:%S}"


def Exit_TK():
    Exit = tmsg.askyesno('quit', 'Are you sure to Exit Central Library')
    if Exit == True:

        quit()
    else:
        pass


def Save_History(Status, BookName):
    Data = open('Data/Data.py', 'a')

    if Entry_email_username_value.get() == '':
        Username = "Guest"
    else:
        Username = Entry_email_username_value.get()

    Data.write(f'''
    Email/Username:- {Username}                            Date:- {format_date}
    Status:- {Status}           
    Book Name:- {BookName}\n
    ''')
    Data.close()


def Loading():
    Root.configure(bg='gray5')
    frame1 = Frame(Root, bg="gray5", height=25)
    frame1.pack(fill=Y)
    frame2 = Frame(Root, bg='gray5', height=25)
    frame2.pack(fill=Y)
    frame3 = Frame(Root, bg='gray5', height=25)
    frame3.pack(fill=Y)

    a1 = "indexing........"
    a2 = "Central Library "
    for k in range(16):

        time.sleep(0.15)
        Root.update()

        Load1 = Label(frame1, text=a2[k], height=2, bg='gray5',
                      fg='cyan', font="Fraunces 100 bold")
        Load1.pack(side=LEFT, fill=Y, pady=70)

        index = Label(frame3, text=a1[k], fg='white', bg="gray5")
        index.pack(side=LEFT, anchor='ne')

    frame3.pack_forget()

    # b = 'Made By Ayush Shete '
    # for k in range(15):
    #     time.sleep(0.1)
    #     Root.update()

    #     Load2 = Label(frame2, text=b[k],  bg='gray5', fg='White',
    #                   font="Fraunces 20 bold")
    #     Load2.pack(side=LEFT, anchor="w", fill=Y)

    time.sleep(1)
    frame1.pack_forget()
    frame2.pack_forget()


Root = Tk()


center_window(1200, 600)
Root.title("Central Library")

Root.wm_minsize(1200, 600)
Icon_Book = PhotoImage(file = 'Icons/logo.png')
Root.iconphoto(False, Icon_Book)

# Calling Loading
# Loading()

Root.configure(bg='white')

# LOGIN
# Registration Function
def Reg_Fun():
    
    Footer_Value.set('wait your data is in process')
    global ABC
    if ABC !=0:
        # resting all values
        Required_name.pack_forget()
        Required_email.pack_forget()
        Required_email_Ends_with.pack_forget()
        Required_password.pack_forget()
        Required_phone.pack_forget()
        Required_phone_count.pack_forget()
        Required_phone_digit.pack_forget()
        Required_fullname.pack_forget()
        if CheckBox_Value_left.get() == 0:
            Footer_Value.set('ERROR!! Check the Box')

        if Entry_fullname_value.get() == "":
            Required_fullname.pack(anchor="e")


        if Entry_number_value.get() == '':
            Required_phone.pack(anchor="e")
        else:
            if Entry_number_value.get().isdigit():
                if len(Entry_number_value.get()) != 10:
                    Required_phone_count.pack(anchor="e")

            else:
                Required_phone_digit.pack(anchor="e")

        if Entry_name_value.get() == "":
            Required_name.pack(anchor="e")

        if Entry_email_value.get() == '':
            Required_email.pack(anchor="e")
        else:
            if Entry_email_value.get().endswith('@gmail.com'):
                pass
            else:
                Required_email_Ends_with.pack(anchor="e")

        if Entry_password_value.get() == '':
            Required_password.pack(anchor="e")

        # final if statement
        if CheckBox_Value_left.get() != 0 and Entry_name_value.get() != "" and Entry_email_value.get() != '' and Entry_email_value.get().endswith('@gmail.com') and Entry_password_value.get() != '':
            Footer_Value.set("is almost completed")
            if Entry_name_value.get() in Username_Accounts.keys():
                Footer_Value.set('username is used by somebody else')
            elif Entry_email_value.get() in Email_Accounts.keys():
                Footer_Value.set('Email is used by somebody else')
            else:

                Email_Accounts[Entry_email_value.get(
                )] = Entry_password_value.get()
                f = open('Login_Email_Details.py', "w")
                f.write(f'Email_Accounts={Email_Accounts}')
                f.close()

                Username_Accounts[Entry_name_value.get(
                )] = Entry_password_value.get()
                f = open('Login_username_Details.py', "w")
                f.write(f'Username_Accounts={Username_Accounts}')
                f.close()

                a0 = Entry_fullname_value.get()
                a1 = Entry_email_value.get()
                a2 = Entry_number_value.get()
                a3 = Entry_name_value.get()
                a4 = Entry_password_value.get()
                a5 = Birth_Date.get()
                # Clear file
                Mail_Data_clr = open('Data/MData.txt', 'w')
                Mail_Data_clr.write('')
                Mail_Data_clr.close()

                Mail_Data = open('Data/MData.txt', 'w')
                Mail_Data.write(f'''
                Name:- {a0}                     Date:- {format_date}
                Username:- {a3}                 Birth Date:-{a5}
                Contact:- {a2}
                Email:- {a1}
                Password:-{a4}
                ''')
                Mail_Data.close()

                # SEND EMAIL
                Footer_Value.set("is almost completed")

                Email_sec_Data_by_Reg_btn()
                # Restart_Login()
                global Email_label
                Entry_name_value.set('')
                Entry_email_value.set('')
                Entry_password_value.set('')
                Entry_verify_code_value.set('')
                Entry_fullname_value.set('')
                Entry_number_value.set('')
                Email_label.pack_forget()
                Verify_label.pack_forget()
                email_verify_Entry.pack_forget()
                Verify_Code.pack(side=RIGHT, padx=(0, 100))
                email_verify_Entry.pack(fill=X, side=RIGHT)
                Verify_Button1.pack(side=RIGHT, padx=8)
                Footer_Value.set('Successfully Register you can Login with your data')

                

        # # Clear after Sending Email
        Mail_Data_Clr = open('Data/MData.txt', 'w')
        Mail_Data_Clr.write('''\\x50\\x59\\x41\\x52\\x4d\\x4f\\x52\\x00\\x00\\x03\\x09\\x00\\x61\\x0d\\x0d\\x0a\\x06\\x27\\xa0\\x01\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x40\\x00\\x00\\x00\\xbb\\x28\\x00\\x00\\x00\\x00\\x00\\x18\\xf6\\x69\\x10\\xfd\\x49\\x0d\\x53\\x02\\x30\\xa8\\xdf\\x14\\xf4\\x04\\x84\\xab\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xd2\\x98\\xbd\\x29\\x7a\\x3b\\x39\\x27\\x87\\xb3\\xb7\\x2a\\x0d\\x30\\x88\\xbf\\xc6\\x36\\xf0\\xa0\\x6c\\x4b\\x32\\xb4\\x26\\x37\\x45\\x0c\\xf6\\xd7\\xe6\\x00\\x46\\x9d\\xe4\\xa6\\x75\\x12\\xec\\x34\\x2b\\x67\\xea\\x8b\\x03\\x4a\\x31\\xce\\xec\\xc8\\xf5\\x56\\x78\\xca\\xf5\\x81\\x80\\x3e\\xf5\\xe1\\x60\\xcd\\xa4\\xed\\xee\\xad\\x21\\x23\\xef\\x9e\\x25\\x94\\xac\\xe1\\x60\\x74\\xfc\\xfd\\xdd\\x0d\\x75\\x1b\\x91\\x4f\\xb6\\x20\\x9d\\x86\\xad\\x3f\\x4c\\x0f\\x09\\x45\\x9d\\x14\\x17\\x37\\x33\\x6b\\x67\\x1c\\x15\\x0e\\x44\\x55\\xf8\\x5f\\xa6\\x0a\\x7d\\x6f\\xf5\\xe3\\xe0\\x0f\\x5e\\xae\\x0e\\xf2\\x20\\x7f\\x23\\x9e\\x60\\x8e\\x50\\xae\\x19\\x52\\x4d\\xdc\\x86\\xbb\\xda\\xb1\\xaa\\x7f\\xca\\x9d\\x63\\xd6\\xd0\\xe6\\xc5\\x17\\x8e\\x2a\\xd9\\xc9\\x7f\\x8e\\x89\\x94\\x6f\\xd3\\xa9\\x98\\xad\\x40\\xa6\\x77\\x07\\xa8\\x61\\x34\\xc3\\xd3\\x57\\xf4\\x40\\xa2\\x70\\x10\\x86\\x8d\\xe4\\x27\\x1d\\x0e\\xe6\\x68\\xbb\\x5c\\xb6\\xbb\\x99\\x94\\xb1\\x05\\xac\\x96\\x8f\\x8e\\x3c\\xe4\\x33\\xfe\\x78\\xfc\\x18\\xfc\\x6c\\x06\\xc4\\x4e\\x3d\\x37\\x59\\xb7\\x6e\\x99\\xf3\\xab\\x35\\x4d\\xe7\\xc7\\x47\\x32\\xed\\x20\\x09\\x27\\x4c\\x7c\\xa2\\x2d\\x05\\x52\\x5e\\xaa\\x1b\\x5e\\x86\\xc2\\x6d\\x51\\x4b\\xef\\xc2\\xc7\\x4f\\x57\\x6e\\x13\\x15\\xc0\\x09\\x1a\\x53\\x8b\\x63\\x8c\\x01\\x21\\x56\\x46\\xa6\\x2c\\x6a\\x30\\xd5\\xf5\\x82\\xa5\\xe4\\x9c\\x09\\x9a\\x4d\\xe7\\xf1\\xc0\\x51\\x0e\\x26\\x93\\x2b\\x2b\\xf8\\x11\\x3f\\x76\\x07\\xb8\\xc7\\xc6\\x6d\\xb8\\x ''')
        Mail_Data_Clr.close()

        CheckBox_Value_left.set(0)
    else:
        Footer_Value.set('Email is not verified')


def Log_Fun():
    Capacha2 = Capacha_Code.get()
    if Enter_Capatcha.get() == Capacha2:

        Footer_Value.set('')
        Required_password_login.pack_forget()
        Required_email_login.pack_forget()

        if CheckBox_Value_Right.get() == 0:
            Footer_Value.set('ERROR!! Check the Box')

        if Entry_password_login_value.get() == '':
            Required_password_login.pack(anchor="e")

        if Entry_email_username_value.get() == "":
            Required_email_login.pack(anchor="e")
        if CheckBox_Value_Right.get() != 0 and Entry_password_login_value.get() != '' and Entry_email_username_value.get() != "":
            if (Entry_email_username_value.get() in Email_Accounts.keys()):
                if Entry_password_login_value.get() == Email_Accounts[Entry_email_username_value.get()]:

                    Main_Screen()

                else:
                    Footer_Value.set('Invalid Password!! check your password')
                    Entry_password_login_value.set('')

            elif(Entry_email_username_value.get() in Username_Accounts.keys()):
                if Entry_password_login_value.get() == Username_Accounts[Entry_email_username_value.get()]:

                    Main_Screen()

                else:
                    Footer_Value.set('Invalid Password!! check your password')
                    Entry_password_login_value.set('')

            else:

                Footer_Value.set('Username/Email is not registered')

        CheckBox_Value_Right.set(0)
    else:
        Footer_Value.set('Invalid Captacha')




# Footer
Footer_Value = StringVar()
Footer_Value.set('© Central Library (Made By Ayush Shete)')
Footer1 = Label(Root, bg='black', fg='white', textvar=Footer_Value)
Footer1.pack(fill=X, side=BOTTOM)


# Bottom Frame
Frame_Bottom = Frame(Root, bg="steelblue4", border='5')
Frame_Bottom.pack(side=BOTTOM, fill=BOTH)
Guest_Label = Label(
    Frame_Bottom, text="Guest Mode", font='Fraunces 10 bold', bg="steelblue4")
Guest_Label.pack(side=LEFT)


# Left Frame
Frame_Left = Frame(Root, bg="#80f3ff", border='5')
Frame_Left.pack(side=LEFT, fill=BOTH, anchor='n', padx=30, pady=(0, 30))

FL1 = Label(Frame_Left, text="  \t New User Registration     \t  ",
            font='Oswald 30 bold', bg='#80f3ff')
FL1.pack(fill=X)

#NAME
name = Label(Frame_Left, text='Enter Full Name:',
             font="Abel 15", bg='#80f3ff')
name.pack(padx=11, pady=5)
Entry_fullname_value = StringVar()
Entry_fullname_value.set('')
full_name_Entry = Entry(
    Frame_Left, textvar=Entry_fullname_value, font="Abel 15")
full_name_Entry.pack(padx=100, fill=X)
Required_fullname = Label(full_name_Entry, text='*Required field',
                          pady=3, fg="red", bg='white')

Username_frame = Frame(Frame_Left, bg='#80f3ff')
Username_frame.pack(fill=X)

#USERNAME
name_username = Label(Username_frame, text='Enter username:',
                      font="Abel 15", bg='#80f3ff')

#BIRTHDATE
user_date = Label(Username_frame, text='Enter Birth Date:',
                  font="Abel 15", bg='#80f3ff')
name_username.pack()

Entry_username_frame = Frame(Frame_Left, bg='#80f3ff')
Entry_username_frame.pack(fill=X)
Entry_name_value = StringVar()
Entry_name_value.set('')
name_Entry = Entry(Entry_username_frame,
                   textvar=Entry_name_value, font="Abel 15", width=20)
name_Entry.pack(padx=(100, 100), fill=X)
Required_name = Label(Entry_username_frame, text='*Required field',
                      pady=3, fg="red", bg='#80f3ff')

Birth_Date = DateEntry(Entry_username_frame, width=30, background='gray99',
                       foreground='black', borderwidth=2)

def show_BirthDate(event):
    name_username.pack_forget()
    name_username.pack(side=LEFT, padx=(120, 0))
    user_date.pack(side=RIGHT, padx=(0, 120))
    name_Entry.pack_forget()
    name_Entry.pack(padx=(100, 0), fill=X, side=LEFT, anchor='w')
    Birth_Date.pack(padx=(0, 100), side=RIGHT)


name_Entry.bind('<Enter>', show_BirthDate)

#PHONE NUMBER
phone = Label(Frame_Left, text='Enter phone number:',
              font="Abel 15", bg='#80f3ff')
phone.pack(padx=11, pady=5)
Entry_number_value = StringVar()
Entry_number_value.set('')
phone_Entry = Entry(Frame_Left, textvar=Entry_number_value, font="Abel 15")
phone_Entry.pack(padx=100, fill=X)
Required_phone = Label(phone_Entry, text='*Required field',
                       pady=3, fg="red", bg='white')
Required_phone_digit = Label(phone_Entry, text='*Enter Digit',
                             pady=3, fg="red", bg='white')
Required_phone_count = Label(phone_Entry, text='*Invalid count Number',
                             pady=3, fg="red", bg='white')

Email_Frame_Text = Frame(Frame_Left, bg='#80f3ff')
Email_Frame_Text.pack(fill=X)

#EMAIL
email = Label(Email_Frame_Text, text='Enter Email:',
              font="Abel 15", bg='#80f3ff')
email.pack()


Email_Frame_Entry = Frame(Frame_Left, bg='#80f3ff')
Email_Frame_Entry.pack(fill=X)

Entry_email_value = StringVar()
Entry_email_value.set('')
email_Entry = Entry(Email_Frame_Entry,
                    textvar=Entry_email_value, font="Abel 15")
email_Entry.pack(fill=X, padx=(100, 100))

Required_email = Label(
    Email_Frame_Entry, text='*Required field', fg="red", bg='#80f3ff')

Required_email_Ends_with = Label(
    Email_Frame_Entry, text='*Invalid Email', pady=3, fg="red", bg='#80f3ff')

# Random Code Generator



def Sending_Code():
    global CODE
    Verify_Button1.pack_forget()
    Verify_Button2.pack(side=RIGHT, padx=8)
    Required_email.pack_forget()

    if Entry_email_value.get() in Email_Accounts.keys():
        Footer_Value.set('Email is used by somebody else')
    else:
        if Entry_email_value.get() == '':
            Required_email.pack_forget()
            Required_email.pack(anchor="e")
            
        else:
            # Footer_Value.set(CODE)
            if Entry_email_value.get().endswith('@gmail.com'):
                import smtplib
                from plyer import notification
                S = string.digits

                s = []
                s.extend(list(S))

                random.shuffle(s)

                CODE = ("".join(s[0:7]))
                print(CODE)

                GMAIL_ID = 'centrallibraryproject@gmail.com'
                GMAIL_PSWD = 'Password_Library_123456789'

                Message = f'''
                Hello,

                Thank you for signing up for Central Library!

                Your 7-digit verification code is:

                {CODE}

                Enter this verification code on the Central Library registration page where you requested the code. This code is valid for 30 minutes.

                Welcome and happy building!

                Thank you,
                Central Library'''

                To = Entry_email_value.get()
                Subject = 'Central Library verification code'

                try:

                    Email = smtplib.SMTP('smtp.gmail.com', 587)
                    Email.starttls()
                    Email.login(GMAIL_ID, GMAIL_PSWD)
                    Email.sendmail(
                        GMAIL_ID, To, f"Subject: {Subject}\n\n{Message}")

                    ICON_PATH = "Icons\\Logo.ico"
                    notification.notify(
                        app_icon = ICON_PATH,
                        title="Central Library",
                        message=f"Conformation code is send to your email. Check Your Email Inbox",
                        timeout=4
                    )
                    Footer_Value.set("check your email Inbox")
                    Email.Exit_TK()
                except:
                    pass
            else:
                Required_email_Ends_with.pack(anchor="e")

Email_label = Label(email_Entry, text="Email Verify Succesfully", font=15)


def Check_Code():
    global CODE

    if Entry_verify_code_value.get() == CODE:
        Verify_label.pack()
        Verify_Code.pack_forget()
        Verify_Button1.pack_forget()
        Verify_Button2.pack_forget()
        email_verify_Entry.pack(fill=X, side=RIGHT, padx=(0, 100))
        Email_label.pack()
        global ABC

        ABC = ABC+1
    else:
        Footer_Value.set("Invalid Code")

        

#CODE VERIFY
Verify_Code = Button(Email_Frame_Entry, text='Verify',
                     bg='gray50', cursor='hand2', command=Check_Code, activebackground="gray50")



Entry_verify_code_value = StringVar()
Entry_verify_code_value.set('') 
email_verify_Entry = Entry(
    Email_Frame_Entry, textvar=Entry_verify_code_value, font="Abel 15", width='8')
def return_conectivity(event):
    connect()

email_verify_Entry.bind('<Enter>', return_conectivity )


Verify_label = Label(email_verify_Entry,
                     text='   Verify   ', bg='green', fg='black')

#GET CODE
Verify_Button1 = Button(Email_Frame_Entry, text=' Get Code ',
                       bg='gray50', cursor='hand2', command=Sending_Code, activebackground="gray50")
Verify_Button2 = Button(Email_Frame_Entry, text='resend Mail',
                       bg='gray50', cursor='hand2', command=Sending_Code, activebackground="gray50")


def show_verify(event):
    Required_email.pack_forget()
    Verify_Button2.pack_forget()
    email.pack(padx=(160, 80), pady=5, side=LEFT)
    email_Entry.pack_forget()
    email_Entry.pack(fill=X, side=LEFT, padx=(100, 0))
    Verify_Code.pack(side=RIGHT, padx=(0, 100))
    email_verify_Entry.pack(fill=X, side=RIGHT)
    Verify_Button1.pack(side=RIGHT, padx=8)
   
email_Entry.bind('<Enter>', show_verify)

#PASSWORD
password = Label(Frame_Left, text='Enter password:',
                 font="Abel 15", fg="black", bg='#80f3ff')
password.pack(padx=11, pady=5)
Entry_password_value = StringVar()
Entry_password_value.set('')
password_Entry = Entry(Frame_Left, show='●',
                       textvar=Entry_password_value, font="Abel 15")
password_Entry.pack(padx=100, fill=X)
# Show_btn = Btn(password_Entry,text=)
Required_password = Label(
    password_Entry, text='*Required field', pady=3,  fg="red", bg='white')

#CHECK BOX
CheckBox_Value_left = IntVar()
CheckBox_Value_left.set(0)
Robot_Check_left = Checkbutton(
    Frame_Left, text='I am Human', bg='azure', variable=CheckBox_Value_left, border=10, cursor='hand2', activebackground="azure")
Robot_Check_left.pack(pady=5)

password_Entry1 = Entry(
    password_Entry, textvar=Entry_password_value, font="Abel 15")


def in_hover(event):
    Footer_Value.set(password_Entry.get())


def out_hover(event):
    Footer_Value.set('')
    connect()


# key image


load = Image.open("Icons/key.png")
render = ImageTk.PhotoImage(load)
img_key = Button(password_Entry, image=render, relief=FLAT,
                 cursor='hand2', activebackground="white")
img_key.image = render
img_key.pack(side=RIGHT)
img_key.bind('<Enter>', in_hover)
img_key.bind('<Leave>', out_hover)

# Register_Button
Reg_Btn = Button(Frame_Left, text="Register", command=Reg_Fun,
                 bg='turquoise1', font="Fraunces 20  bold", cursor='hand2', activebackground="turquoise1")
Reg_Btn.pack(pady=5)


# Right Frame
Frame_Right = Frame(Root, bg="#00b8cb", border='5')
Frame_Right.pack(side=RIGHT, fill=BOTH, anchor='n', padx=(0, 30), pady=(0, 30))

RL1 = Label(Frame_Right, text="            Login            ",
            font='Oswald 30 bold', bg='#00b8cb')
RL1.pack()

#USERNAME
email_Username = Label(
    Frame_Right, text='\nEnter email or username:', font="Abel 15", bg='#00b8cb')
email_Username.pack(padx=11, pady=5)
Entry_email_username_value = StringVar()
Entry_email_username_value.set('')
email_username_Entry = Entry(
    Frame_Right, textvar=Entry_email_username_value, font="Abel 15")
email_username_Entry.pack(padx=30, fill=X)

Required_email_login = Label(
    email_username_Entry, text='*Required field', pady=3, fg="red", bg='white')


#PASSWORD
password_login = Label(Frame_Right, text='Enter password:',
                       font="Abel 15", bg='#00b8cb')
password_login.pack(padx=11, pady=5)
Entry_password_login_value = StringVar()
Entry_password_login_value.set('')
password_login_Entry = Entry(
    Frame_Right, show='●', textvar=Entry_password_login_value, font="Abel 15")
password_login_Entry.pack(padx=30, fill=X, pady=(0, 10))
Required_password_login = Label(
    password_login_Entry, text='*Required field', pady=3, fg="red", bg='white')


def in_hover_login(event):

    Footer_Value.set(password_login_Entry.get())


def out_hover_login(event):
    Footer_Value.set('')
    connect()


# key image

load = Image.open("Icons/key.png")
render = ImageTk.PhotoImage(load)
img_key = Button(password_login_Entry, image=render,
                 relief=FLAT, cursor='hand2')
img_key.image = render
img_key.pack(side=RIGHT)
img_key.bind('<Enter>', in_hover_login)
img_key.bind('<Leave>', out_hover_login)

#CAPATCHA
Verify_Capatcha = Frame(Frame_Right, bg='#00b8cb')
Verify_Capatcha.pack()


Capacha = key_generator.Random_Number1()
Capacha_Code = StringVar()
Capacha_Code.set(Capacha)
Show_Capatcha = Label(Verify_Capatcha, textvar=Capacha_Code, font='bold')
Show_Capatcha.pack(pady=3, fill=X)


def Refresh_btn():
    import string
    import random

    s1 = string.ascii_letters
    s2 = string.digits
    # s3 = string.punctuation

    s = []
    # extend is same as apend bt apend direct put main file to other bt extend put element to another
    s.extend(list(s1))
    s.extend(list(s2))

    random.shuffle(s)

    Capacha_Code.set(("".join(s[0:5])))


load = Image.open("Icons/refresh.png")
render = ImageTk.PhotoImage(load)
img_reset = Button(Show_Capatcha, image=render,
                   relief=FLAT, cursor='hand2', anchor='e', command=Refresh_btn)
img_reset.image = render
img_reset.pack(side=RIGHT, anchor='e')

#ENTR cAPATCHA
Capacha_Code_Entry = StringVar()
Capacha_Code_Entry.set('')
Enter_Capatcha = Entry(Verify_Capatcha, text=Capacha_Code_Entry, font='10')
Enter_Capatcha.pack(pady=5, fill=X)

#CHECK BOX
CheckBox_Value_Right = IntVar()
CheckBox_Value_Right.set(0)
Robot_Check = Checkbutton(Frame_Right, text='I am Human', bg='azure',
                          variable=CheckBox_Value_Right, border=10, cursor='hand2', activebackground="azure")
Robot_Check.pack(pady=5)

# Login_Button
Log_Btn = Button(Frame_Right, text=" Login ", command=Log_Fun,
                 bg='deepskyblue', font="Fraunces 20  bold", cursor='hand2', activebackground="deepskyblue")
Log_Btn.pack(pady=5)

# Forgot password
Forgot_Btn = Label(Frame_Right, text="*Forgot username and password",
                   relief=FLAT, cursor='hand2', bg='#00b8cb', activebackground="#00b8cb")
Forgot_Btn.pack(pady=5)
Entry_email_username_value.set('')

    

# MAIN SCREEN FUNCTION

def Main_Screen():
    connect()
    if Entry_email_username_value.get() == '':
        Entry_email_username_value.set("Login Now")

    global Guest_Count
    # Background_Color
    Root.configure(bg='#1e1e1e')
 
    # Binds_Hover_Color
    Footer1.pack_forget()
    Footer2 = Label(Root,bg='black', fg='white',
                    anchor='w', textvar=Footer_Value)
    Footer2.pack(side=BOTTOM, fill=X)
    Frame_Right.pack_forget()
    Frame_Left.pack_forget()
    Frame_Bottom.pack_forget()

    def TOP_FRAME():


        def Binds_f5(key):
            def on_leave(event):
                key['bg'] = 'gray'
                key['fg'] = 'black'

            def on_enter(event):

                key['background'] = 'gray40'
                key['fg'] = 'yellow'

            key.bind('<Enter>', on_enter)
            key.bind('<Leave>', on_leave)

        B1 = Button(f5, padx=4, relief=FLAT, cursor='hand2',
                    bg="gray", fg="black", text="Check Available Books ⩔\t", command=Available_Books, activebackground="gray")
        B1.pack(side=LEFT)
        B2 = Button(f5, padx=4, relief=FLAT, cursor='hand2',
                    bg="gray", fg="black",  text="Borrow Books ⩔\t", command=Book_Borrow, activebackground="gray")
        B2.pack(side=LEFT)
        B3 = Button(f5, padx=4, relief=FLAT, cursor='hand2',
                    bg="gray", fg="black",  text="Add/Return Books ⩔\t", command=Add_Return_Book, activebackground="gray")
        B3.pack(side=LEFT)
        B5 = Button(f5, relief=FLAT, cursor='hand2',
                    bg="gray", fg="black",  text="History ⩔", command=History, activebackground="gray")
        B5.pack(side=LEFT)
        Button(f5, text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', bg="gray",
               fg="black", relief=FLAT, activebackground="gray").pack(side=LEFT)

        Binds_f5(B1)
        Binds_f5(B2)
        Binds_f5(B3)
        Binds_f5(B4)
    def Available_Books():
        main_Footer.set('')
        global num_for_Avai_book
        global num_for_Borrow_book
        global num_for_history

        Frame_Add_Return_Book.pack_forget()
        while True:
            if num_for_Borrow_book == 0:
                Frame_Borrow_Book1.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 1:
                Frame_Borrow_Book2.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 2:
                Frame_Borrow_Book3.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 3:
                Frame_Borrow_Book4.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 4:
                Frame_Borrow_Book5.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 5:
                Frame_Borrow_Book6.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 6:
                Frame_Borrow_Book7.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 7:
                Frame_Borrow_Book8.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 8:
                Frame_Borrow_Book9.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 9:
                Frame_Borrow_Book10.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 10:
                Frame_Borrow_Book11.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 11:
                Frame_Borrow_Book12.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 12:
                Frame_Borrow_Book13.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 13:
                Frame_Borrow_Book14.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 14:
                Frame_Borrow_Book15.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 15:
                Frame_Borrow_Book16.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 16:
                Frame_Borrow_Book17.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 17:
                Frame_Borrow_Book18.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Borrow_book == 18:
                Frame_Borrow_Book19.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Borrow_book == 19:
                Frame_Borrow_Book20.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_Borrow_Book20.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        while True:
            if num_for_history == 0:
                Frame_history1.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 1:
                Frame_history2.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 2:
                Frame_history3.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 3:
                Frame_history4.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 4:
                Frame_history5.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 5:
                Frame_history6.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 6:
                Frame_history7.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 7:
                Frame_history8.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 8:
                Frame_history9.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 9:
                Frame_history10.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 10:
                Frame_history11.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 11:
                Frame_history12.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 12:
                Frame_history13.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 13:
                Frame_history14.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 14:
                Frame_history15.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 15:
                Frame_history16.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 16:
                Frame_history17.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 17:
                Frame_history18.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_history == 18:
                Frame_history19.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_history == 19:
                Frame_history20.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_history20.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        while True:
            if num_for_Avai_book == 0:
                Frame_Book_Available1.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available1, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available1)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available1, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')

                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 1:
                Frame_Book_Available2.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available2, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available2)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available2, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')

                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 2:
                Frame_Book_Available3.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available3, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available3)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available3, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(

                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 3:
                Frame_Book_Available4.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available4, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available4)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available4, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 4:
                Frame_Book_Available5.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available5, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available5)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available5, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 5:
                Frame_Book_Available6.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available6, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available6)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available6, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 6:
                Frame_Book_Available7.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available7, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available7)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available7, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 7:
                Frame_Book_Available8.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available8, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available8)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available8, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 8:
                Frame_Book_Available9.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available9, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available9)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available9, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break

            elif num_for_Avai_book == 9:
                Frame_Book_Available10.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available10, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available10)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available10, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 10:
                Frame_Book_Available11.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available11, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available11)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available11, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 11:
                Frame_Book_Available12.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available12, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available12)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available12, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 12:
                Frame_Book_Available13.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available13, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available13)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available13, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 13:
                Frame_Book_Available14.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available14, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available14)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available14, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 14:
                Frame_Book_Available15.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available15, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available15)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available15, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 15:
                Frame_Book_Available16.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available16, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available16)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available16, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 16:
                Frame_Book_Available17.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available17, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available17)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available17, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 17:
                Frame_Book_Available18.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available18, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available18)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available18, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 18:
                Frame_Book_Available19.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available19, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available19)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available19, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            elif num_for_Avai_book == 19:

                Frame_Book_Available20.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available20, text='Book Avaibility', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)

                SB = Scrollbar(Frame_Book_Available20)
                SB.pack(side=RIGHT, fill=Y)

                LB = Listbox(Frame_Book_Available20, yscrollcommand=SB.set,
                             height=100, font="20", bg='gray90')
                LB.insert(END, '  #CODE                    #BOOK NAME')
                LB.insert(END, '')
                Books_Name = []
                Books_Code = []
                for i in Books.values():
                    Books_Name.append(i)
                for i in Books.keys():
                    Books_Code.append(i)
                Range = len(Books_Code)

                for j in range(Range):
                    LB.insert(
                        END, f'  {Books_Code[j]}                       {Books_Name[j]}')

                LB.pack(fill=X, padx=5)

                SB.config(command=LB.yview)
                break
            else:
                Frame_Book_Available20.pack(fill=BOTH)
                l1 = Label(Frame_Book_Available20, text='Book Avaibility  (ERROR)', anchor="w",
                           font="Fraunces 11 bold")
                l1.pack(pady=10, padx=5, fill=X)

                Exit1 = Button(l1, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit1.pack(side=RIGHT)
                for i in range(15):
                    if i == 5:
                        Label(Frame_Add_Return_Book, text="", font="100",
                              bg='gray40').pack(fill=BOTH)
                        Button(Frame_Add_Return_Book,
                               text='Click to Exit', command=Exit_TK).pack()
                    else:
                        Label(Frame_Add_Return_Book, text="", font="100",
                              bg='gray40').pack(fill=BOTH)

    def Book_Borrow():
        global num_for_Avai_book
        global num_for_Borrow_book
        global num_for_history

        def Borrow_Book():

            if Entry_email_username_value.get() != 'Login Now':
                main_Footer.set('')

                Code_List = []

                for i in Books.keys():

                    Code_List.append(i)

                check1 = Enter_Code.get().isdigit()
                if (check1 == False):
                    main_Footer.set('Invalid Code Enter Valid Code')
                else:
                    a = int(Enter_Code.get())

                    check2 = a in Code_List
                    check3 = len(Enter_Code.get())

                    if (check2 == True) and (check3 == 4):

                        B_Code = Enter_Code.get()
                        B = int(B_Code)

                        main_Footer.set(
                            f'Thanks for Borrowing Book ■ {Books[B]} ■ Return Within ## Days')
                        Save_History('Book Borrow', Books[B])

                        del Books[B]

                    else:
                        if Enter_Code.get() == '':
                            main_Footer.set('Enter Code')
                        else:
                            main_Footer.set(
                                'Invalid Code enter Valid Code')

                Frame_Add_Return_Book.pack_forget()
            else:
                import os
                ans = tmsg.askokcancel(
                    'Login Error', "You have no permission to use this function in Guest mode\nfor permission Login in our Central Library\nPress 'OK' for Login")

                if ans == TRUE:
                    Restart_Login()
        while True:
            if num_for_Avai_book == 0:
                Frame_Book_Available1.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 1:
                Frame_Book_Available2.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 2:
                Frame_Book_Available3.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 3:
                Frame_Book_Available4.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 4:
                Frame_Book_Available5.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 5:
                Frame_Book_Available6.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 6:
                Frame_Book_Available7.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 7:
                Frame_Book_Available8.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 8:
                Frame_Book_Available9.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 9:
                Frame_Book_Available10.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 10:
                Frame_Book_Available11.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 11:
                Frame_Book_Available12.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 12:
                Frame_Book_Available13.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 13:
                Frame_Book_Available14.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 14:
                Frame_Book_Available15.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 15:
                Frame_Book_Available16.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 16:
                Frame_Book_Available17.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 17:
                Frame_Book_Available18.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 18:
                Frame_Book_Available19.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Avai_book == 19:
                Frame_Book_Available20.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_Book_Available10.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        while True:
            if num_for_history == 0:
                Frame_history1.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 1:
                Frame_history2.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 2:
                Frame_history3.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 3:
                Frame_history4.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 4:
                Frame_history5.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 5:
                Frame_history6.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 6:
                Frame_history7.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 7:
                Frame_history8.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 8:
                Frame_history9.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 9:
                Frame_history10.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 10:
                Frame_history11.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 11:
                Frame_history12.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 12:
                Frame_history13.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 13:
                Frame_history14.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 14:
                Frame_history15.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 15:
                Frame_history16.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 16:
                Frame_history17.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 17:
                Frame_history18.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_history == 18:
                Frame_history19.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_history == 19:
                Frame_history20.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_history20.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        while True:
            if num_for_Borrow_book == 0:
                Frame_Borrow_Book1.pack(fill=BOTH,side=TOP)
                l2 = Label(Frame_Borrow_Book1, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book1, text='\n\nEnter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book1, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book1, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book1, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)

                break

            elif num_for_Borrow_book == 1:
                Frame_Borrow_Book2.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book2, text='Borrow Book',
                           anchor="w", font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book2, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book2, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book2, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book2, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 2:
                Frame_Borrow_Book3.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book3, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book3, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book3, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book3, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book3, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 3:
                Frame_Borrow_Book4.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book4, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book4, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book4, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book4, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book4, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 4:
                Frame_Borrow_Book5.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book5, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book5, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book5, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book5, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book5, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 5:
                Frame_Borrow_Book6.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book6, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book6, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book6, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book6, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book6, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 6:
                Frame_Borrow_Book7.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book7, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book7, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book7, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book7, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book7, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 7:
                Frame_Borrow_Book8.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book8, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book8, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book8, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book8, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book8, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 8:
                Frame_Borrow_Book9.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book9, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book9, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book9, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book9, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book9, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break

            elif num_for_Borrow_book == 9:
                Frame_Borrow_Book10.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book10, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book10, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book10, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book10, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book10, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 10:
                Frame_Borrow_Book11.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book11, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book11, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book11, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book11, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book11, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 11:
                Frame_Borrow_Book12.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book12, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book12, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book12, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book12, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book12, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 12:
                Frame_Borrow_Book13.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book13, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book13, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book13, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book13, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book13, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 13:
                Frame_Borrow_Book14.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book14, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book14, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book14, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book14, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book14, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 14:
                Frame_Borrow_Book15.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book15, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book15, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book15, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book15, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book15, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 15:
                Frame_Borrow_Book16.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book16, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book16, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book16, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book16, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book16, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 16:
                Frame_Borrow_Book17.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book17, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book17, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book17, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book17, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book17, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                break
            elif num_for_Borrow_book == 17:
                Frame_Borrow_Book18.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book18, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book18, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book18, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book18, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book18, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Borrow_book == 18:
                Frame_Borrow_Book19.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book19, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book19, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book19, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book19, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book19, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Borrow_book == 19:
                Frame_Borrow_Book20.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book20, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book20, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book20, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book20, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book20, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                main_Footer.set(
                    'you used app for more time please Restart App')
                break

            else:
                Frame_Borrow_Book20.pack(fill=BOTH)
                l2 = Label(Frame_Borrow_Book20, text='Borrow Book', anchor="w",
                           font="Fraunces 11 bold")
                l2.pack(pady=10, padx=5, fill=X)

                Exit2 = Button(l2, padx=4, relief=FLAT, cursor='hand2',
                               bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                Exit2.pack(side=RIGHT)

                Label(Frame_Borrow_Book20, text='Enter Code of Book',
                      bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

                Enter_2_value = IntVar()
                Enter_2_value.set("")
                Enter_Code = Entry(Frame_Borrow_Book20, textvar=Enter_2_value,
                                   font="Poppins 20 bold")
                Enter_Code.pack(pady=10, padx=320, fill=X)

                Enter_Btn = Button(Frame_Borrow_Book20, text='Borrow Book',
                                   font="Poppins 10 bold", command=Borrow_Book, pady="10")
                Enter_Btn.pack(pady=0, padx=320, fill=X)

                for i in range(15):
                    Label(Frame_Borrow_Book20, text="", font="100",
                          bg='#1e1e1e').pack(fill=BOTH)
                main_Footer.set(
                    'you used app for more time please Restart App')
                break

    def Add_Return_Book():
        global num_for_Avai_book
        global num_for_Borrow_book
        global num_for_history

        main_Footer.set('')

        def ReturnBook():

            if Entry_email_username_value.get() != 'Login Now':
                main_Footer.set('')

                if Enter_name.get() == "":

                    main_Footer.set('Enter Book Name')
                else:
                    for i in Books.keys():
                        i = i
                    i = int(i)
                    Books[i+1] = Enter_name.get()

                    main_Footer.set(
                        f'Thanks for Return book "{Enter_name.get()}"')
                    Save_History('Book Return', Enter_name.get())
                    Enter_1_value.set('')
            else:
                import os
                ans = tmsg.askokcancel(
                    'Login Error', "You have no permission to use this function in Guest mode\nfor permission Login in our Central Library\nPress 'OK' for Login")

                if ans == TRUE:
                    Restart_Login()

        Frame_Add_Return_Book.pack_forget()

        while True:
            if num_for_Avai_book == 0:
                Frame_Book_Available1.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 1:
                Frame_Book_Available2.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 2:
                Frame_Book_Available3.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 3:
                Frame_Book_Available4.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 4:
                Frame_Book_Available5.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 5:
                Frame_Book_Available6.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 6:
                Frame_Book_Available7.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 7:
                Frame_Book_Available8.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 8:
                Frame_Book_Available9.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break

            elif num_for_Avai_book == 9:
                Frame_Book_Available10.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 10:
                Frame_Book_Available11.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 11:
                Frame_Book_Available12.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 12:
                Frame_Book_Available13.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 13:
                Frame_Book_Available14.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 14:
                Frame_Book_Available15.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 15:
                Frame_Book_Available16.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 16:
                Frame_Book_Available17.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                break
            elif num_for_Avai_book == 17:
                Frame_Book_Available18.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Avai_book == 18:
                Frame_Book_Available19.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Avai_book == 19:
                Frame_Book_Available20.pack_forget()
                num_for_Avai_book = num_for_Avai_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_Book_Available10.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        while True:
            if num_for_Borrow_book == 0:
                Frame_Borrow_Book1.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 1:
                Frame_Borrow_Book2.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 2:
                Frame_Borrow_Book3.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 3:
                Frame_Borrow_Book4.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 4:
                Frame_Borrow_Book5.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 5:
                Frame_Borrow_Book6.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 6:
                Frame_Borrow_Book7.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 7:
                Frame_Borrow_Book8.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 8:
                Frame_Borrow_Book9.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 9:
                Frame_Borrow_Book10.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 10:
                Frame_Borrow_Book11.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 11:
                Frame_Borrow_Book12.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 12:
                Frame_Borrow_Book13.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 13:
                Frame_Borrow_Book14.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 14:
                Frame_Borrow_Book15.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 15:
                Frame_Borrow_Book16.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 16:
                Frame_Borrow_Book17.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                break
            elif num_for_Borrow_book == 17:
                Frame_Borrow_Book18.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Borrow_book == 18:
                Frame_Borrow_Book19.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_Borrow_book == 19:
                Frame_Borrow_Book20.pack_forget()
                num_for_Borrow_book = num_for_Borrow_book + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_Borrow_Book20.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        while True:
            if num_for_history == 0:
                Frame_history1.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 1:
                Frame_history2.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 2:
                Frame_history3.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 3:
                Frame_history4.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 4:
                Frame_history5.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 5:
                Frame_history6.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 6:
                Frame_history7.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 7:
                Frame_history8.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 8:
                Frame_history9.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 9:
                Frame_history10.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 10:
                Frame_history11.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 11:
                Frame_history12.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 12:
                Frame_history13.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 13:
                Frame_history14.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 14:
                Frame_history15.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 15:
                Frame_history16.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 16:
                Frame_history17.pack_forget()
                num_for_history = num_for_history + 1
                break
            elif num_for_history == 17:
                Frame_history18.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_history == 18:
                Frame_history19.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            elif num_for_history == 19:
                Frame_history20.pack_forget()
                num_for_history = num_for_history + 1
                main_Footer.set(
                    'you used app for more time please Restart App')
                break
            else:
                Frame_history20.pack_forget()

                main_Footer.set(
                    'you used app for more time please Restart App')
                break

        Frame_Add_Return_Book.pack(fill=BOTH)
        l3 = Label(Frame_Add_Return_Book, text='Return Book', anchor="w",
                   font="Fraunces 11 bold")
        l3.pack(pady=10, padx=5, fill=X)

        Exit3 = Button(l3, padx=4, relief=FLAT, cursor='hand2',
                       bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
        Exit3.pack(side=RIGHT)

        Label(Frame_Add_Return_Book, text='\n\nEnter Name of Book',
              bg='#1e1e1e', fg='white', font="15").pack(side=TOP, pady=0, padx=320, fill=X)

        Enter_1_value = StringVar()
        Enter_1_value.set("")
        Enter_name = Entry(Frame_Add_Return_Book, textvar=Enter_1_value,
                           font="Poppins 20 bold")
        Enter_name.pack(side=TOP, fill=X, padx=320, pady=10)

        Enter_Btn = Button(Frame_Add_Return_Book, text='Return Book',
                           font="Poppins 10 bold", command=ReturnBook, pady=10)
        Enter_Btn.pack(pady=0, padx=320, fill=X)

        for i in range(15):
            Label(Frame_Add_Return_Book, text="",
                  font="100", bg='#1e1e1e').pack(fill=BOTH)

    def History():
        global num_for_Avai_book
        global num_for_Borrow_book
        global num_for_history

        if Entry_email_username_value.get() != 'Login Now':

            while True:
                if num_for_Avai_book == 0:
                    Frame_Book_Available1.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 1:
                    Frame_Book_Available2.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 2:
                    Frame_Book_Available3.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 3:
                    Frame_Book_Available4.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 4:
                    Frame_Book_Available5.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 5:
                    Frame_Book_Available6.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 6:
                    Frame_Book_Available7.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 7:
                    Frame_Book_Available8.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 8:
                    Frame_Book_Available9.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break

                elif num_for_Avai_book == 9:
                    Frame_Book_Available10.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 10:
                    Frame_Book_Available11.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 11:
                    Frame_Book_Available12.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 12:
                    Frame_Book_Available13.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 13:
                    Frame_Book_Available14.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 14:
                    Frame_Book_Available15.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 15:
                    Frame_Book_Available16.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 16:
                    Frame_Book_Available17.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    break
                elif num_for_Avai_book == 17:
                    Frame_Book_Available18.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break
                elif num_for_Avai_book == 18:
                    Frame_Book_Available19.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break
                elif num_for_Avai_book == 19:
                    Frame_Book_Available20.pack_forget()
                    num_for_Avai_book = num_for_Avai_book + 1
                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break
                else:
                    Frame_Book_Available20.pack_forget()

                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break

            while True:
                if num_for_Borrow_book == 0:
                    Frame_Borrow_Book1.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 1:
                    Frame_Borrow_Book2.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 2:
                    Frame_Borrow_Book3.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 3:
                    Frame_Borrow_Book4.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 4:
                    Frame_Borrow_Book5.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 5:
                    Frame_Borrow_Book6.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 6:
                    Frame_Borrow_Book7.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 7:
                    Frame_Borrow_Book8.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 8:
                    Frame_Borrow_Book9.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 9:
                    Frame_Borrow_Book10.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break

                elif num_for_Borrow_book == 10:
                    Frame_Borrow_Book11.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 11:
                    Frame_Borrow_Book12.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 12:
                    Frame_Borrow_Book13.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 13:
                    Frame_Borrow_Book14.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 14:
                    Frame_Borrow_Book15.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 15:
                    Frame_Borrow_Book16.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 16:
                    Frame_Borrow_Book17.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    break
                elif num_for_Borrow_book == 17:
                    Frame_Borrow_Book18.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break
                elif num_for_Borrow_book == 18:
                    Frame_Borrow_Book19.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break
                elif num_for_Borrow_book == 19:
                    Frame_Borrow_Book20.pack_forget()
                    num_for_Borrow_book = num_for_Borrow_book + 1
                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break
                else:
                    Frame_Borrow_Book20.pack_forget()

                    main_Footer.set(
                        'you used app for more time please Restart App')
                    break

            while True:
                if num_for_history == 0:
                    Frame_history1.pack(fill=BOTH)
                    l4 = Label(Frame_history1, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history1)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history1, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)
                    Data.close()

                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 1:
                    Frame_history2.pack(fill=BOTH)
                    l4 = Label(Frame_history2, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history2)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history2, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)
                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 2:
                    Frame_history3.pack(fill=BOTH)
                    l4 = Label(Frame_history3, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history3)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history3, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 3:
                    Frame_history4.pack(fill=BOTH)
                    l4 = Label(Frame_history4, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history4)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history4, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 4:
                    Frame_history5.pack(fill=BOTH)
                    l4 = Label(Frame_history5, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history5)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history5, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 5:
                    Frame_history6.pack(fill=BOTH)
                    l4 = Label(Frame_history6, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history6)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history6, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 6:
                    Frame_history7.pack(fill=BOTH)
                    l4 = Label(Frame_history7, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history7)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history7, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 7:
                    Frame_history8.pack(fill=BOTH)
                    l4 = Label(Frame_history8, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history8)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history8, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 8:
                    Frame_history9.pack(fill=BOTH)
                    l4 = Label(Frame_history9, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history9)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history9, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 9:
                    Frame_history10.pack(fill=BOTH)
                    l4 = Label(Frame_history10, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history10)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history10, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 10:
                    Frame_history11.pack(fill=BOTH)
                    l4 = Label(Frame_history11, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history11)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history11, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 11:
                    Frame_history12.pack(fill=BOTH)
                    l4 = Label(Frame_history12, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history12)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history12, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 12:
                    Frame_history13.pack(fill=BOTH)
                    l4 = Label(Frame_history13, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history13)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history13, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 13:
                    Frame_history14.pack(fill=BOTH)
                    l4 = Label(Frame_history14, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history14)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history14, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 14:
                    Frame_history15.pack(fill=BOTH)
                    l4 = Label(Frame_history15, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history15)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history15, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 15:
                    Frame_history16.pack(fill=BOTH)
                    l4 = Label(Frame_history16, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history16)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history16, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 16:
                    Frame_history17.pack(fill=BOTH)
                    l4 = Label(Frame_history17, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history17)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history17, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 17:
                    Frame_history18.pack(fill=BOTH)
                    l4 = Label(Frame_history18, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history18)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history18, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 18:
                    Frame_history19.pack(fill=BOTH)
                    l4 = Label(Frame_history19, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history19)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history19, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                elif num_for_history == 19:
                    Frame_history20.pack(fill=BOTH)
                    l4 = Label(Frame_history20, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history20)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history20, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
                else:
                    Frame_history20.pack(fill=BOTH)
                    l4 = Label(Frame_history20, text='History', anchor="w",
                               font="Fraunces 11 bold")
                    l4.pack(pady=10, padx=5, fill=X)

                    Exit4 = Button(l4, padx=4, relief=FLAT, cursor='hand2',
                                   bg="gray", fg="black", text="Exit Library", command=Exit_TK, activebackground="gray")
                    Exit4.pack(side=RIGHT)

                    SB = Scrollbar(Frame_history20)
                    SB.pack(side=RIGHT, fill=Y)

                    LB = Listbox(Frame_history20, yscrollcommand=SB.set,
                                 height=100, font="20", bg='gray90')
                    Data = open("Data/Data.py", 'r')

                    for line in Data:
                        LB.insert(END, line)

                    Data.close()
                    LB.pack(fill=X, padx=5)

                    SB.config(command=LB.yview)
                    break
        else:
            import os
            ans = tmsg.askokcancel(
                'Login Error', "You have no permission to use this function in Guest mode\nfor permission Login in our Central Library\nPress 'OK' for Login")

            if ans == TRUE:
                Restart_Login()
    # Frames
    f3 = Frame(Root, bg="#333333")
    f3.pack(side=TOP, fill=X)

    f4 = Frame(Root, bg="purple")
    f4.pack(side=BOTTOM, fill=X)

    f1 = Frame(Root, bg="#333333")
    f1.pack(side=LEFT, fill=Y)

    f5_m = Frame(Root, height=25, bg="#1e1e1e")
    f5_m.pack(fill=X)

    f5 = Frame(f5_m, bg="#1e1e1e", height=25)
    f5.pack(fill=X)

    f2 = Frame(Root, bg="#252526")
    f2.pack(side=LEFT, fill=Y)

    menubar = Menu(Root)
    m1 = Menu(menubar, tearoff=0,  background='#333333', foreground='white',
              activebackground='#004c99', activeforeground='white')
    m1.add_command(label='⪢ Check Available Books', command=Available_Books)
    m1.add_command(label='⪢ Borrow Books', command=Book_Borrow)
    m1.add_command(label='⪢ Add/Return Books', command=Add_Return_Book)
    m1.add_command(label='⪢ History', command=History)
    m1.add_command(label='')
    m1.add_command(label='⪢ Profile')
    m1.add_command(label='⪢ Logout',command=Exit_TK)
    menubar.add_cascade(label='Options', menu=m1)

    m1 = Menu(menubar, tearoff=0,  background='#333333', foreground='white',
              activebackground='#004c99', activeforeground='white')
    m1.add_command(label='⪢ Fees per Month')
    m1.add_command(label='⪢ Pay per Book')
    m1.add_command(label='⪢ Renew Library License(Staff only)')
    m1.add_command(label='⪢ Fine(for Damage Book)')
    menubar.add_cascade(label='Fine', menu=m1)

    m1 = Menu(menubar, tearoff=0,  background='#333333', foreground='white',
              activebackground='#004c99', activeforeground='white')
    m1.add_command(label='⪢ Change Themes')
    m1.add_command(label='⪢ Change font')
    m1.add_command(label='⪢ Setting')
    m1.add_command(label='⪢ Edit Api')

    menubar.add_cascade(label='Edit', menu=m1)

    m1 = Menu(menubar, tearoff=0,  background='#333333', foreground='white',
              activebackground='#004c99', activeforeground='white')
    m1.add_command(label='⪢ Welcome')
    m1.add_command(label='⪢ About Library')
    m1.add_command(label='⪢ Library License')
    m1.add_command(label='⪢ ##')
    menubar.add_cascade(label='Help', menu=m1)
    Root.config(menu=menubar)

    m1 = Menu(menubar, tearoff=0,  background='#333333', foreground='white',
              activebackground='#004c99', activeforeground='white')
    m1.add_command(label='⪢ Email us')
    m1.add_command(label='⪢ Chatbox Querry')
    m1.add_command(label='⪢ Contact our call cantre')
    m1.add_command(label='⪢ Feedbck')
    menubar.add_cascade(label='Contact', menu=m1)
    Root.config(menu=menubar)
    #top header f3
    LH = Label(f3, text="Welcome To Central Library",
               fg="White", font="Lobster 12 ", bg='#333333')

    photo = Image.open("Icons/logo.png")
    render = ImageTk.PhotoImage(photo)
    Logo =Label(f3, image=render, cursor='hand2',  bg="#333333",
                relief=FLAT, fg='#42a5f5', padx=10, pady=10, activebackground="#333333")
    Logo.image = render
    Logo.pack(padx=5,side=LEFT)
    


    # Frame 5 (Header2)
    l1 = Label(f5, text="  EXPLORER                                     ･･･",
               fg="White", font="Lobster 9 ", bg='#1e1e1e')
    l1.pack(side=LEFT)
    l2 = Label(f5, text="Welcome To Central Library",
               fg="White", font="Lobster 12 ", bg='#1e1e1e')
    l2.pack(fill=Y)

    # Frame 4 (Footer)

    photo = Image.open("Icons/notification.png")
    render = ImageTk.PhotoImage(photo)
    B8 =Button(f4, image=render, cursor='hand2',  bg="purple",
                relief=FLAT, fg='#42a5f5', padx=10, pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(padx=5,side=RIGHT)
    
    photo = Image.open("Icons/message.png")     
    render = ImageTk.PhotoImage(photo)
    B8 =Button(f4, image=render, cursor='hand2',  bg="purple",
                relief=FLAT, fg='#42a5f5', padx=10, pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(padx=5,side=RIGHT)

    photo = Image.open("Icons/phone.png")
    render = ImageTk.PhotoImage(photo)
    B8 =Button(f4, image=render, cursor='hand2',  bg="purple",
                relief=FLAT, fg='#42a5f5', padx=10, pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(padx=5,side=RIGHT)




    main_Footer = StringVar()
    main_Footer.set('Choose Your Choice')
    Label(f4, textvar=main_Footer, fg='white', bg='purple').pack()
    

    # main Frame
    # Available Books

    Frame_Book_Available1 = Frame(bg="#1e1e1e")
    Frame_Book_Available1.pack()

    Frame_Book_Available2 = Frame(bg="#1e1e1e")
    Frame_Book_Available2.pack()

    Frame_Book_Available3 = Frame(bg="#1e1e1e")
    Frame_Book_Available3.pack()

    Frame_Book_Available4 = Frame(bg="#1e1e1e")
    Frame_Book_Available4.pack()

    Frame_Book_Available5 = Frame(bg="#1e1e1e")
    Frame_Book_Available5.pack()

    Frame_Book_Available6 = Frame(bg="#1e1e1e")
    Frame_Book_Available6.pack()

    Frame_Book_Available7 = Frame(bg="#1e1e1e")
    Frame_Book_Available7.pack()

    Frame_Book_Available8 = Frame(bg="#1e1e1e")
    Frame_Book_Available8.pack()

    Frame_Book_Available9 = Frame(bg="#1e1e1e")
    Frame_Book_Available9.pack()

    Frame_Book_Available10 = Frame(bg="#1e1e1e")
    Frame_Book_Available10.pack()

    Frame_Book_Available11 = Frame(bg="#1e1e1e")
    Frame_Book_Available11.pack()

    Frame_Book_Available12 = Frame(bg="#1e1e1e")
    Frame_Book_Available12.pack()

    Frame_Book_Available13 = Frame(bg="#1e1e1e")
    Frame_Book_Available13.pack()

    Frame_Book_Available14 = Frame(bg="#1e1e1e")
    Frame_Book_Available14.pack()

    Frame_Book_Available15 = Frame(bg="#1e1e1e")
    Frame_Book_Available15.pack()

    Frame_Book_Available16 = Frame(bg="#1e1e1e")
    Frame_Book_Available16.pack()

    Frame_Book_Available17 = Frame(bg="#1e1e1e")
    Frame_Book_Available17.pack()

    Frame_Book_Available18 = Frame(bg="#1e1e1e")
    Frame_Book_Available18.pack()

    Frame_Book_Available19 = Frame(bg="#1e1e1e")
    Frame_Book_Available19.pack()

    Frame_Book_Available20 = Frame(bg="#1e1e1e")
    Frame_Book_Available20.pack()

    # Data History
    # History

    Frame_history1 = Frame(bg="#1e1e1e")
    Frame_history1.pack(fill=BOTH)

    Frame_history2 = Frame(bg="#1e1e1e")
    Frame_history2.pack()

    Frame_history3 = Frame(bg="#1e1e1e")
    Frame_history3.pack()

    Frame_history4 = Frame(bg="#1e1e1e")
    Frame_history4.pack()

    Frame_history5 = Frame(bg="#1e1e1e")
    Frame_history5.pack()

    Frame_history6 = Frame(bg="#1e1e1e")
    Frame_history6.pack()

    Frame_history7 = Frame(bg="#1e1e1e")
    Frame_history7.pack()

    Frame_history8 = Frame(bg="#1e1e1e")
    Frame_history8.pack()

    Frame_history9 = Frame(bg="#1e1e1e")
    Frame_history9.pack()

    Frame_history10 = Frame(bg="#1e1e1e")
    Frame_history10.pack()

    Frame_history11 = Frame(bg="#1e1e1e")
    Frame_history11.pack()

    Frame_history12 = Frame(bg="#1e1e1e")
    Frame_history12.pack()

    Frame_history13 = Frame(bg="#1e1e1e")
    Frame_history13.pack()

    Frame_history14 = Frame(bg="#1e1e1e")
    Frame_history14.pack()

    Frame_history15 = Frame(bg="#1e1e1e")
    Frame_history15.pack()

    Frame_history16 = Frame(bg="#1e1e1e")
    Frame_history16.pack()

    Frame_history17 = Frame(bg="#1e1e1e")
    Frame_history17.pack()

    Frame_history18 = Frame(bg="#1e1e1e")
    Frame_history18.pack()

    Frame_history19 = Frame(bg="#1e1e1e")
    Frame_history19.pack()

    Frame_history20 = Frame(bg="#1e1e1e")
    Frame_history20.pack()

    # Book Borrow
    Frame_Borrow_Book1 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book1.pack()

    Frame_Borrow_Book2 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book2.pack()

    Frame_Borrow_Book3 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book3.pack()

    Frame_Borrow_Book4 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book4.pack()

    Frame_Borrow_Book5 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book5.pack()

    Frame_Borrow_Book6 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book6.pack()

    Frame_Borrow_Book7 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book7.pack()

    Frame_Borrow_Book8 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book8.pack()

    Frame_Borrow_Book9 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book9.pack()

    Frame_Borrow_Book10 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book10.pack()

    Frame_Borrow_Book11 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book11.pack()

    Frame_Borrow_Book12 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book12.pack()

    Frame_Borrow_Book13 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book13.pack()

    Frame_Borrow_Book14 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book14.pack()

    Frame_Borrow_Book15 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book15.pack()

    Frame_Borrow_Book16 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book16.pack()

    Frame_Borrow_Book17 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book17.pack()

    Frame_Borrow_Book18 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book18.pack()

    Frame_Borrow_Book19 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book19.pack()

    Frame_Borrow_Book20 = Frame(Root, bg="#1e1e1e")
    Frame_Borrow_Book20.pack()

    # Add Books
    Frame_Add_Return_Book = Frame(Root, bg="#1e1e1e")
    Frame_Add_Return_Book.pack()

    fmain = Frame(Root, bg="#1e1e1e")
    fmain.pack(fill=BOTH)

    def Binds_f2(key):
        def on_leave(event):
            key['bg'] = '#252526'
            key['fg'] = 'azure'

        def on_enter(event):

            key['background'] = '#2a2d2e'
            key['fg'] = 'yellow'

        key.bind('<Enter>', on_enter)
        key.bind('<Leave>', on_leave)

    # Buttons

    B1 = Button(f2, padx=4, anchor="w", relief=FLAT, cursor='hand2',
                bg="#252526", fg="azure", text=" ⪢ Check Available Books\t\t", command=Available_Books, activebackground="#2a2d2e")
    B1.pack(anchor="nw", fill=X)

    B2 = Button(f2, padx=4, anchor="w", relief=FLAT, cursor='hand2',
                bg="#252526", fg="azure",  text=" ⪢ Borrow Books", command=Book_Borrow, activebackground="#2a2d2e")
    B2.pack(anchor="nw", fill=X)

    B3 = Button(f2, padx=4, anchor="w", relief=FLAT, cursor='hand2',
                bg="#252526", fg="azure",  text=" ⪢ Add/Return Books", command=Add_Return_Book, activebackground="#2a2d2e")
    B3.pack(anchor="nw", fill=X)

    B5 = Button(f2, padx=4, anchor="w", relief=FLAT, cursor='hand2',
                bg="#252526", fg="azure",  text=" ⪢ History", command=History, activebackground="#2a2d2e")
    B5.pack(anchor="nw", fill=X)

    B4 = Button(f2, padx=4, relief=FLAT, cursor='hand2',
                bg="#252526", fg="azure", text=" ⪢ Exit Library ⪡", command=Exit_TK, activebackground="#2a2d2e")
    B4.pack(anchor="s", fill=X, side=BOTTOM)


    Binds_f2(B1)
    Binds_f2(B2)
    Binds_f2(B3)
    Binds_f2(B4)
    Binds_f2(B5)

    def Binds_f1(key):
        def on_leave(event):
            key['bg'] = '#333333'
            key['fg'] = '#42a5f5'

        def on_enter(event):

            key['background'] = '#252526'
            key['fg'] = 'white'

        key.bind('<Enter>', on_enter)
        key.bind('<Leave>', on_leave)

    def HISO():
        global count
        if count % 2 == 0:
            def Hide():
                f2.pack_forget()
                f5.pack_forget()
                LH.pack()
            Hide()
            count = count+1
        else:
            def Show():
                f2.pack_forget()
                f5.pack(side=LEFT, fill=Y)
                TOP_FRAME()
                l1.pack_forget()
                l2.pack_forget()
                LH.pack()

            Show()
            count = count+1

    def FUSH():

        global count
        if count % 2 == 0:

            def Full_screen():
                width = Root.winfo_screenwidth()

                height = Root.winfo_screenheight()

                Root.geometry('%dx%d' % (width, height))
            Full_screen()
            count = count+1
        else:

            def Short_screen():
                Root.geometry('1001x555')
            Short_screen()
            count = count+1

    # Frame Button

    hideshow = Image.open("Icons/hide.png")
    render = ImageTk.PhotoImage(hideshow)
    B6 = Button(f1, image=render, command=HISO, cursor='hand2',  bg="#333333",
                relief=FLAT, fg='#42a5f5', activebackground="#333340",padx=10,pady=10)
    B6.image = render
    B6.pack(fill=X,padx=5,pady=5)
    Binds_f1(B6)

    fulscr = Image.open("Icons/fulscr.png")
    render = ImageTk.PhotoImage(fulscr)
    B8 = Button(f1, image=render, command=FUSH, cursor='hand2',  bg="#333333",
                relief=FLAT, fg='#42a5f5',padx=10,pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(fill=X,padx=5,pady=5)
    Binds_f1(B8)

    photo = Image.open("Icons/search.png")
    render = ImageTk.PhotoImage(photo)
    B8 =Label(f1, image=render,  cursor='hand2',  bg="#333333",
                relief=FLAT, fg='#42a5f5', padx=10,pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(fill=X,padx=5,pady=5)
    Binds_f1(B8)

    photo = Image.open("Icons/user_alt.png")
    render = ImageTk.PhotoImage(photo)
    B8 =Label(f1, image=render, cursor='hand2',  bg="#333333",
                relief=FLAT, fg='#42a5f5',padx=10,pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(fill=X,padx=5,pady=5, side=BOTTOM)
    Binds_f1(B8)

    photo = Image.open("Icons/gear.png")
    render = ImageTk.PhotoImage(photo)
    B8 =Label(f1, image=render, cursor='hand2',  bg="#333333",
                relief=FLAT, fg='#42a5f5', padx=10,pady=10, activebackground="#333333")
    B8.image = render
    B8.pack(fill=X, side=BOTTOM,pady=5,padx=5)
    Binds_f1(B8)



    a = Entry_email_username_value.get()
    if a == '':

        load = Image.open("Icons/User.png")
        render = ImageTk.PhotoImage(load)
        img_User = Button(f3,  text='Guest',image=render, relief=FLAT,
                          bg='white', activebackground="white",compound=LEFT)
        img_User.image = render
        img_User.pack(side=RIGHT, anchor='e')

        import os
        ans = tmsg.askokcancel(
            'Login Error', "You have no permission to use this function in Guest mode\nfor permission Login in our Central Library\nPress 'OK' for Login")

        if ans == TRUE:
            Restart_Login()

    else:
        load = Image.open("Icons/User.png")
        render = ImageTk.PhotoImage(load)
        img_User = Button(f3, image=render, text=a,relief=FLAT,
                          bg='white', activebackground="white",compound=LEFT)
        img_User.image = render
        img_User.pack(side=RIGHT, anchor='e')

    Guest_Count = Guest_Count + 1

Guest_Btn = Button(Frame_Bottom, text="Guest", bg='steelblue3',
                   command=Main_Screen, cursor='hand2', activebackground="steelblue3")
Guest_Btn.pack(pady=5, padx=20, side=LEFT)

#Network Connection
a = connect()
if a == False:
    Error = tmsg.showerror('Network problem',"You have not connected to internet \nPlease Conect to internet")

Root.mainloop()
#Made By Ayush shete  #First year student fo Ramdeobaba College of Engineering and Management 