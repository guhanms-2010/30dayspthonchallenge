def reverse_string1(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1
str = "Sriram"
print("The orginal string is:",str)
print("The reversed string is:", reverse_string1(str))

if reverse_string1(str) == str:
    print("The Given string Is palindrome")
else:
    print("The given string is not palindrome")

    
    
    