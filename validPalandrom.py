class Solution:
    
    def validPalandrom(self,inStr):
        palandrom = True
        cleanString = []
        for i in inStr:
            if i.isdigit() or i.isalpha():
                cleanString.append(i.lower())
        
        i = 0
        j = len(cleanString) -1
        
        while i <= j:
            
            if cleanString[i] != cleanString[j] :
                palandrom = False
                break
            else:
                i += 1
                j -= 1
        
        return palandrom
    
if __name__ == '__main__':
    Input="A man, a plan, a canal: Panama"
    Input="race a car"
    print(Solution().validPalandrom(Input))
