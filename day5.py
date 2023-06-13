# #---Loops with list
# fruits=["Apple","peach","orange"]
# for fruit in fruits:
#     print(fruit+"pie")
# print(fruits)    
#----  calculate avg student height from List
# student_height=input("input the student height ").split()
# # for n in range(0,len(student_height)):

# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
# i=0
# for n in student_height:
#     i+=n
# print(i)
# average=0
# for student in student_height:
#     average+=1
# avg=i/average    
# print(round(avg,2))
# -----largest number ---
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# i=0
# for n in student_scores:
#   if n>i:
#     i=n
# print(i)    
# ----- adding even number only---
i=0
for n in range(0,100,2):
    i+=n
print(i)
           

