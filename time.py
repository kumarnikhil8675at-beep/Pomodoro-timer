import tkinter as tk

window = tk.Tk()
window.title("Stopwatch")

time = 0
running = False

label = tk.Label(window, text="00:00", font=("Arial", 30))
label.pack(pady=20)


def start():
    global running

    if not running:
        running = True
        update_time()


def update_time():
    global time

    if running:
        time += 1

        minutes = time // 60
        seconds = time % 60

        label.config(text=f"{minutes:02}:{seconds:02}")

        window.after(1000, update_time)


def stop():
    global running
    running = False


def reset():
    global time, running

    running = False
    time = 0
    label.config(text="00:00")


tk.Button(window, text="Start", command=start).pack()
tk.Button(window, text="Stop", command=stop).pack()
tk.Button(window, text="Reset", command=reset).pack()

window.mainloop()