from tkinter import *
from tkinter import font
import time

global hours_numberr
global minutes_numberr
global sceonds_numberr
seconds =0
min = 0
hou = 0
stopp = True
#creating start mehtod that is used to count the time...that displayed in the window..
def start():
    global masterr
    global hours_numberr
    global minutes_numberr
    global sceonds_numberr
    global seconds,min,hou
    global stopp
    if stopp == True:
        seconds += 1
    if seconds == 59:
        min += 1
        seconds = 0
    if min == 60:
        hou += 1
        min = 0
    sceonds_numberr.config(text=seconds)
    minutes_numberr.config(text=min)
    hours_numberr.config(text=hou)
    masterr.after(1000,start)


#method to stop count down ..
def stop():
    global stopp
    stopp = False

#method to reset the hours,seconds,minutes and set to 0.
def restart():
    global hours_numberr
    global minutes_numberr
    global sceonds_numberr
    global seconds,min,hou
    global stopp
    hours_numberr.config(text="00")
    minutes_numberr.config(text="00")
    sceonds_numberr.config(text="00")
    seconds,min,hou = 0,0,0
    stopp = True


#creating main method that will displays the all the widgets..
def main():
    global masterr
    #window creation
    global hours_numberr
    global minutes_numberr
    global sceonds_numberr
    masterr = Tk()
    masterr.title("Stop Watch")
    masterr.geometry("700x350+100+100")
    masterr.config(bg="#2c313c")
    masterr.resizable(False,False)
    #heading for masterr window
    main_headingg=Label(masterr,text="Counter Clock",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="#2c313c")
    main_headingg.pack()
    #creating frame for main window
    parentt = Frame(masterr,bg='#2c313c')
    parentt.pack()
    #creating widgets
    #creating number icons for displaying time..
    hours_numberr = Label(parentt,text="00",pady=10,padx=10,fg="#fff",bg="#b871ce",font=font.Font(family="times new roman",size=50),height=2,width=3)
    hours_numberr.grid(row =0,column=0,padx=10,pady=10)
    minutes_numberr = Label(parentt,text="00",pady=10,padx=10,bg="#599bd3",fg="#fff",font=font.Font(family="times new roman",size=50),height=2,width=3)
    minutes_numberr.grid(row=0,column=1,padx=10,pady=10)
    sceonds_numberr = Label(parentt,text="00",pady=10,padx=10,bg="#98c379",fg="#fff",font=font.Font(family="times new roman",size=50),height=2,width=3)
    sceonds_numberr.grid(row=0,column=2,padx=10,pady=10)
    #creating number text for what it displays
    hours_textt = Label(parentt,text="Hours",pady=10,padx=10,bg="#b871ce",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
    hours_textt.grid(row=1,column=0,padx=10,pady=10)
    minutes_textt = Label(parentt,text ="Minutes",pady=10,padx=10,bg="#599bd3",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
    minutes_textt.grid(row=1,column=1,padx=10,pady=10)
    seconds_textt = Label(parentt,text="Seconds",pady=10,padx=10,bg="#98c379",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
    seconds_textt.grid(row=1,column=2,padx=10,pady=10)
    #creating another frame for buttonss like start,stop,reset..
    #creating another frame like child to parentt or main frame..
    buttonss = Frame(masterr,bg="#2c313c")
    buttonss.pack(side=BOTTOM)
    #creating buttonss for buttonss frame..
    start_buttonn=Button(buttonss,text="Start",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="#98c379",bd=0,width=10,command=start)
    start_buttonn.grid(row=0,column=0,padx=5)
    stop_buttonn=Button(buttonss,text="Stop",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="silver",bd=0,width=10,command=stop)
    stop_buttonn.grid(row=0,column=1,padx=5)
    reset_buttonn=Button(buttonss,text="Reset",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="#599bd3",bd=0,width=10,command=restart)
    reset_buttonn.grid(row=0,column=2,padx=5)
    parentt.mainloop()

if __name__ == "__main__":
    main()
