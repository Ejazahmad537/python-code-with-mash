# # #if statment
# is_hot = True # is_hot = True #(this is boolean veriable) A boolean variable is a type of variable that can only hold one of two values: true or false
# if is_hot:
#     print("it,s a hot day")
#     print("drink planty water")
# else:
#     print("it,s could day")
#     print("wear warm cloths")

# # #another example
# price_of_house = 100000
# has_good_credit = True
# if has_good_credit:
#     down_pyment = 0.1 * price_of_house
# else:
#     down_pyment = 0.2 * price_of_house
# print(f"down_pyment: ${down_pyment}")


# #.....................
# #if and elif statment
# #......................
# weather = input("Enter Weather Condition: ")
# if weather.lower() == "hot":
#         print('it,s a hot day')
#         print('drink a plenty of water')
#
# elif weather.lower() == "could":
#     print('it,s not a could day')
#     print('wear warm cloths')
#
# else:
#     print('it,s a sunny day')
#
# #............................
# #logical operator (and, or, and not)
# #..........................
# has_good_credit = True #Both condition is Ture
# has_high_income = True
# if has_good_credit and has_high_income: #and is a logical operator
#     print("Eligible for loan")
#
# has_good_credit = False # at least one condition is True
# has_high_income = True
# if has_good_credit or has_high_income: #and is a logical operator
#     print("Eligible for loan")
#
# has_good_credit = True
# has_creminal_record = False
# if has_good_credit and not has_creminal_record : #and is a logical operator
#     print("Eligible for loan")

##.......................................................
##Comparison Operators (>, <, <=, >=, ==, != and so on)
##.....................................................
# temperature = 35
# if temperature > 30:
#     print("it,s a hot day")
#
# else:
#     print("it,s a cold day")


# # Swaping using three veriables
# a = 5
# b = 9
# num = a
# a = b
# b = num
# print(f"swaping a = {a}, b = {b}")


#using Two veriables
a = 5
b = 8

a,b = b,a
print(f"a={a}, b={b}")