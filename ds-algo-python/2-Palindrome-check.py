def isPalindrome(str1):
    start_index = 0
    end_index = len(str1) -1

    while start_index < end_index:
        if str1[start_index] != str1[end_index]:
            return "Not Palindrome"
        else:
            start_index += 1
            end_index -= 1
    
    return "Palindrome"

def isPalindromeEasy(str1):
    if str1 == str1[::-1]:
        return True
    
    return False

print(isPalindrome("FrarF"))
print(isPalindromeEasy("FraKF"))
