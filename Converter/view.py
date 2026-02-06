from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

FONT = ("Arial", 20)
LIST_OF_CONVERSIONS = ["Miles/Kilometers", "Kilometers/Miles", "Inches/Centimeters", "Centimeters/Inches",
          "Feet/Meters", "Meters/Feet", "Yards/Meters", "Meters/Yards"
          ]
WINDOW_WIDTH = 380
WINDOW_HEIGHT = 300

class View:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window.title("Converter")
        self.window.config(padx=20, pady=5)
        self.center_window()

        self.button = Button(font=FONT, text="Convert")
        self.button.grid(column=1, row=3, pady=20)

        self.input = Entry(width=10, font=FONT)
        self.input.grid(column=0, row=1, pady=20)

        self.result_label = Label(text="0", font=FONT)
        self.result_label.grid(column=0, row=2, pady=20)

        self.convert_unit_label = Label(text="Miles", font=FONT)
        self.convert_unit_label.grid(column=1, row=1, pady=20)

        self.convert_to_unit_label = Label(text="Kilometers", font=FONT)
        self.convert_to_unit_label.grid(column=1, row=2, padx=20, pady=20)

        self.combobox = Combobox(font=FONT, values=LIST_OF_CONVERSIONS, width=15)
        self.combobox.grid(column=0, row=0, pady=20)
        self.combobox.current(0)

    def center_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))

        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

    def get_input(self):
        return float(self.input.get().replace(",", "."))

    def set_result(self, result):
        self.result_label.config(text=str(result))

    def set_convert_unit_label(self, label):
        self.convert_unit_label.config(text=label)

    def set_convert_to_unit_label(self, label):
        self.convert_to_unit_label.config(text=label)

    def get_selected_conversion(self, event):
        selection = self.combobox.get()
        return selection

    def convert(self, command):
        self.button.config(command=command)

    @staticmethod
    def value_error():
        messagebox.showerror(title="Error", message="Please enter a valid value")

    def reset_conversion(self):
        self.result_label.config(text="0")
        self.input.delete(0, END)