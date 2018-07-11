def checkAnagram(str1,str2):
    
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    
    isAnagram = True
    myanagram = {}
    
    for char in str1:
        if char in myanagram.keys():
            myanagram[char] += 1
        else:
            myanagram[char] = 1

    for char in str2:
        if char in myanagram.keys():
            myanagram[char] -= 1
        else:
            isAnagram = False
    
    for char in myanagram.keys():
        if myanagram[char] > 0:
            isAnagram = False
    
    return isAnagram

str1 = "funeral" 
str2 = "real fun"
checkAnagram(str1,str2)
