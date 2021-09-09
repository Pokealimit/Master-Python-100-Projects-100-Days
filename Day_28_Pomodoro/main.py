from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_btn = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 18))
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 18))
reset_btn.grid(column=2, row=2)

# Pomodoro Ticks
ticks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(24))
ticks.grid(column=1, row=3)

window.mainloop()