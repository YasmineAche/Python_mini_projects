from tkinter import *
from typing import Literal

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
PINK = "#e2979c"
RED = "#e7305b"
PADDING_X = 100
PADDING_Y = 50

class View:
    def __init__(self):
        self.window = Tk()
        self.set_window()

        self.canvas = Canvas()
        self.tomato_img = PhotoImage(file="tomato.png")
        self.timer_text = ""
        self.set_canvas()

        self.start_button = Button()
        self.reset_button = Button()
        self.title_label = Label()
        self.check_marks_label = Label()
        self.set_buttons_labels()

        self.center_window()

    def set_window(self) -> None:
        self.window.title("Pomodoro")
        self.window.config(padx=PADDING_X, pady=PADDING_Y, background=YELLOW)

    def center_window(self):
        self.window.update_idletasks() # Update window to calculate its actual size

        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"+{x}+{y}")

    def set_canvas(self) -> None:
        self.canvas.config(width=200, height=224, background=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 140, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

    def set_buttons_labels(self) -> None:
        self.start_button.config(text="Start", font=(FONT_NAME, 20, "bold"), width=4, highlightthickness=0, borderwidth=0)
        self.start_button.grid(row=2, column=0)

        self.reset_button.config(text="Reset", font=(FONT_NAME, 20, "bold"), width=4, highlightthickness=0, borderwidth=0)
        self.reset_button.grid(row=2, column=2)

        self.title_label.config(text="Timer", font=(FONT_NAME, 45, "bold"), foreground=GREEN, background=YELLOW)
        self.title_label.grid(row=0, column=1)

        self.check_marks_label.config(font=(FONT_NAME, 20, "bold"), foreground=GREEN, background=YELLOW)
        self.check_marks_label.grid(row=3, column=1)

    def start_timer(self, command) -> None:
        self.start_button.config(command=command)

    def disable_activate_start_button(self, state: Literal["normal", "active", "disabled"]) -> None:
        self.start_button.config(state=state)

    def update_timer_text(self, time:str) -> None:
        self.canvas.itemconfig(tagOrId=self.timer_text, text=time)

    def update_title_text(self, text:str) -> None:
        if text == "Short Break":
            self.title_label.config(text="Break", foreground=PINK)
        elif text == "Long Break":
            self.title_label.config(text="Break", foreground=RED)
        else:
            self.title_label.config(text=text, foreground=GREEN)

    def update_check_marks_text(self, text:str) -> None:
        self.check_marks_label.config(text=text)

    def reset_timer(self, command) -> None:
        self.reset_button.config(command=command)