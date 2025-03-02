str1 = "priti"
str2 = "priooooya"
def commonletters(st1,st2):
    s1 = set(st1)
    s2=set(st2)
    print("string 1 ==> ",s1)
    print("string 2 ==> ", s2)
    lst = s1 & s2
    print("common .. == >  ",lst)


commonletters(str1,str2)