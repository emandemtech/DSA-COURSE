# def count_num(arr):
#     freq = {}
#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1
#     return freq
# def main():
#     arr = [1, 2, 2, 3, 3, 3, 4]
#     print(count_num(arr))
# main()

# def word_count(s):
#     words = s.split() # split() method is used to split a string into a list of words based on whitespace
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq
# def main():
#     s = "hello world hello"
#     print(word_count(s))
# main()

def max_freq_value(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_count = 0
    result = None
    
    for key,value in freq.items():
        if value > max_count:
            max_count = value
            result = key
    return result
def main():
    arr = [1, 2, 2, 3, 3, 3, 4]
    print(max_freq_value(arr))
main()