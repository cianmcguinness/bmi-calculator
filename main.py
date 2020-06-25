from user import User
from tkinter import *
import tkinter.messagebox
import csv
from datetime import datetime


class BMI:
    def __init__(self, r):
        self.root = r
        self.root.title("Body Mass Index")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='Gray')

        ################################################################################################################
        # Define variables
        ################################################################################################################

        name_input = StringVar()
        height_cm_input = StringVar()
        weight_kg_input = StringVar()
        height_feet_input = StringVar()
        height_inches_input = StringVar()
        weight_stone_input = StringVar()
        weight_pounds_input = StringVar()
        result_variable = DoubleVar()

        ################################################################################################################
        # Define Functions
        ################################################################################################################

        # Custom isdigit function that accepts floats and strings
        def is_digit(temp):
            try:
                float(temp)
                return True
            except ValueError:
                return False

        # reset function used for clearing text boxes and re initializing user variables and other variables
        def reset_function():
            if user.is_metric():
                name_input.set("")
                height_cm_input.set("")
                weight_kg_input.set("")
                result_variable.set(0)
                self.bmi_result_text.delete('1.0', END)
                self.user = 0
                self.user = User()
                self.export_button['state'] = 'disabled'
            else:
                name_input.set("")
                height_feet_input.set("")
                height_inches_input.set("")
                weight_stone_input.set("")
                weight_pounds_input.set("")
                result_variable.set(0)
                self.bmi_result_text.delete('1.0', END)
                self.user = 0
                self.user = User()
                self.export_button['state'] = 'disabled'
                self.height_inches_text['state'] = 'disabled'
                self.height_feet_text['state'] = 'disabled'
                self.weight_stone_text['state'] = 'disabled'
                self.weight_pounds_text['state'] = 'disabled'
                self.height_cm_text['state'] = 'normal'
                self.weight_kg_text['state'] = 'normal'

        # function used for exception handling and ensuring user inputs were valid. then setting weight and height
        # for user object and triggering the calculate_bmi function in user class
        def calculate_bmi():
            if user.is_metric():
                n = name_input.get()
                w = weight_kg_input.get()
                h = height_cm_input.get()

                if (is_digit(w) is False) or (is_digit(h) is False) or (w.strip() == "") or (h.strip() == ""):
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter valid height and weight")
                elif n.strip() == "":
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter a valid name.")
                elif (float(h) <= 0) or (float(h) > 250):
                    tkinter.messagebox.showwarning(title="Body Mass Index",
                                                   message="Height must be > 0 cm and <= 250 cm. "
                                                           "Enter a valid height and weight.")
                elif (float(w) <= 0) or (float(w) > 300 or w == ""):
                    tkinter.messagebox.showwarning(title="Body Mass Index",
                                                   message="Weight must be > 0 kg and <= 300 kg. "
                                                           "Enter a valid height and weight.")
                else:
                    user.set_name(n)
                    user.set_weight_metric(float(w))
                    user.set_height_metric(float(h))
                    result = user.get_bmi()
                    self.bmi_result_text.delete('1.0', END)
                    if result <= 50:
                        self.bmi_result_text.insert(END, str(result))
                        result_variable.set(result)
                        self.export_button['state'] = 'normal'
                    else:
                        result_variable.set(0)
                        tkinter.messagebox.showwarning(title="Body Mass Index", message="BMI result is too large. "
                                                                                        "Enter a valid height and "
                                                                                        "weight.")
            else:
                n = name_input.get()
                ws = weight_stone_input.get()
                wp = weight_pounds_input.get()
                hf = height_feet_input.get()
                hi = height_inches_input.get()

                if ws.strip() == "":
                    ws = "0"
                if wp.strip() == "":
                    wp = "0"
                if hf.strip() == "":
                    hf = "0"
                if hi.strip() == "":
                    hi = "0"

                if (ws == "0" and wp == "0") or (hf == "0" and hi == "0"):
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter valid height and weight")
                elif ((ws.isdigit() is False) or (wp.isdigit() is False) or (hf.isdigit() is False) or
                      (hi.isdigit() is False)):
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter valid height and weight")
                elif n.strip() == "":
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter valid name")
                elif (int(hf) < 0) or (int(hi) < 0) or (int(hf) > 8) or (int(hi) > 11):
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter valid height.\n\n0 - 8 "
                                                                                    "feet. 0 - 11 inches")
                elif (int(ws) < 0) or (int(wp) < 0) or (int(ws) > 50) or (int(wp) > 13):
                    tkinter.messagebox.showwarning(title="Body Mass Index", message="Enter valid weight.\n\n0 - 50 "
                                                                                    "stone. 0 - 13 pounds")
                else:
                    user.set_name(n)
                    user.set_weight_imperial(int(ws), int(wp))
                    user.set_height_imperial(int(hf), int(hi))
                    result = user.get_bmi()
                    if result <= 50:
                        self.bmi_result_text.insert(END, str(result))
                        result_variable.set(result)
                        self.export_button['state'] = 'normal'
                    else:
                        result_variable.set(0)
                        tkinter.messagebox.showwarning(title="Body Mass Index", message="BMI result is too large. "
                                                                                        "Enter a valid height and "
                                                                                        "weight.")

        # function used to change user object metric value and disable / enable certain text boxes
        def toggle_metric():
            if user.is_metric():
                user.metric = False
                height_cm_input.set("")
                weight_kg_input.set("")
                result_variable.set(0)
                self.bmi_result_text.delete('1.0', END)
                self.export_button['state'] = 'disabled'
                self.weight_kg_text['state'] = 'disabled'
                self.height_cm_text['state'] = 'disabled'
                self.weight_stone_text['state'] = 'normal'
                self.weight_pounds_text['state'] = 'normal'
                self.height_feet_text['state'] = 'normal'
                self.height_inches_text['state'] = 'normal'
                self.export_button['state'] = 'disabled'
            else:
                user.metric = True
                height_feet_input.set("")
                height_inches_input.set("")
                weight_stone_input.set("")
                weight_pounds_input.set("")
                result_variable.set(0)
                self.bmi_result_text.delete('1.0', END)
                self.weight_kg_text['state'] = 'normal'
                self.height_cm_text['state'] = 'normal'
                self.weight_stone_text['state'] = 'disabled'
                self.weight_pounds_text['state'] = 'disabled'
                self.height_feet_text['state'] = 'disabled'
                self.height_inches_text['state'] = 'disabled'
                self.export_button['state'] = 'disabled'

        # function used to export bmi result date, time, weight, height, name to a CSV file
        # considers imperial vs metric
        def export_to_csv():
            with open("bmi_result.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Height", "Weight", "BMI", "Date & Time"])

                if user.is_metric():
                    writer.writerow([user.get_name(), str(round(user.get_height_cm())) + " cm",
                                     str(round(user.get_weight_kg(), 2)) + " kg", user.get_bmi(), datetime.now()])
                    writer.writerow([])
                else:
                    writer.writerow([user.get_name(),
                                     str(round(user.get_height_feet())) + " feet " +
                                     str(round(user.get_height_inches())) + " inches",
                                     str(round(user.get_weight_stone())) + " stone " +
                                     str(round(user.get_weight_pounds())) + " pounds",
                                     user.get_bmi(), datetime.now()])
                    writer.writerow([])
            f.close()
            tkinter.messagebox.showinfo("Body Mass Index",
                                        "Your results have been saved to CSV file bmi_result.csv")

        ###############################################################################################################
        # Define Main tkinter Frames
        ###############################################################################################################

        main_frame = Frame(self.root, bd=20, width=1350, height=700, padx=10, pady=10, relief=RIDGE)
        main_frame.grid()

        left_frame = Frame(main_frame, bd=10, width=600, height=600, padx=10, pady=13, relief=RIDGE)
        left_frame.pack(side=LEFT)

        right_frame = Frame(main_frame, bd=10, width=560, height=600, padx=10, pady=10, relief=RIDGE)
        right_frame.pack(side=RIGHT)

        ################################################################################################################
        # Define inner frames on left side
        ################################################################################################################

        left_frame_0 = Frame(left_frame, bd=5, width=712, height=100, padx=5, bg="sky blue", relief=RIDGE)
        left_frame_0.grid(row=0, column=0)
        left_frame_1 = Frame(left_frame, bd=5, width=712, height=100, padx=5, pady=5, relief=RIDGE)
        left_frame_1.grid(row=1, column=0)
        left_frame_2 = Frame(left_frame, bd=5, width=712, height=150, padx=5, pady=6, relief=RIDGE)
        left_frame_2.grid(row=2, column=0)
        left_frame_3 = Frame(left_frame, bd=5, width=712, height=150, padx=5, pady=5, relief=RIDGE)
        left_frame_3.grid(row=3, column=0)

        ################################################################################################################
        # Define inner frames on right side
        ################################################################################################################

        right_frame_0 = Frame(right_frame, bd=5, width=522, height=200, padx=5, pady=2, relief=RIDGE)
        right_frame_0.grid(row=0, column=0)
        right_frame_1 = Frame(right_frame, bd=5, width=522, height=400, padx=5, relief=RIDGE)
        right_frame_1.grid(row=1, column=0)
        right_frame_2 = Frame(right_frame, bd=5, width=522, height=200, padx=5, relief=RIDGE)
        right_frame_2.grid(row=2, column=0)

        ################################################################################################################
        # Define Labels, Buttons, Text Boxes, and Scales
        ################################################################################################################

        self.title_label = Label(left_frame_0, text="Body Mass Index", padx=17, pady=4, bd=1, fg="#000000",
                                 relief=RIDGE, font=('arial', 30, 'bold'), bg="sky blue", width=20)
        self.title_label.pack()

        self.body_height_scale = Scale(right_frame_0, variable=result_variable, from_=0, to=50, length=507,
                                       tickinterval=5, orient=HORIZONTAL, state=DISABLED, label="BMI Result",
                                       font=("arial", 10, "bold"))
        self.body_height_scale.grid(row=1, column=1)

        self.bmi_table_label = Label(right_frame_1, font=("arial", 20, "bold",), text="\tBMI Table").grid(row=0,
                                                                                                          column=0)
        self.bmi_table_text = Text(right_frame_1, height=12, width=53, bd=16, font=("arial", 12, "bold"))
        self.bmi_table_text.grid(row=1, column=0, columnspan=3)

        self.toggle_button = Button(right_frame_2, text="Toggle Metric / Imperial", font=("arial", 20, "bold"), bd=2,
                                    bg="sky blue", justify=LEFT, width=29, command=toggle_metric)
        self.toggle_button.pack()

        self.bmi_table_text.insert(END, "Underweight \t\t\t\t" + "less than 18.5 \n\n")
        self.bmi_table_text.insert(END, "Normal \t\t\t\t" + "between 18.5 and 24.9 \n\n")
        self.bmi_table_text.insert(END, "Overweight \t\t\t\t" + "between 25 and 29.9 \n\n")
        self.bmi_table_text.insert(END, "Obese \t\t\t\t" + "30 or greater \n\n")

        self.name_label = Label(left_frame_1, text="Enter Your Name:", font=("arial", 15, "bold"), bd=2, justify=LEFT)
        self.name_label.grid(row=0, column=0, padx=15)
        self.name_text = Entry(left_frame_1, textvariable=name_input, font=("arial", 15, "bold"), bd=5, width=24,
                               justify=LEFT)
        self.name_text.grid(row=0, column=1, pady=10, columnspan=3)

        self.height_cm_label = Label(left_frame_1, text="Height in CM:", font=("arial", 15, "bold"), bd=2,
                                     justify=LEFT)
        self.height_cm_label.grid(row=1, column=0, padx=15)
        self.height_cm_text = Entry(left_frame_1, textvariable=height_cm_input, font=("arial", 15, "bold"), bd=5,
                                    width=24, justify=LEFT)
        self.height_cm_text.grid(row=1, column=1, pady=10, columnspan=3)

        self.weight_kg_label = Label(left_frame_1, text="Weight in KG:", font=("arial", 15, "bold"), bd=2,
                                     justify=LEFT)
        self.weight_kg_label.grid(row=2, column=0)
        self.weight_kg_text = Entry(left_frame_1, textvariable=weight_kg_input, font=("arial", 15, "bold"), bd=5,
                                    width=24, justify=LEFT)
        self.weight_kg_text.grid(row=2, column=1, pady=10, columnspan=3)

        self.height_feet_label = Label(left_frame_1, text="Height in Feet:", font=("arial", 15, "bold"), bd=2,
                                       justify=LEFT)
        self.height_feet_label.grid(row=3, column=0, padx=15)
        self.height_feet_text = Entry(left_frame_1, textvariable=height_feet_input, font=("arial", 15, "bold"), bd=5,
                                      width=7, justify=LEFT, state=DISABLED)
        self.height_feet_text.grid(row=3, column=1, pady=10)

        self.height_inches_label = Label(left_frame_1, text="Inches:", font=("arial", 15, "bold"), bd=2,
                                         justify=LEFT)
        self.height_inches_label.grid(row=3, column=2)
        self.height_inches_text = Entry(left_frame_1, textvariable=height_inches_input, font=("arial", 15, "bold"),
                                        bd=5, width=7, justify=LEFT, state=DISABLED)
        self.height_inches_text.grid(row=3, column=3, pady=10)

        self.weight_stone_label = Label(left_frame_1, text="Weight in Stone:", font=("arial", 15, "bold"), bd=2,
                                        justify=LEFT)
        self.weight_stone_label.grid(row=4, column=0)
        self.weight_stone_text = Entry(left_frame_1, textvariable=weight_stone_input, font=("arial", 15, "bold"), bd=5,
                                       width=7, justify=LEFT, state=DISABLED)
        self.weight_stone_text.grid(row=4, column=1, pady=10)

        self.weight_pounds_label = Label(left_frame_1, text="Pounds:", font=("arial", 15, "bold"), bd=2, justify=LEFT)
        self.weight_pounds_label.grid(row=4, column=2)
        self.weight_pounds_text = Entry(left_frame_1, textvariable=weight_pounds_input, font=("arial", 15, "bold"),
                                        bd=5, width=7, justify=LEFT, state=DISABLED)
        self.weight_pounds_text.grid(row=4, column=3, pady=10)

        self.bmi_button = Button(left_frame_2, text="Calculate BMI", font=("arial", 20, "bold"), bd=2, bg="sky blue",
                                 justify=LEFT, command=calculate_bmi)
        self.bmi_button.grid(row=0, column=0)

        self.export_button = Button(left_frame_2, text="Export to CSV", font=("arial", 20, "bold"), bd=2, bg="sky blue",
                                    justify=LEFT, state=DISABLED, command=export_to_csv)
        self.export_button.grid(row=0, column=1)

        self.reset_button = Button(left_frame_2, text="Reset", font=("arial", 20, "bold"), bd=2, bg="sky blue",
                                   justify=LEFT, command=reset_function)
        self.reset_button.grid(row=0, column=2)

        self.bmi_result_label = Label(left_frame_3, text="BMI Result:", font=("arial", 20, "bold"), bd=2,
                                      justify=LEFT)
        self.bmi_result_label.grid(row=0, column=0)
        self.bmi_result_text = Text(left_frame_3, padx=105, pady=5, font=("arial", 20, "bold"), bd=2, width=10,
                                    height=1, relief="sunk")
        self.bmi_result_text.grid(row=0, column=1)


user = User()
if __name__ == '__main__':
    root = Tk()
    application = BMI(root)
    root.mainloop()
