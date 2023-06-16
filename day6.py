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

#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guess = input("Guess a letter: ").lower()
# for n in range(0,len(chosen_word)):
#     print("_")


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for letter in chosen_word:
    if letter == guess:
        print(letter)
    else:
        print("_")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
