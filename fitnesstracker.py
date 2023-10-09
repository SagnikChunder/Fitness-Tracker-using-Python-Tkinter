import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text=f"BMI: {bmi:.2f}")

def calculate_calories():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    
    if gender == "Male":
        calories = (10 * weight) + (6.25 * height * 100) - (5 * age) + 5
    else:
        calories = (10 * weight) + (6.25 * height * 100) - (5 * age) - 161
    
    calories_label.config(text=f"Calories: {calories:.2f}")

# Create the main window
window = tk.Tk()
window.title("Fitness Tracker")

# Create labels and entries for user input
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar(window)
gender_var.set("Male")
gender_option = tk.OptionMenu(window, gender_var, "Male", "Female")
gender_option.pack()

# Create buttons to calculate BMI and calories
bmi_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
bmi_button.pack()

calories_button = tk.Button(window, text="Calculate Calories", command=calculate_calories)
calories_button.pack()

# Create labels to display the results
bmi_label = tk.Label(window, text="BMI: ")
bmi_label.pack()

calories_label = tk.Label(window, text="Calories: ")
calories_label.pack()

# Start the main loop
window.mainloop()