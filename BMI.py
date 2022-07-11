def bmi_calc(w, h):
    bmi = w / (h/100)**2
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
result = bmi_calc(weight, height)
print("Your BMI is: ", result)
