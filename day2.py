# #---data types--silicing----
# # string
# print("hello"[4])
# # ---type of data ---
# num_char=len(input("enter the name:- "))
# print(type(num_char))
# num_str=str(num_char)
# print(type(num_str))
# ----data types---
# two_digit=str(input("enter the two digit number: "))
# a=two_digit[0]
# b=two_digit[1]
# result=int(a)+int(b)
# print(result)
# # ----BMI Body index mask---
# height=float(input("enter your height in m: "))
# weight=int(input("enter your weight in kg: "))
# bmi=weight/(height**2)
# print(round(bmi,2))
# ------age reamining  problem-----
age=int(input("whats is your current age? "))
reaming_years=90-age

days=int(reaming_years*365)
month=int(reaming_years*12)
weeks=int(reaming_years*52)
massage=f"you have {days} days,you have {weeks} weeks,you have {month} month"
print(massage)

