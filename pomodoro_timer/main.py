import tkinter
from PIL import Image, ImageTk
import os
import random
import math

def set_bg():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'Assets')
    images = os.listdir(images_dir)
    index = random.randint(0, len(images) - 1)
    image_path = os.path.join(images_dir, images[index])
    image = Image.open(image_path)
    return ImageTk.PhotoImage(image)

def work_or_break():
    text = canvas.itemcget(work_break, "text")
    if text == "Start Working?" or "Break Time!":
        text = canvas.itemconfig(work_break, text="Work Time!", font=(FONT_NAME, 65, "italic" ), fill="white")
        
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Kozuka Mincho Pro"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps 
    window.after_cancel(my_timer)
    reps = 0
    canvas.itemconfig(timer, text="00:00", font=(FONT_NAME, 100, "bold"), fill="white")
    canvas.itemconfig(work_break, text="Start Working?", font=(FONT_NAME, 65, "italic" ), fill="white")
    canvas.itemconfig(check_mark, text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 8:
        count_down(long_break_sec)
        reps = 0
        canvas.itemconfig(check_mark, text="")

    elif reps % 2 == 0:
        work_or_break()
        count_down(short_break_sec)
        canvas.itemconfig(work_break, text="Break Time!", font=(FONT_NAME, 65, "italic" ), fill="white")
    
    else:
        work_or_break()
        count_down(work_sec)
         

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    time_min = math.floor(count / 60)
    time_sec = count % 60 

    if time_sec < 10:
        time_sec = f"0{time_sec}"


    canvas.itemconfig(timer, text=f"{time_min}:{time_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        play()
        canvas.itemconfig(check_mark, text=canvas.itemcget(check_mark, "text") + "✔")

# ---------------------------- UI SETUP ------------------------------- #
# pygame.init()
# pygame.mixer.init()

window = tkinter.Tk()
window.geometry("1920x1080")
window.attributes("-type", "tkinter.TOPLEVEL")

canvas = tkinter.Canvas(window, width=1920, height=1080)
canvas.place(x=0, y=0)
backgroud = set_bg()
canvas.create_image( 0, 0, anchor=tkinter.NW, image=backgroud)

timer = canvas.create_text(960, 540, text="00:00", font=(FONT_NAME, 100, "bold"), fill="white")
work_break = canvas.create_text(960, 320, text="Start Working?", font=(FONT_NAME, 65, "italic" ), fill="white")


canvas.create_text(960, 140, text="Pomodoro", font=(FONT_NAME, 50 ), fill="white")

start_button = tkinter.Button(canvas, text="Start", font=(FONT_NAME, 25, "bold"), bg="black", fg="white", highlightthickness=0, command=start_timer)
start_button.place(x=690, y=700)

reset_button = tkinter.Button(canvas, text="Reset", font=(FONT_NAME, 25, "bold"), bg="black", fg="white", highlightthickness=0, command=reset)
reset_button.place(x=1100, y=700)

check_mark = canvas.create_text(960, 850, text="", fill="green2", font=(FONT_NAME, 50, "bold"))


window.update()
window.mainloop()
