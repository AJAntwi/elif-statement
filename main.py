# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI= round(weight / (height ** 2))

if BMI < 18.5:
  print("You are underweight.")
elif BMI < 28:
  print("You have a normal weight")
elif BMI <33:
  print("You are slightly overweight")
elif BMI < 40:
  print("You are obese.")
else:
  print("You are clinically obese")


