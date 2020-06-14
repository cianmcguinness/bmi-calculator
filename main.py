from User import User

user = User()

user.set_name(str(input("Enter your name: ")))

if user.is_metric:
    user.set_weight_metric(float(input("Enter your weight (kg): ")))
    user.set_height_metric(float(input("Enter your height (cm): ")))
else:
    user.set_height_imperial(float(input("Enter your height in feet: ")), float(input("Enter your height in inches: ")))
    user.set_weight_imperial(float(input("Enter your weight in stone: ")),
                             float(input("Enter your weight in pounds: ")))

if user.is_metric:
    print("Your weight in stone: " + str(user.weight_stone))
    print("Your weight in pounds: " + str(user.weight_pounds))
    print("Your height in feet: " + str(user.height_foot))
    print("Your height in inches: " + str(user.height_inches))
else:
    print("Your weight in KG: " + str(user.weight_kg))
    print("Your height in cm: " + str(user.height_cm))

user.get_bmi()

user.print_bmi()
