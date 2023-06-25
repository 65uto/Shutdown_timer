import customtkinter as ctk
import tkinter as tk
from tkinter import *
import datetime as dt
from time import strftime
from datetime import datetime
import time
from datetime import *
import os

#ctk.set_appearance_mode("dark")

# Function
def clock():
    time = strftime('%H : %M : %S')
    Digi_Clock.configure(text=time)
    Digi_Clock.after(1000, clock)
    try:
        next_hour, next_minut, next_second = str(nextTime_label.cget('text')).split(':')
        #hour, minut, second = str(time).split(':')
        h, m, s = time.split(' :')
        if (int(h)==int(next_hour) and int(m)==int(next_minut) and int(s)==int(next_second)):
            print('shutdown')
            os.system('shutdown -r')
        
    except :
        a = 1
        
def next_time():
    time = (combobox.get()).split('นาที')
    time = int(time[0])
    
    hour, mins = divmod(time, 60)
    sec = strftime('%S')
    # Time
    text = str(hour) + ':' + str(mins) + ':' + str(sec)
    time_label.configure(text=text)
    
    # Next time for shutdown
    next_hour = int(strftime('%H')) + hour
    next_minute = (divmod(int(strftime('%M')) + mins, 60))[1]
    if next_minute >= 60:
        next_minute = (divmod(next_minute, 60))[0]
        next_hour = (divmod(next_minute), 60)[1] + next_hour
    if len(str(next_minute)) == 1:
        next_minute = '0'+str(next_minute)

    day, next_hour = divmod(next_hour, 24)
    
    if len(str(next_hour)) == 1 :
        next_hour = '0'+str(next_hour)
    
    next_second = strftime('%S')
    
    if day > 0:
        text = str(day) + 'วัน' + ' ' + str(next_hour) + ':' + str(next_minute) + ':' + str(next_second)
    else:   
        text = str(next_hour) + ':' + str(next_minute) + ':' + str(next_second)

    nextTime_label.configure(text=text)


def cancel():
    time_label.configure(text=' ')
    nextTime_label.configure(text=' ')
    os.system('shutdown -a')
"""---------------------------------------------------------------------------"""
 
app = ctk.CTk()
app.title('Shutdown timer')
app.geometry('400x200')

Digi_Clock = ctk.CTkLabel(
                     app, text="",
                     font=('Arial', 25),
                     pady=10,
                     corner_radius=20,
                     fg_color="#7DFAB6"
                          )

Digi_Clock.pack()

time_label = ctk.CTkLabel(app, text='')
time_label.pack()
nextTime_label = ctk.CTkLabel(app, text='')
nextTime_label.pack()

# Combobox for selecting time
combobox_var = ctk.StringVar(value="0")
combobox = ctk.CTkComboBox(master=app,
                                     values=['5 นาที', '10 นาที',
                                             '15 นาที', '30 นาที',
                                             '60 นาที', '90 นาที',
                                             '120 นาที', '180 นาที',
                                             '240 นาที'],
                                     variable=combobox_var)
combobox.pack(padx=20, pady=10)

# Button
enter_button = ctk.CTkButton(app, text="Enter", command=next_time).pack()
cancel_button = ctk.CTkButton(app, text="Cancel", command=cancel).pack()


# call function
clock()

app.mainloop()
