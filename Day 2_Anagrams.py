def check(S1,S2):
    if(sorted(S1)== sorted(S2)):
        print("The given text  are Anagrams")
    else:
        print("The given text are not anagrams")
        
S1 = "Ate"
S2 = "Eat"

check(S1,S2)
