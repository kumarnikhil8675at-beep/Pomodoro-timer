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
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

background=PhotoImage(file='tomato.png')
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=background)
time=canvas.create_text(100,130,text="00:00",fill="white",font=('Arial',30,'bold'))
canvas.grid(column=2,row=2)

display=Label(text="Work",font=('Arial',40),bg=YELLOW,fg=GREEN)
display.grid(column=2,row=1)

finalbreak=0

def timestart():
    global finalbreak
    finalbreak +=1
    print(finalbreak)
    
    if finalbreak%8==0:
        stopwatch(20*60)
        display.config(text="Break",font=('Arial',40),fg=PINK)
    elif finalbreak%2==0:
        stopwatch(5*60)
        display.config(text="Break",font=('Arial',40),fg=RED)
    else:
        stopwatch(25*60)
        display.config(text="Work",font=('Arial',40),fg=GREEN)
        
def stopwatch(macho):
    
    minutes= macho // 60
    seconds=macho % 60
            
    canvas.itemconfig(time,text=f"{minutes:02}:{seconds:02}")
        
    if minutes>0:
        window.after(1,stopwatch,macho-1)
    else:
        timestart()
    
def timereset():
    global finalbreak

    # finalbreak=0
    # running=False
    canvas.itemconfig(time,text=f"00:00")
    howmany.config(text="")

start=Button(text="Start",font=('Arial',20),command=timestart)
start.grid(column=1,row=3)

reset=Button(text="Reset",font=('Arial',20),command=timereset)
reset.grid(column=3,row=3)

howmany=Label(text="",font=('Arial',20),bg=YELLOW,fg=GREEN)
howmany.grid(column=2,row=4)

window.mainloop()