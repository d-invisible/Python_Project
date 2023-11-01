# Import libraries
from tkinter import *
import pyttsx3

# Initialize window
root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title('DataFlair - TEXT_TO_SPEECH')

# Heading
Label(root, text='TEXT TO SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='DataFlair', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

# Label
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

# Text variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

# Define functions
def Text_to_speech():
    Message = entry_field.get()
    engine = pyttsx3.init()
    engine.say(Message)
    engine.runAndWait()

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Buttons
Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset).place(x=175, y=140)

# Infinite loop to run the program
root.mainloop()
