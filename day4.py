###randomnization---
import random 
# random_integer=random.randint (1,10)
# print(random_integer)

# ----heads and tail---
# import random
# random_side=random.randint(0,1)
# if random_side==1:
#     print("Heads")
# else:
#     print("tails")    
# --------list---
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
#                      "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
#                      "New Hampshire", "Virginia", "New York", "North Carolina", 
#                      "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", 
#                      "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
#                        "Maine", "Missouri", "Arkansas", "Michigan", "Florida", 
#                        "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
#                          "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", 
#                          "Colorado", "North Dakota", "South Dakota", "Montana", 
#                          "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
#                          "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # ---.appedn,.extend comes in data structure-- 
# # ---if want to add states use .apppend ---
# states_of_america.append("kukuland")
# # ----if wanted to add more then 2 items
# states_of_america.extend(["kukuland","huluhulu land"])
# print(states_of_america)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
                # "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
name_str=["Angela", "Ben", "jenny", "Michael", "chole"]
count=len(name_str)
random_name=random.randint(0,count-1)
print(f"{name_str[random_name]},is going to buy meal today!")
