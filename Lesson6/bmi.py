height=float(input("Enter your height"))
weight=float(input("Enter your weight"))
bmi=weight/height**2
print(bmi)
if bmi<=20:
    print("You are underweight")
elif bmi<=30:
    print("You are healthy")
elif bmi<=40:
    print("You are over weight")
elif bmi<=50:
    print("You are obese")
else:
    print("You are severly obese")