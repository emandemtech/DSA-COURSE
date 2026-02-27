# # strings:
# name = "Codegnan"
# print(len(name))  # length of the string

# # write a program to count the number of characters in a string
# def count_characters(string):
#     count = 0
#     for char in string:
#         count += 1
#     return count
# def main():
#     text = input("Enter a string: ")
#     character_count = count_characters(text)
#     print(f"The number of characters in the string is: {character_count}")
# main()

# # write a program to count the number of vowels in a given string
# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
# for char in string:
#     if char in vowels:
#         vowel_count += 1
# print(f"The number of vowels in the string is: {vowel_count}")

# # string reversal
# string = input("Enter a string: ")
# reversed_string = ""
# for char in string:
#     reversed_string = char + reversed_string
# print(f"The reversed string is: {reversed_string}")

string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"The reversed string is: {reversed_string}")

