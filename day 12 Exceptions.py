# #when we type text instead number then the program give me error
# Age = int(input("How old are you? "))
# print(Age)
#
# #now we give the massege to the user we using( try and except valueError)
# try:
#     Age = int(input("How old are you? "))
#     print(Age)
# except ValueError:
#     print("invalid input")

#another example of except valueError
try:
    Age = int(input("How old are you? "))
    incom = 2000
    risk = incom / Age
    print(Age)
except ZeroDivisionError:
    print("Age can't be divided by zero")
except ValueError:
    print("invalid input")
