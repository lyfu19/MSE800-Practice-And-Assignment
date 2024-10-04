import tkinter as tk
from tkinter import PhotoImage
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
timer = None
is_paused = False
is_break = False
remaining_time = WORK_MIN * 60  # To store the remaining time for work session
work_sessions = 0  # Keep track of how many sessions have been completed

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global is_paused, is_break, timer, remaining_time, work_sessions
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    start_button.config(text="Start", state="normal")
    short_break_button.config(state="normal")
    long_break_button.config(state="normal")
    is_paused = False
    is_break = False
    remaining_time = WORK_MIN * 60  # Reset to 25 minutes
    work_sessions = 0  # Reset work session count
    canvas.itemconfig(timer_progress, extent=0)  # Reset progress bar
    timer = None

# ---------------------------- PAUSE AND CONTINUE ------------------------------- #
def pause_continue_timer():
    global is_paused, timer
    if is_paused:  # If paused, continue from the remaining time
        count_down(remaining_time)  # Resume countdown from the paused time
        start_button.config(text="Pause")
        is_paused = False
    else:  # If not paused, pause the countdown
        if timer:
            window.after_cancel(timer)  # Stop the current countdown
        start_button.config(text="Continue")
        is_paused = True

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global remaining_time, is_paused, is_break
    is_break = False  # Switch to work mode
    if is_paused:
        pause_continue_timer()  # If paused, continue the countdown
    else:
        remaining_time = WORK_MIN * 60  # Initialize for 25 minutes
        count_down(remaining_time)  # Start the countdown
        start_button.config(text="Pause")  # Change button text to Pause
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- SHORT BREAK ------------------------------- #
def short_break():
    global is_break, timer, remaining_time, is_paused
    is_break = True
    is_paused = False  # Reset pause state for a fresh break
    if timer:
        window.after_cancel(timer)  # Stop the current countdown
    remaining_time = SHORT_BREAK_MIN * 60  # Set 5 minutes for the short break
    count_down(remaining_time)  # Start the short break countdown
    title_label.config(text="Short Break", fg=PINK)
    start_button.config(text="Continue", state="normal")  # Display Continue
    short_break_button.config(state="disabled")
    long_break_button.config(state="normal")

# ---------------------------- LONG BREAK ------------------------------- #
def long_break():
    global is_break, timer, remaining_time, is_paused
    is_break = True
    is_paused = False  # Reset pause state for a fresh break
    if timer:
        window.after_cancel(timer)  # Stop the current countdown
    remaining_time = LONG_BREAK_MIN * 60  # Set 15 minutes for long break
    count_down(remaining_time)  # Start the long break countdown
    title_label.config(text="Long Break", fg=RED)
    start_button.config(text="Continue", state="normal")  # Display Continue
    short_break_button.config(state="normal")
    long_break_button.config(state="disabled")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global remaining_time, timer, is_paused, is_break, work_sessions
    remaining_time = count  # Save the remaining time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Update the progress circle dynamically
    total_time = WORK_MIN * 60 if not is_break else (SHORT_BREAK_MIN if remaining_time == SHORT_BREAK_MIN * 60 else LONG_BREAK_MIN) * 60
    progress = (total_time - count) / total_time * 360
    canvas.itemconfig(timer_progress, extent=progress)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Update every second
    else:
        if is_break:
            start_button.config(text="Start", state="normal")
        else:
            work_sessions += 1  # Increase the completed work sessions
            check_marks.config(text="✔" * work_sessions)  # Update the check marks
            start_button.config(text="Start", state="normal")

# ---------------------------- TASK ADDITION ------------------------------- #
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Title Label
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas for circular progress and timer display
canvas = tk.Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)

# Load the tomato image (user uploaded image)
tomato_img = PhotoImage(file="/Users/kevinhuang/Downloads/MSE800-Practice-and-Assignment/Week11_exercise/tomato.png")
canvas.create_image(150, 150, image=tomato_img)  # Place the image at the center of the canvas
timer_progress = canvas.create_arc(10, 10, 290, 290, start=90, extent=0, outline=PINK, width=5)  # Circular progress bar
timer_text = canvas.create_text(150, 150, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start/Pause/Continue Button
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer, font=("Arial", 12, "bold"))
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer, font=("Arial", 12, "bold"))
reset_button.grid(column=2, row=2)

# Short Break Button
short_break_button = tk.Button(text="Short Break", highlightthickness=0, command=short_break, font=("Arial", 12, "bold"))
short_break_button.grid(column=0, row=3)

# Long Break Button
long_break_button = tk.Button(text="Long Break", highlightthickness=0, command=long_break, font=("Arial", 12, "bold"))
long_break_button.grid(column=2, row=3)

# Check Marks
check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=("Arial", 15, "bold"))
check_marks.grid(column=1, row=4)

# Task Entry
task_entry = tk.Entry(width=40)
task_entry.grid(column=0, row=5, columnspan=2, pady=10)

# Add Task Button
add_task_button = tk.Button(text="Add Task", command=add_task, font=("Arial", 12, "bold"))
add_task_button.grid(column=2, row=5)

# Task Listbox
task_listbox = tk.Listbox(height=5, width=40)
task_listbox.grid(column=0, row=6, columnspan=3, pady=10)

window.mainloop()