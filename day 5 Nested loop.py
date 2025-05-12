# for x in range(4):
#     for y in range(5):
#         print(x, y)
#
# for x in range(4):
#     for y in  range(5):
#         print(f"({x},{y})")

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print("x" * x_count)

#using nested loop
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)