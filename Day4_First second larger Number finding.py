list1 = [10,20,30,45,25,8]
list1.sort()
print("The largest element is :   ", list1[-1])


list2  = list(set(list1))

list2.sort()

print("The Second largest Numeber is :  ", list2[-2])


list3 = list(set(list2))

list3.sort()

print("The Thrild Largerst Number is :   ", list3[-3])



