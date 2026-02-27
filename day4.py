n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i):            
        print(" ", end=" ")          # this will print spaces before the stars
    for j in range(n - i):
        print("*", end=" ")
    print()  # makes the line break after each row

# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()  # makes the line break after each row

# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()  # makes the line break after each row

# n = int(input("Enter rows: "))
# for i in range(1, n + 1):
#     # print spaces
#     for j in range(n - i):
#         print(" ", end=" ")
#     # print stars
#     for j in range(i):
#         print("*", end=" ")
#     print()