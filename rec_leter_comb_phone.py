def cPhoneNum(number,start,myD,pD):

    cNum = number[0]

    for chr in pD[int(cNum)]:
        newStr = start + chr
        if len(number)> 1:
            cPhoneNum(number[1:],newStr,myD,pD)
        else:
            myD.add(newStr)

    return myD



pD = {
    1:[''],
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r','s'],
    8: [ 't', 'u','v'],
    9: ['w', 'x','y','z']
}

myD = set()

phNum = "123456"
start = ''

print(cPhoneNum(phNum,start,myD,pD))
