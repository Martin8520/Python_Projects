from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#416D19"
YELLOW = "#FFF67E"
BUTTON_COLOR = "#F72798"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(long_break_sec)
    elif REPS % 2 == 0:
        countdown(short_break_sec)
    else:
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")

canvas = Canvas(width=200, height=224, bg="black", highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), highlightthickness=0, bg=YELLOW)
timer.grid(row=0, column=1)

check = Label(text="✔", fg=GREEN, font="bold", bg=YELLOW)
check.grid(row=3, column=1)

start = Button(text="START", bg=BUTTON_COLOR, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="RESET", bg=BUTTON_COLOR, font=(FONT_NAME, 15, "bold"), highlightthickness=0)
reset.grid(row=2, column=2)
window.mainloop()
