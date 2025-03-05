#concat +

def amastring(str1):
    vowels="aeiouAEIOU"
    count = 0
    #need to check index and character both
    for i,char in enumerate(str1):
        if char in vowels:
            count+=len(str1)-i
            return count


print(amastring("priti"))