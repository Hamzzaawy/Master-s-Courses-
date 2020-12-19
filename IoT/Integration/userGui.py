import tkinter 
from tkinter import *
import tkinter.font as tkFont



def UserPage(username, meetings ):

    root = tkinter.Tk()

    fontStyle_1 = tkFont.Font(family="Lucida Grande", size=20)
    fontStyle_2 = tkFont.Font(family="Lucida Grande", size=10)

    root.title("Hello!")

    root.resizable(width="false", height="false")

    root.minsize(width=1000, height=600)


    Welcome = tkinter.Label(root, text="Welcome" + " " + username, font = fontStyle_1)
    Welcome.place(relx = 0.5,  rely = 0.11, anchor = 'center')

    email = tkinter.Label(root, text="email - > kod.iot2020@gmail.com", font = fontStyle_2)
    email.place(relx = 0.05,  rely = 0.2)

    TargetEmail = tkinter.Label(root, text="Tar.email - > EmailList@comapny.com", font = fontStyle_2)
    TargetEmail.place(relx = 0.05,  rely = 0.235)

    edit_button = tkinter.Button(root, text="edit")
    edit_button.place(relx = 0.12,  rely = 0.27)

    CurrentTemp = tkinter.Label(root, text="Current Temperature        25", font = fontStyle_2)
    CurrentTemp.place(relx = 0.4,  rely = 0.2)

    DesiredTemp = tkinter.Label(root, text="Desired Temperature", font = fontStyle_2)
    DesiredTemp.place(relx = 0.4,  rely = 0.235)

    temp_entry = tkinter.Entry(root, width = 5)
    temp_entry.place(relx = 0.57,  rely = 0.235)

    Apply_button = tkinter.Button(root, text="Apply")
    Apply_button.place(relx = 0.45,  rely = 0.27)



    LightDimm = tkinter.Label(root, text="Current light dimming ration        70%", font = fontStyle_2)
    LightDimm.place(relx = 0.7,  rely = 0.2)

    DesiredDimm = tkinter.Label(root, text="Desired light dimming ratio ", font = fontStyle_2)
    DesiredDimm.place(relx = 0.7,  rely = 0.235)

    temp_entry = tkinter.Entry(root, width = 5)
    temp_entry.place(relx = 0.9,  rely = 0.235)

    Apply_button = tkinter.Button(root, text="Apply")
    Apply_button.place(relx = 0.77,  rely = 0.27)

    Schedule = tkinter.Label(root, text="Today' Schedule", font = ('Arial', 14))
    Schedule.place(relx = 0.43,  rely = 0.38)



    Time_1 = tkinter.Label(root, text="Time", font = ('Arial', 14))
    Time_1.place (relx = 0.1,  rely = 0.5)

    X_1 = tkinter.Label(root, text="08:00", font = ('Arial', 14))
    X_1.place(relx = 0.1,  rely = 0.6)

    X_2 = tkinter.Label(root, text="09:00", font = ('Arial', 14))
    X_2.place(relx = 0.1,  rely = 0.68)

    X_3 = tkinter.Label(root, text="10:00", font = ('Arial', 14))
    X_3.place(relx = 0.1,  rely = 0.76)

    X_4 = tkinter.Label(root, text="11:00", font = ('Arial', 14))
    X_4.place(relx = 0.1,  rely = 0.84)

    Meeting_1 = tkinter.Label(root, text="Meeting", font = ('Arial', 14))
    Meeting_1.place (relx = 0.23,  rely = 0.5)

    Y_1 = tkinter.Label(root, text=meetings[0], font = ('Arial', 14))
    Y_1.place(relx = 0.23,  rely = 0.6)

    Y_2 = tkinter.Label(root, text=meetings[1], font = ('Arial', 14))
    Y_2.place(relx = 0.23,  rely = 0.68)

    Y_3 = tkinter.Label(root, text=meetings[2], font = ('Arial', 14))
    Y_3.place(relx = 0.23,  rely = 0.76)

    Y_4 = tkinter.Label(root, text=meetings[3], font = ('Arial', 14))
    Y_4.place(relx = 0.23,  rely = 0.84)


    Time_2 = tkinter.Label(root, text="Time", font = ('Arial', 14))
    Time_2.place (relx = 0.6,  rely = 0.5)

    X_5 = tkinter.Label(root, text="13:00", font = ('Arial', 14))
    X_5.place(relx = 0.6,  rely = 0.6)

    X_6 = tkinter.Label(root, text="14:00", font = ('Arial', 14))
    X_6.place(relx = 0.6,  rely = 0.68)

    X_7 = tkinter.Label(root, text="15:00", font = ('Arial', 14))
    X_7.place(relx = 0.6,  rely = 0.76)

    X_8 = tkinter.Label(root, text="16:00", font = ('Arial', 14))
    X_8.place(relx = 0.6,  rely = 0.84)

    Meeting_2 = tkinter.Label(root, text="Meeting", font = ('Arial', 14))
    Meeting_2.place (relx = 0.73,  rely = 0.5)

    Y_5 = tkinter.Label(root, text=meetings[5], font = ('Arial', 14))
    Y_5.place(relx = 0.73,  rely = 0.6)

    Y_6 = tkinter.Label(root, text=meetings[6], font = ('Arial', 14))
    Y_6.place(relx = 0.73,  rely = 0.68)

    Y_7 = tkinter.Label(root, text=meetings[7], font = ('Arial', 14))
    Y_7.place(relx = 0.73,  rely = 0.76)

    Y_8 = tkinter.Label(root, text=meetings[8], font = ('Arial', 14))
    Y_8.place(relx = 0.73,  rely = 0.84)


    root.mainloop()