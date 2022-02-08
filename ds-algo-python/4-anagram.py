def anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            return False 

    return True

print(anagram("tast", "sttt"))
