height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
print(round(bmi, 1))

if bmi >= 0 and bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Healthy weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30 and bmi <= 39.9:
    print("Obese")
elif bmi >= 40:
    print("Extremely Obese")
else:
    print("Error, try again")
