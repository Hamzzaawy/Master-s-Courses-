from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
from facial_recog import RecognizeUser, RegisterNewUser
from sheets import readSheet,AppendData
from send_mail import Send_Mail
# from intgerate import Person
from userGui import UserPage

persons = {}

def main_account_screen():

    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("500x500") # set the configuration of GUI window 
    main_screen.title("Account") # set the title of GUI window
    main_screen.configure(background='white')

    fname="back.png"
    bg_image= tk.PhotoImage(file=fname)
    w = bg_image.width()
    h = bg_image.height()
    # size the window so the image will fill it
    main_screen.geometry("%dx%d+50+30" % (w, h))

    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')

    myFont = font.Font(family='Arial')
    
    # create Login Button 
    Button(cv, text="Login", height="1", width="15", font=myFont, bg="white", command=loading).place(x=150, y=280) 
 
    # create a register button
    Button(cv, text="Register", height="1", width="15", bg='DarkOrchid3', fg='white', font=myFont, command=register).place(x=150, y=200) 
 
    main_screen.mainloop() # start the GUI

    
def loading():
    global load_screen
    load_screen = Toplevel(main_screen)
    load_screen.title("...")
    load_screen.geometry("500x100")
    load_screen.configure(background="white")
    myFont = font.Font(family='Arial')
    Label(load_screen, text="", bg="white").pack()
    Label(load_screen, text="Initializing the face recognition...", bg="white", font=myFont).pack()
    load_screen.after(500, lambda: endLoad())
    def endLoad():
        state = RecognizeUser()
        load_screen.destroy()
        if state:
            Send_Mail()
            AppendData()
            UserPage("Hamza",readSheet())
            
        # print("Hello")
        
    
    
    


def register():
 
    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window. 
    #Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("500x500")
    register_screen.configure(background="white")
    myFont = font.Font(family='Arial')
        

    
    name_label = Label(register_screen, text="Name * ", font=myFont, bg = "white")
    name_label.pack()
 
    
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    name_entry = Entry(register_screen)
    name_entry.pack()
   
    
    emp_label = Label(register_screen, text="Employment ID * ", font=myFont, bg = "white")
    emp_label.pack()
    
    
    emp_entry = Entry(register_screen)
    emp_entry.pack()

    mail_label = Label(register_screen, text="Email * ", font=myFont, bg = "white")
    mail_label.pack()
    
    
    mail_entry = Entry(register_screen)
    mail_entry.pack()   

    comp_label = Label(register_screen, text="Company Name * ", font=myFont, bg = "white")
    comp_label.pack()
    
    
    comp_entry = Entry(register_screen)
    comp_entry.pack()
    
    corr_label = Label(register_screen, text="Corresponding Email * ", font=myFont, bg = "white")
    corr_label.pack()
    
    
    corr_entry = Entry(register_screen)
    corr_entry.pack()

    Label(register_screen,  text="", bg = "white").pack()
    
    # Set register button
    


    def setInfo(event):
        txt1 = name_entry.get()
        txt2 = mail_entry.get()
        txt3 = emp_entry.get()
        txt4 = comp_entry.get()
        txt5 = corr_entry.get()
        #name.append(txt1)
        #email.append(txt2)
        #employmentID.append(txt3)
        #companyName.append(txt4)
        #corrEmail.append(txt5)
        file = open("info.txt", "a")
        file.write("\n" + txt1 + "," + txt2 + "," + txt3 + "," + txt4 + "," + txt5)
        file.close()
        print("Hi")
        
    test = Button(register_screen, text="Next", width=10, height=1, bg="DarkOrchid3", fg="white", font=myFont, command=prepare)
    test.pack()
    test.bind("<ButtonRelease-1>", setInfo)

    # register_screen.bind("<ButtonRelease-1>", setInfo)
    
    
    
def prepare():
    prepare_screen = Toplevel(register_screen)
    prepare_screen.title("")
    prepare_screen.geometry("500x100")
    prepare_screen.configure(background="white")
    myFont = font.Font(family='Arial')
    Label(prepare_screen, text="Prepare yorself to take a photo.", font=myFont, bg = "white").pack()
    Label(prepare_screen,  text="", bg = "white").pack()

    def endPrepare():
        prepare_screen.destroy()
        # hello()
    
    Button(prepare_screen, text="OK", width=5, height=1, bg="DarkOrchid3", fg="white", font=myFont, command=endPrepare).pack()

    

    

main_account_screen() # call the main_account_screen() function
