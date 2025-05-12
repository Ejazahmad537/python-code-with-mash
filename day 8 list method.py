# #append method (method is after Dot(.)
# numbers = [1, 2, 3, 4, 5]
# numbers.append(20)
# print(numbers)
#
# #insert method
# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, 10) #mean put 10 into first value
# print(numbers)
#
# #remove method
# numbers = [1, 2, 3, 4, 5]
# numbers.remove(3) #mean to remove 3 from the list
# print(numbers)
#
#
# #clear method
# numbers = [1, 2, 3, 4, 5]
# numbers.clear() #if we want to remove all the list
# print(numbers)
#
#pop method
from operator import index

##pop method
# numbers = [1, 2, 3, 4, 5]
# numbers.pop() #if we want to remove last item from the list
# print(numbers)
#
# #indix method
# numbers = [1, 2, 3, 4, 5]
# print(numbers.index(5)) #to find the index of the value in the list

# #count method
# numbers = [1, 2, 3, 4,4,4, 5]
# print(numbers.count(4))

# #sort and revirse method
# numbers = [1, 2, 3, 4,4,4, 5]
# numbers.sort()
# numbers.reverse()
# print(numbers)

#write a program to remove the duplicate from the list
numbers = [1, 2, 2, 4, 5, 8, 4, 8, 9]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)