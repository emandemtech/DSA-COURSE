# total_size = 7
# linear_table = [None] * 7
# quadratic_table = [None] * 7
# double_hasing_table = [None] * 7
# def hash_function(key):
#     return key % total_size

# def insert_linear(key):
#     index = hash_function(key)
#     i = 0
#     while linear_table[(index + i) % total_size] is not None:
#         i += 1
#     new_index = (index + i) % total_size
#     linear_table[new_index] = key

# def insert_quadratic(key):
#     index = hash_function(key)
#     i = 0
#     while quadratic_table[(index + i**2) % total_size] is not None:
#         i += 1
#     new_index = (index + i**2) % total_size
#     quadratic_table[new_index] = key
    
# def insert_double_hashing(key):
#     index = hash_function(key)
#     i = 0
#     while double_hasing_table[(index + i * hash_function(key)) % total_size] is not None:
#         i += 1
#     new_index = (index + i * hash_function(key)) % total_size
#     double_hasing_table[new_index] = key
    
# keys = [8,15,22]

# for key in keys:
#         insert_linear(key)
        
# for key in keys:
#         insert_quadratic(key)

# for key in keys:
#         insert_double_hashing(key)
        
# print("Linear probing table:")
# print(linear_table)

# print("\n")

# print("Quadratic probing table:")
# print(quadratic_table)

# print("\n")
# print("Double hashing table:")
# print(double_hasing_table)

# two pointer approach
# input = [2, 7, 11, 13]
# output = [2, 7]
# target = 9

nums = [2, 7, 11, 13]
target = 9

seen = {}

for num in nums:
    complement = target - num
    if complement in seen:
        print([complement, num])
        break
    seen[num] = True