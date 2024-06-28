def is_palindrome(s):
    
    return s == s[::-1]


input_string = input("Enter a string : ")


result = is_palindrome(input_string)


if result:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
