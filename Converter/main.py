from view import View
from model import Model

def perform_conversion():
    try:
        selected_conversion = view.get_selected_conversion(event=None)
        value = view.get_input()
        result = 0.0
        match selected_conversion:
            case ("Miles/Kilometers"):
                result = model.convert_miles_to_km(miles=value)
            case ("Kilometers/Miles"):
                result = model.convert_km_to_miles(km=value)
            case ("Inches/Centimeters"):
                result = model.convert_inches_to_cm(inches=value)
            case ("Centimeters/Inches"):
                result = model.convert_cm_to_inches(cm=value)
            case ("Feet/Meters"):
                result = model.convert_feet_to_m(feet=value)
            case ("Meters/Feet"):
                result = model.convert_m_to_feet(m=value)
            case ("Yards/Meters"):
                result = model.convert_yards_to_m(yards=value)
            case ("Meters/Yards"):
                result = model.convert_m_to_yards(m=value)
        view.set_result(round(result, ndigits=4))
    except ValueError:
        view.value_error()


def update_labels(event):
    view.reset_conversion()
    selected_conversion = view.get_selected_conversion(event=None)
    unites = selected_conversion.split("/")
    view.set_convert_unit_label(label=unites[0])
    view.set_convert_to_unit_label(label=unites[1])

view = View()
model = Model()

# Configuration des actions
view.combobox.bind("<<ComboboxSelected>>", update_labels)
view.convert(command=perform_conversion)

view.window.mainloop()
