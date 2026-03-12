# def find_sum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     return sum
# def main():
#     arr = [1, 2, 3, 4, 5]
#     print(find_sum(arr))
# main()

# arr = [15,22,98,19,22]
# max = arr[0]
# second_max = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#     for j in range(len(arr)):
#         if arr[j] > second_max and arr[j] < max:
#             second_max = arr[j]
# print("max:", max)
# print("second max:", second_max)

# def find_second_largest(arr):
#     first = arr[0]
#     second = arr[0]
#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#     return second
# def main():
#     arr = [15,22,98,19,25]
#     print(find_second_largest(arr))
# main()

def count_even(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count
def main():
    arr = [1, 2, 3, 4, 5, 6]
    print(count_even(arr))
main()