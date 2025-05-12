#
# matrix = [
#
#          [1 , 2, 3],
#          [4, 5,  6],
#          [7 , 8, 9]
#     ]
# print(matrix)
#
# matrix = [
#
#          [1 , 2, 3], #mean first 1 value in first list
#          [4, 5,  6],
#          [7 , 8, 9]
#     ]
# print(matrix[0][1])

#using for loop
matrix = [

         [1 , 2, 3], #mean first 1 value in first list
         [4, 5,  6],
         [7 , 8, 9]
    ]
for row in matrix:
    for item in row:
        print(item)
