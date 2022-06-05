Numbers = [3,5,6,2,11,-4,8]
pair_sum = 7


def TwoSum(Numbers,pair_sum):
    for i in range(len(Numbers)-1):
        for j in range(i + 1,len(Numbers)):
            if Numbers[i] + Numbers[j] == pair_sum:
                print("Pair with sum", pair_sum,"is: (", Numbers[i],",",Numbers[j],")")
                
TwoSum(Numbers, pair_sum)

    
    