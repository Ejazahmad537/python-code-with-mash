# i = 1
# while i <= 20:
#     print("*" * i)
#     i = i + 1
#
# print("Done")

# #...........................
# #Game using while loop
# #.........................
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("guess a number: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("you won!")
#         break # break is use to stop the loop
# else:
#     print("sorry, you lose :")

#..................................................
#another game using while loop and if eles statement
#................................................
# commond = ""
# started = False
# while True: #while True is used to rapeat the loop
#     commond = input("> ").lower()
#     if commond == "start":
#         if started:
#             print("car already started")
#         else:
#             started = True
#             print("car started")
#     elif commond == ("stop"):
#         if not started:
#             print("car already stopped")
#         else:
#             started = False
#             print("car stopped")
#     elif commond == "help":
#         print(""""
#         start to start the car
#         stop to stop the car
#         quit to quit the game
#         """)
#     elif commond == ("quit"):
#         break
#     else:
#        print("invalid input")

# i = 0
# while i < 60:
#     i = i + 1

# password = ""
# while password != "secret":
#     password = input("Enter your password: ")
#     if password == "secret":
#         print("Welcome again")
#         break
#     else:
#         print("not allowed")

total = 0
num = 1
while num <= 10:
    total = total + num
    num = num + 1
    print(f"the sem is",total)
