class User:
    # User class is used in main program for creating a user object, assigning weight, height, name, and metric (bool)
    # values to it. get_bmi function in user class is used to calculate a BMI based on user class variables and return
    # bmi result

    def __init__(self):
        self.name = ""

        self.metric = True

        self.weight_kg = float(0)
        self.weight_stone = int(0)
        self.weight_pounds = int(0)

        self.height_cm = int(0)
        self.height_feet = int(0)
        self.height_inches = int(0)

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
        self.height_cm = int(round(cm))
        self.convert_height()

    def set_height_imperial(self, foot, inches):
        self.height_feet = int(round(foot))
        self.height_inches = int(round(inches))
        self.convert_height()

    def convert_weight(self):
        if self.metric:
            # convert kg to stone and pounds
            total_pounds = int(round(self.weight_kg * 2.205))
            self.weight_stone = int(total_pounds // 14)
            self.weight_pounds = int(total_pounds % 14)
        else:
            # convert stone and pounds to kg
            total_pounds = int(round((self.weight_stone * 14) + self.weight_pounds))
            self.weight_kg = round((total_pounds / 2.205), 2)

    def convert_height(self):
        if self.metric:
            # convert cm to feet and inches
            total_inches = int(round(self.height_cm / 2.54))
            self.height_feet = total_inches // 12
            self.height_inches = total_inches % 12
        else:
            # convert feet and inches to cm
            total_inches = (self.height_feet * 12) + self.height_inches
            self.height_cm = int(round(total_inches * 2.54))

    # calculates bmi and returns the result using different formula depending on metric or imperial
    def get_bmi(self):
        if self.metric:
            # (Weight in Kilograms / (Height in Meters x Height in Meters))
            result = round(
                float(self.weight_kg / (float(self.height_cm / 100) * float(self.height_cm / 100))), 1)
            return result
        else:
            # (Weight in Pounds / (Height in inches x Height in inches)) x 703
            result = round(
                (((self.weight_stone * 14) + self.weight_pounds) /
                 (((self.height_feet * 12) + self.height_inches) *
                  ((self.height_feet * 12) + self.height_inches)) * 703), 1)
            return result

    def get_name(self):
        return self.name

    def get_height_cm(self):
        return self.height_cm

    def get_weight_kg(self):
        return self.weight_kg

    def get_height_feet(self):
        return self.height_feet

    def get_height_inches(self):
        return self.height_inches

    def get_weight_stone(self):
        return self.weight_stone

    def get_weight_pounds(self):
        return self.weight_pounds

    def is_metric(self):
        return self.metric
