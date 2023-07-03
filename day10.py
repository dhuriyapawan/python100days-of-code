# --day 10 function-----
# def function():
#     sample text
# def formate_name(f_name,l_name):
#     formted_fname=f_name.title()
#     formted_lname=l_name.title()
#     return f"{formted_fname} {formted_lname}"
    
# print(formate_name("pawan","shona"))

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
        
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month():
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month==2:
#     return 29
#   return month_days[month-1]
# # #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# ------------calculator
def add(n1,n2):
    return n1+n2

def subs(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operator_fucntion={
    "+":add,
    "-":subs,
    "*":mul,
    "/":divide
}
n1=int(input("enter the n1 " ))
n2=int(input( "enter the n2 "))
for symbol in operator_fucntion:
    print(symbol)
opertion_symbol=input(" pick operation ")
calculation=operator_fucntion[opertion_symbol ]
answer=calculation(n1,n2)

print(f"the numbers are{n1} and {n2} = {answer}")