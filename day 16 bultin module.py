#we import random module for generating random values
import random
# # for i in range(3):
# #     print(random.random())
#
#
# #now we use randint method and put the value
# for i in range(3):
#     print(random.randint(5,10))


# #select some one is a leader game
# members = ["Ejaz", "murad", "Imtiaz", "Zia"]
# leader = random.choice(members)
# print(leader)


# #Dice game
# dice = [1,2,3,4,5,6,7]
# for i in range(1):
#     choice = random.choice(dice)
#     print(choice)

#Another method of dice game
class Dice:
    def roll(self):
        first_number = random.randint(1,6)
        second_number = random.randint(1,6)
        return first_number,second_number

dice = Dice()
print(dice.roll())

