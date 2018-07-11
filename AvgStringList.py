def AvgStringList(stringlist):
    wordCount = 0
    wordLength = 0
    for in_string in stringlist:
        word_list = in_string.split(" ")
        for word in word_list:
            validWord = False
            for char in word:
                if char.isalpha() or char.isdigit():
                    wordLength += 1
                    validWord = True
            if validWord: wordCount += 1
                
    return wordLength/wordCount

stringlist = ["Hello World!", "Welcome to CoderPad.", "This pad is running Python 3."]
print(AvgStringList(stringlist))
