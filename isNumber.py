class Solution2:
    
    def isNumber(self,num):
        
        isnumberTrue = True
        num = num.replace(' ','')
        length = len(num.replace(' ',''))
        decimal = False
        
        if length == 0: return False
        
        for i,char in enumerate(num):
            
            if num[i] == ".":
                decimal = True
                if num[i+1] in ["e"] or num[i+1].isdigit():
                    pass
                else:
                    isnumberTrue = False
                    
            if num[i] == "e":
                if num[i+1] in ["-"] or num[i+1].isdigit():
                    pass
                else:
                    isnumberTrue = False
            
            if not num[i].isdigit() and num[i] not in  ["e",'.','-']:
                isnumberTrue = False
                
            if num[i] == '-' and decimal != True:
                isnumberTrue = False
            
        
        return isnumberTrue
        
    
    
if __name__ == "__main__":
    assert Solution2().isNumber("3.e-23") == True
    assert Solution2().isNumber(".2e81") == True
    assert Solution2().isNumber("2e10") == True
    assert Solution2().isNumber(" 0.1") == True
    assert Solution2().isNumber("1 b") == False
    assert Solution2().isNumber("3-2") == False
    assert Solution2().isNumber("abc") == False
