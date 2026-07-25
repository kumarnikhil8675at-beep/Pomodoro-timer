from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window=Tk()
# window.minsize(400,400)
window.title("Pomodoro")
window.

background=PhotoImage(file='tomato.png')
# bg=Label(image=background)
# bg.place(x=0, y=0, relwidth=1, relheight=1)

canvas=Canvas(width=200,height=224,bg=YELLOW)
canvas.create_image(100,112,image=background)
canvas.pack()

display=Label(text="Work",font=('Arial',40))
display.place(x=150,y=20)

watch=0
running=False
Work_time=True
finalbreak=0

def timestart():
    global watch,running
    
    if not running:
        running=True
        stopwatch()
        
def stopwatch():
    global watch,finalbreak,Work_time
    
    if running:
        watch +=1
        minutes= watch // 60
        seconds=watch % 60
            
        time.config(text=f"{minutes:02}:{seconds:02}")
        if minutes==25 and seconds==0 and Work_time==True:
            Work_time=False
            display.config(text="Break",font=('Arial',40))
            finalbreak +=1
            watch=0
        elif (minutes==5 or minutes==20) and seconds==0 and Work_time==False:
            if finalbreak==4:
                if minutes==20:
                    Work_time=True
                    finalbreak=0
                    display.config(text="Work",font=('Arial',40))
                    watch=0
            else:
                Work_time=True
                display.config(text="Work",font=('Arial',40))
                watch=0
            
        window.after(1000,stopwatch)
    
    
def timereset():
    global watch,running
    
    watch=0
    running=False
    
    time.config(text=f"00:00")
    
time=Label(text="00:00",font=('Arial',20))
time.place(x=160,y=200)

start=Button(text="Start",font=('Arial',20),command=timestart)
start.place(x=100,y=320)

reset=Button(text="Reset",font=('Arial',20),command=timereset)
reset.place(x=200,y=320)

window.mainloop()