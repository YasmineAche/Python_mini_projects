MILES_KM = 1.60934
INCHES_CM = 2.54
FEET_M = 0.3048
YARDS_M = 0.9144

class Model:

    def convert_miles_to_km(self, miles):
        return miles * MILES_KM

    def convert_km_to_miles(self, km):
        return km / MILES_KM

    def convert_inches_to_cm(self, inches):
        return inches * INCHES_CM

    def convert_cm_to_inches(self, cm):
        return cm / INCHES_CM

    def convert_feet_to_m(self, feet):
        return feet * FEET_M

    def convert_m_to_feet(self, m):
        return m / FEET_M

    def convert_yards_to_m(self, yards):
        return yards * YARDS_M

    def convert_m_to_yards(self, m):
        return m / YARDS_M