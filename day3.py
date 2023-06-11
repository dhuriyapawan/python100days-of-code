##--Loops---
# number=float(input("which number do you want to check even or odd "))
# if number%2==0:
#     print(f"this is a even number",number )
# else:
#     print(f"this is a odd number",number )
#-----nested if else----
# height=int(input("Enter your height in cm: "))
# if height>=120:
#     print("you can ride")
#     age=int(input("enter the age in years "))
#     if age>=18:
#         print("pl pay $12")
#     elif age<18:
#         print("pl pay $7")
# else:
#     print("you cant ride")
# --------BMI calcluator 2.0--------
height=float(input("enther h: "))
weight=float(input("enther w: "))
bmi=weight/(height**2)
bmi_a=round(bmi)
if bmi_a<=18.5:
    print("underway")
elif 18.5>bmi_a<25:
    print("Normal Weight")
elif 25>bmi_a<35:
    print("overwieght")
elif 30>bmi_a<35:
    print("obses") 
elif bmi_a>35:
    print("clinical obsese")
          