#Repitition Statement
#Data types allowed ti be iterated: Lists, Ranges, Sets, Tuple, Dictionaries, Strings
# ctrl + / = shortcut for comment

# x = range(5,11)
petName = ["Snowy", "Blacky", "Bruno"]

#For Loop
# for num in x:
    # print(num)

# Slicing a lists
for name in petName[::-1]:
    print(name)

#Looping Dictionaries
# key:value
# user = {
#     "first_name" : "Johnny",
#     "last_name" : "Tadea",
#     "age" : 25,
#     "average" : 81.76,
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# }

# for key in user:
#     print(key, ":", user[key])

#Looping List of Dictionaries
# list_of_users = [{
#             "first_name" : "Johnny",
#             "last_name" : "Tadea",
#             "age" : 25,
#             "average" : 81.76,
#             "list_subjects" : ["Programming", "Mathematics", "English"]
#     }, 
#     {
#             "first_name" : "Rose",
#             "last_name" : "Tadea",
#             "age" : 23,
#             "average" : 82.54,
#             "list_subjects" : ["Programming", "Mathematics", "English"]
#     },
#     {
#         "first_name" : "Angel",
#         "last_name" : "Tadea",
#         "age" : 27,
#         "average" : 86,
#         "list_subjects" : ["Programming", "Mathematics", "English"]
#     }
# ]

# for key in list_of_users:
#     for x in key:
#         print(x, ":", key[x])

# #looping in reverse
# x = range(1,10)
# for i in x[::-1]:
#     print(i)