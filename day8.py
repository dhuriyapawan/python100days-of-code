# #---Function 
# # Create a function called greet(). 
# # def greet():
# # Write 3 print statements inside the function.
# #  print("Hi")
# #  print("Heloo")
# #  print("chalo")
# # # Call the greet() function and run your code.
# # greet()
# #----------- Function allows input
# # # def greet_with(name,location):
 
# # #  print(f"Hello {name}")

# # #  print(location)

# # # greet_with (name="pawan",location="nagpur")

# # #-----Coding challenge----- 

# # #Write your code below this line 👇
# # import math
# # def paint_calc(height,width,cover):
# #     area=height*width
# #     num_of_cans=math.ceil(area/cover)
# #     print(f"youll need {num_of_cans} needed")

# # #Write your code above this line 👆
# # # Define a function called paint_calc() so that the code below works.   

# # # 🚨 Don't change the code below 👇
# # test_h = int(input("Height of wall: "))
# # test_w = int(input("Width of wall: "))
# # coverage = 5
# # paint_calc(height=test_h, width=test_w, cover=coverage)
# # ---Prime nuber checker
# #Write your code below this line 👇
# # def prime_checker(number):
# #     is_prime=True
# #     for i in range(2,number):
# #         if number%i==0  :
# #          is_prime=False
# #     if is_prime: 
# #          print(f"{number} is a prime number")
# #     else:    
# #          print(f"{number} is a not prime number")
# # #Write your code above this line 👆11

    
# # #Do NOT change any of the code below👇
# # n = int(input("Check this number: "))
# # prime_checker(number=n)


# # ---------cipher rule----------
  
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# def encrypt(plain_text, shift_amount):
#     cipher_text=" "
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+= new_letter
#     print(f"the encoded text is {cipher_text}")
         
# encrypt(plain_text=text,shift_amount=shift)

# def decrypt(cipher_text,shift_amount):
#     plain_text=" "
#     for letter in cipher_text:
#         n_position=alphabet.index(letter)
#         nw_position=n_position-n_position
#         plain_text +=alphabet[nw_position] 
#     print(f"the decode code is{plain_text}")

# decrypt(cipher_text=text,shift_amount=shift)




# # -----------

    

















# #     ##HINT: How do you get the index of an item in a list:
# #     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# #     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# # #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
