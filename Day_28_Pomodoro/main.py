from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Pomodoro Time Schedule
    # 25min Work    (1st rep) - work
    # 5min Break    (2nd rep) - short break
    # 25min Work    (3rd rep) - work
    # 5min Break    (4th rep) - short break
    # 25min Work    (5th rep) - work
    # 5min Break    (6th rep) - short break
    # 25min Work    (7th rep) - work
    # 20min Break   (8th rep) - long break

    # If 8th rep (long break)
    if reps % 8 == 0:
        timer_header.config(text="Break", fg=RED)
        count_down(long_break_sec)

    # If 2nd/4th/6th reps (short break)
    elif reps % 2 == 0:
        timer_header.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        
    # If 1st/3rd/5th/7th reps (work)
    else:
        timer_header.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Make the second display 2 digits
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Header Label
timer_header = Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 50))
timer_header.grid(column=1, row=0)

# Create tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# To make tomato be in center of canvas (half the coordinates in canvas)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Buttons
start_btn = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 18), command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 18))
reset_btn.grid(column=2, row=2)

# Pomodoro Ticks
ticks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(24))
ticks.grid(column=1, row=3)

window.mainloop()