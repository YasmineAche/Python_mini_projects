from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from typing import Literal

FONT = ("Arial", 14, "bold")
PINK = "#F9DFDF"

class View:
    def __init__(self):
        self.window = Tk()
        self.configure_window()

        self.canvas = Canvas()
        self.image = PhotoImage(file="logo.png")
        self.configure_canvas()

        self.website_label = Label()
        self.email_username_label = Label()
        self.password_label = Label()
        self.website_input = Entry()
        self.email_username_input = Entry()
        self.password_input = Entry()
        self.generate_password_button = Button()
        self.add_button = Button()
        self.configure_widgets()

        self.center_window()

    def configure_window(self) -> None:
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, background=PINK)

    def center_window(self) -> None:
        self.window.update_idletasks() # Update window to calculate its actual size

        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"+{x}+{y}")

    def configure_canvas(self) -> None:
        self.canvas.config(background=PINK, highlightthickness=0, width=200, height=200)
        self.canvas.create_image(100, 100, image=self.image)
        self.canvas.grid(column=1, row=0)

    def configure_widgets(self) -> None:
        # Labels
        self.website_label.config(text="Website Link:", font=FONT, background=PINK, foreground="black")
        self.website_label.grid(column=0, row=1, pady=2)

        self.email_username_label.config(text="Email/Username:", font=FONT, background=PINK, foreground="black")
        self.email_username_label.grid(column=0, row=2, pady=2)

        self.password_label.config(text="Password:", font=FONT, background=PINK, foreground="black")
        self.password_label.grid(column=0, row=3, pady=2)

        # Entries
        self.website_input.config(background="white", highlightthickness=0, width=36, foreground="black")
        self.website_input.grid(column=1, row=1, columnspan=2, pady=2)
        self.focus_cursor()

        self.email_username_input.config(background="white", highlightthickness=0, width=36, foreground="black")
        self.email_username_input.insert(index=0, string="@gmail.com")
        self.email_username_input.grid(column=1, row=2, columnspan=2, pady=2)

        self.password_input.config(background="white", highlightthickness=0, width=20, foreground="black")
        self.password_input.grid(column=1, row=3, pady=2)

        # Buttons
        self.generate_password_button.config(text="Generate Password", font=FONT, width=14, highlightthickness=0, highlightbackground=PINK)
        self.generate_password_button.grid(column=2, row=3, pady=2)

        self.add_button.config(text="Add", font=FONT, width=38, highlightthickness=0, highlightbackground=PINK)
        self.add_button.grid(column=1, row=4, columnspan=2, pady=2)

    def get_user_input(self) -> tuple[str, str, str]:
        website = self.website_input.get()
        email_username = self.email_username_input.get()
        password = self.password_input.get()
        return website, email_username, password

    def add_to_file(self, save_data:str) -> None:
        self.add_button.config(command=save_data)

    def init_inputs(self) -> None:
        self.website_input.delete(first=0, last=END)
        self.email_username_input.delete(first=0, last=END)
        self.email_username_input.insert(index=0, string="@gmail.com")
        self.password_input.delete(first=0, last=END)

    def focus_cursor(self) -> None:
        self.website_input.focus()

    def focus_window(self) -> None:
        self.window.focus_force()

    @staticmethod
    def show_messagebox(message:str, type_of_messagebox:Literal["confirmation", "error"]) -> bool | None:
        if type_of_messagebox == "confirmation":
            return messagebox.askyesno(title="Confirmation", message="Are you sure you want to save this data?", detail=message, icon="question")
        elif type_of_messagebox == "error":
            messagebox.showerror(title="Error", message=message, icon="error")
        return None

    @staticmethod
    def get_number_of_characters() -> int:
        return simpledialog.askinteger(title="Password", prompt="Enter the number of characters you wish your password to have: ", minvalue=0, initialvalue=8)

    def generate_password_click(self, command) -> None:
        self.generate_password_button.config(command=command)

    def set_password(self, password:str) -> None:
        self.password_input.delete(first=0, last=END)
        self.password_input.insert(0, password)

    def loop(self) -> None:
        self.window.mainloop()