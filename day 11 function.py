#what is function : function is that to take input and give output
#Functions are blocks of reusable code that perform specific tasks
# def Greeting_user():
#     print("Hello World")
#     print("wellcom to aboard")
#
# print("start")
# Greeting_user()
# print("finish")

# #.....................
# #Parameters
# #.................
# def Greeting_user(name): #this name in the brekets is called parameter
#     print(f"Hello {name}")
#     print("wellcom to aboard")
#
# print("start")
# Greeting_user("Ejaz") #this Ejaz name in the breket is called argument
# Greeting_user("Asad")
# print("finish")


#
# ##Multipal parameters
# def Greeting_user(first_name , last_name): #this first_name and last_name in the brekets is called multipal parameter
#     print(f"Hello {first_name}, {last_name}")
#     print("wellcom to aboard")
#
# print("start")
# Greeting_user("Ejaz", "Ahmad") #this Ejaz name in the breket is called argument
# print("finish")

# #..............................
# #keyword Arguments
# #........................
# def Greeting_user(first_name , last_name): #this first_name and last_name in the brekets is called multipal parameter
#     print(f"Hello {first_name}, {last_name}")
#     print("wellcom to aboard")
#
# print("start")
# Greeting_user(last_name="Ahmad", first_name="Ejaz") #this is called keyword argument
# print("finish")

# #....................................
# #Return Statments
# #...................................
# def squre(number):
#     return number * number #this is called return statment
# result = squre(3)
# print(result)

# #we also write this in the print
# def squre(number):
#     return number * number #this is called return statment
# print(squre(3))

#.........................................
#Creating Reusable Function
#.....................................
def emoji_converter(massege):
    words = massege.split(' ')
    emojis = {
        ":)": "😂",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
massege = input("> ")
print(emoji_converter(massege))
