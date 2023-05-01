import time
import datetime
from datetime import datetime
import tkinter as tk
from tkinter import *
from time import strftime
from tkinter import messagebox
from datetime import timedelta
import os

window = tk.Tk()
window.geometry('300x200')
window.config(bg='black')
window.resizable(False,False)

# ------------------------------------------------------------------ #
# -------------- Function -------------#
"""-----------------------------------------------------------------"""


""" digital clock function"""
def clock():
    time = strftime('%H : %M : %S')
    Ltime.config(text=time)
    Ltime.after(1000, clock)
    
""" timeCheckFunction """
def checkTime(H, M):
    current_time = datetime.now()
    print(H, M)
    time = current_time + timedelta(hours=H, minutes=M)
    N_H,N_M = time.hour, time.minute
    if len(str(N_M)) <= 1:
            N_M = '0' + str(N_M)
            L_Next_Min.config(text=N_M)
    L_Next_Hour.config(text=N_H)
    L_Next_Min.config(text=N_M)
    
    textSec = int(strftime('%S'))
    L_Next_Sec.config(text=textSec)
    
""" Cancel """
def cancel():
    hour = StringVar()
    hour.set("00")
    entryMin.config(textvariable=hour)
    
    LHour.config(text='0')
    LMin.config(text='00')
    
    L_Next_Hour.config(text='0')
    L_Next_Min.config(text='00')
    L_Next_Sec.config(text='00')
    
    os.system('shutdown -a')

""" Timer """
def timer():
    tH = int(strftime('%H'))
    tM = int(strftime('%M'))
    tS = int(strftime('%S'))
    
    Next_Hour = L_Next_Hour.cget("text")
    Next_Min = L_Next_Min.cget("text")
    Next_Sec = L_Next_Sec.cget("text")
    
    if ((tH == int(Next_Hour)) and (tM == int(Next_Min)) and (tS == int(Next_Sec))):
        os.system('shutdown /s /t 60')
        print("Stop")
    else:
        LMin.after(1000, timer)
    
""" Set Time Function """
def timeSet():
    textHour = 0
    textMin = str(entryMin.get())

    if textMin == '':
        Min = 0
        M = Min
        
    elif textMin != '':
        
        Min = int(textMin)
        if Min >= 60:
            Hour = int(Min // 60)
            H = Hour
            textHour = str(textHour + Hour)
            
            while Min >= 60:
                Min = int((Min - 60))
            M = Min
            textMin = str(Min)
            
            if len(textMin) <= 1:
                textMin = '0' + textMin
            else:   
                textMin = textMin
                
        elif Min < 60:
            Hour = Min // 60
            H = Hour
            textHour = str(int(textHour) + Hour)
            
            M = Min
            textMin = str(Min)
            
            if len(textMin) <= 1:
                textMin = '0' + textMin
                
            else:   
                textMin = textMin
                
    LHour.config(text=textHour)
    LMin.config(text=textMin)
    
    checkTime(H, M)
    #print(type(textHour), type(textMin))
# ------------------------------------------------------------------ #
                           #Display
hour = StringVar()
hour.set("00")
"""-----------------------------------------------------------------"""

""" Digital time display"""
Ltime = Label(window,
              text='',
              font=('Blackoak Std',20),
              background='black',
              foreground='green',
              )

""" Label Time"""

LHour = Label(window,text='0',
              font=(40),
              background='black',
              foreground='green')
LHour.place(x=115 ,y=35)

L = Label(window,
          text=':',font=(40),
          background='black',
          foreground='green')
L.place(x=145 ,y=35)

LMin = Label(window,
             text='00',
             font=(40),
             background='black',
             foreground='green')
LMin.place(x=165 ,y=35)

""" Input time"""
entryMin = Entry(window,
                width = 3,
                font=(40),
                bg='black',
                foreground='green',
             textvariable=hour)
entryMin.place(x=134 ,y=90)

""" Next time """
L_Next_Hour = Label(window,
                    text='0',
                    font=(40),
                    bg='black',
                    foreground='green')
L_Next_Hour.place(x=85, y=60)

L = Label(window,
          text=':',font=(40),
          background='black',
          foreground='green')
L.place(x=115 ,y=60)

L_Next_Min = Label(window,
             text='00',
             font=(40),
             background='black',
             foreground='green')
L_Next_Min.place(x=135 ,y=60)

L = Label(window,
          text=':',font=(40),
          background='black',
          foreground='green')
L.place(x=165 ,y=60)

L_Next_Sec = Label(window,
             text='00',
             font=(40),
             background='black',
             foreground='green')
L_Next_Sec.place(x=185 ,y=60)

""" Button """
timeSet = Button(window,text='Enter', command=timeSet).place(x=130 ,y=130)
cancel = Button(window,text='Cancel', command=cancel).place(x=125 ,y=160)

""" Display """
Ltime.place(x=80,y=5)
clock()
timer()

mainloop()
