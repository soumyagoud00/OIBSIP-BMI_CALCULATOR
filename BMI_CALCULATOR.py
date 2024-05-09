Weight=float(input("Enter your weight in kg: "))
Height=float(input("Enter your height in meters: "))

if Height <= 0 or Weight <= 0:
    print("Invalid input.Please ensure weight and height are positive numbers.")

Height_in_meters=Height / 100
BMI = Weight / (Height_in_meters**2)
if (BMI < 16):
    print(" You are severly underweight and your BMI is",BMI)
elif (BMI >= 16 and BMI < 18.5):
    print("You are Underweight and your BMI is",BMI)
elif (BMI >=18.5 and BMI < 24):
    print("You are Healthy and your BMI is",BMI)
elif (BMI >= 25 and BMI < 30):
    print("You are Overweight and your BMI is",BMI)
elif (BMI >=30):
    print("You are obesity and your BMI is",BMI) 


