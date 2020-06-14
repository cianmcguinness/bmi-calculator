class User:
    def __init__(self):
        self.name = ""

        self.is_metric = False

        self.weight_kg = float(0)
        self.weight_stone = int(0)
        self.weight_pounds = int(0)

        self.height_cm = int(0)
        self.height_foot = int(0)
        self.height_inches = int(0)

        self.bmi = float(0)

    def set_name(self, n):
        self.name = n

    def set_weight_metric(self, kg):
        self.weight_kg = kg
        self.convert_weight()

    def set_weight_imperial(self, stone, pounds):
        self.weight_stone = stone
        self.weight_pounds = pounds
        self.convert_weight()

    def set_height_metric(self, cm):
        self.height_cm = cm
        self.convert_height()

    def set_height_imperial(self, foot, inches):
        self.height_foot = foot
        self.height_inches = inches
        self.convert_height()

    def convert_weight(self):
        if self.is_metric:
            # convert kg to stone and pounds
            total_pounds = self.weight_kg * 2.205
            self.weight_stone = total_pounds // 14
            self.weight_pounds = total_pounds % 14
        else:
            # convert stone and pounds to kg
            total_pounds = (self.weight_stone * 14) + self.weight_pounds
            self.weight_kg = round(total_pounds / 2.205)

    def convert_height(self):
        if self.is_metric:
            # convert cm to feet and inches
            total_inches = round(self.height_cm / 2.54)
            self.height_foot = total_inches // 12
            self.height_inches = total_inches % 12
        else:
            # convert feet and inches to cm
            total_inches = (self.height_foot * 12) + self.height_inches
            self.height_cm = round(total_inches * 2.54)

    def get_bmi(self):
        if self.is_metric:
            # (Weight in Kilograms / (Height in Meters x Height in Meters))
            self.bmi = float(self.weight_kg / (float(self.height_cm / 100) * float(self.height_cm / 100)))
        else:
            # (Weight in Pounds / (Height in inches x Height in inches)) x 703
            self.bmi = (((self.weight_stone * 14) + self.weight_pounds) /
                        (((self.height_foot * 12) + self.height_inches) *
                         ((self.height_foot * 12) + self.height_inches)) * 703)

    def print_bmi(self):
        print("Hi " + self.name + "! Your BMI is: " + str(self.bmi) + ".")
