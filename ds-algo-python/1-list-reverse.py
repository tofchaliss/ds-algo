#Python way of reversing the list
def reverse_list(main_list):
    new_list = []
    for num in main_list[::-1]:
        new_list.append(num)
    return new_list

#This is in place reversing of the array
def reverse_list_with_index(main_list):
    startIndex = 0
    highIndex = len(main_list) -1
    while startIndex < highIndex:
        num = main_list[startIndex]
        main_list[startIndex] = main_list[highIndex]
        main_list[highIndex] = num
        startIndex+= 1
        highIndex -= 1
    return main_list

list_1=[1,2,3]
print(reverse_list(list_1))
list_1=[1,2,3,4,5, 100]
print(reverse_list_with_index(list_1))