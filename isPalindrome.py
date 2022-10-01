def isPalindrome(string):
    start, end = 0, len(string) - 1
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


print("Enter a string to check palindrome")
string = input()
if isPalindrome(string):
    print("String is palindrome")
else:
    print("String is not a palindrome")