# # # # --Dicnary---attonation by  {}
# # # # {"Bug":value}

# # # programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
# # #                            "Function": "A piece of code that you can easily call over and over again."}
# # # # print(programming_dictionary["Bug"])
# # # # Adding  new items in dictronary
# # # programming_dictionary["Looping"]="Addint loop into the dictonary"
# # # # print(programming_dictionary)
# # # # creat a Empty dictonary
# # # empty_dict={}
# # student_scores = {
# #   "Harry": 81,
# #   "Ron": 78,
# #   "Hermione": 99, 
# #   "Draco": 74,
# #   "Neville": 62,
# # }
# # #  🚨 Don't change the code above 👆

# # #TODO-1: Create an empty dictionary called student_grades.
# # student_grades={}
# # #TODO-2: Write your code below to add the grades to student_grades.👇
# # add=0
# # for i in student_scores:
# #     score=student_scores[i]
# #     if score>90:
# #         student_grades[i]="outsatnding"
# #     elif score>80:
# #         student_grades[i]="Exeeds Expection"
# #     elif score>70:
# #             student_grades[i]="Acceptable"
# #     else:
# #          student_grades[i]="fail"                 
# # # 🚨 Don't change the code below 👇
# # print(student_grades)

# # ---nesting list and dictinory-------
#           # {key:[list],
#            #  key2:{dic t} 
# #           #  }
# # travel_vlog={
# #     "France":["parish","Lille","Djon"],
# #     "Germany":["Berlin","hamburg"] 
# # }
# # print(travel_vlog["France"])

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited,times_visited,cities_visited):
#     new_country={}
#     new_country["country"]=country_visited
#     new_country["visited"]=times_visited
#     new_country["cities"]=cities_visited
#     travel_log.append(new_country)

        
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# ----------------dictnory for biding pricing-----
dict={"name":" bid"}
def bid(bid_name,bid_price):
    dict["name"]=bid_name
    dict["bid"]=bid_price
    print(dict)
bid(bid_name="araon",bid_price=25)  



