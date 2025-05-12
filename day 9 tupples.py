
#deffrence b/w list and tupple is that list can be read and writ and tupple is only can read
numbers = (1, 2, 3 , 4)
print(numbers[0])

#but when we cange the velue that give error
numbers = (1, 2, 3 , 4)
numbers[0]= 10

#unpacking tupples
cordinates = (1, 2, 3)
x, y, z = cordinates
print(x)