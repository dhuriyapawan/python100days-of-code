##--Loops---
# number=float(input("which number do you want to check even or odd "))
# if number%2==0:
#     print(f"this is a even number",number )
# else:
#     print(f"this is a odd number",number )
#-----nested if else----
height=int(input("Enter your height in cm: "))
if height>=120:
    print("you can ride")
    age=int(input("enter the age in years"))
    if age>=18:
        print("pl pay $12")
    elif age<18:
        print("pl pay $7")
else:
    print("you cant ride")
            
    