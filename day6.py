# --definign Function--------
# def my_functiomn():
    # do this
    # then do this
    # finally do this
# ----While looping---
# Something is true for condition
# while something_istrue:
#     do this 
# mylist=[]
# i=0
# while len(mylist)<4:
#     mylist.append(i)
#     i+=1
#     print(mylist)
# ----write a program to add upto 100 using while loop
# total=0
# counter=0
# while counter<=100:
#     total=total+counter
#     counter=counter+1
# print(total)
#------find 100 th position in given number---
# lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# my_message=""
# #Type your code here.
# for n in range(0,len(lst)-1):
#     lst[n]=int(lst[n])
#     if lst[n]== 100:
#         # print(n)
#      print(my_message)
#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
true=0
choosen_word=random.choice(word_list)
# for n in range(0,len(word_list)):
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("guess the letter ").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in choosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")    