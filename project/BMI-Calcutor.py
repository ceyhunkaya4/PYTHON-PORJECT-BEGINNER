height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmı = round(weight/height**2)
if bmı <18.5 :
    print(f"Your BMI is {bmı},you are underweight")
elif bmı <25 :
    print(f"Your BMI is {bmı},you have a normal weight")
elif bmı <30 :
    print(f"Your BMI is {bmı},you are slightly owerweight")
elif bmı <35 :
    print(f"Your BMI is {bmı},you are obese")
else :
    print(f"Your BMI is {bmı},you clinicically obese")
