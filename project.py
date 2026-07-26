from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timers=None
rep=0

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

background=PhotoImage(file='tomato.png')
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=background)
time=canvas.create_text(100,130,text="00:00",fill="white",font=('Arial',30,'bold'))
canvas.grid(column=2,row=2)

# <-------------------------------StartTimer-------------------------------------->

def timestart():
    global rep
    rep +=1
    
    if rep%8==0:
        stopwatch(LONG_BREAK_MIN*60)
        display.config(text="Break",font=('Arial',40),fg=PINK)
    elif rep%2==0:
        stopwatch(SHORT_BREAK_MIN*60)
        display.config(text="Break",font=('Arial',40),fg=RED)
    else:
        stopwatch(WORK_MIN*60)
        display.config(text="Work",font=('Arial',40),fg=GREEN)
    
# <-------------------------------TimerMekanism-------------------------------------->
       
def stopwatch(macho):
    minutes= macho // 60
    seconds=macho % 60
                
    canvas.itemconfig(time,text=f"{minutes:02}:{seconds:02}")
            
    if minutes>0:
        global timers
        timers=window.after(1000,stopwatch,macho-1)
    else:
        timestart()
        count=""
        for a in range(rep//2):
            count +="✔"
        howmany.config(text=count)
        
# <-------------------------------RestTimer-------------------------------------->

def timereset():
    global rep
    rep=0
    window.after_cancel(timers)
    canvas.itemconfig(time,text="00:00")
    display.config(text="Timer")
    howmany.config(text="")
    
display=Label(text="Timer",font=('Arial',40),bg=YELLOW,fg=GREEN)
display.grid(column=2,row=1)

start=Button(text="Start",font=('Arial',20),command=timestart)
start.grid(column=1,row=3)

reset=Button(text="Reset",font=('Arial',20),command=timereset)
reset.grid(column=3,row=3)

howmany=Label(text="",font=('Arial',20),bg=YELLOW,fg=GREEN)
howmany.grid(column=2,row=4)

window.mainloop()