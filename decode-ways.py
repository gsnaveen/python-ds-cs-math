# Time:  O(n)
# Space: O(1)
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#
class Solution():
    def numDecodings(self,s):
        count = 0
        strLen:int = len(s)
        if  s == '' or int(s) < 1: 
            pass
        else:
            for i in range(len(s)):

                if s[i] == '0' : continue
                if int(s[i]) > 0 : count += 1
                if len(s[i:i+2]) == 2 and int(s[i:i+2]) < 27 : count += 1
  
        return count

if __name__ == "__main__":
    for i in ["","0", "10", "10", "103", "1032", "10323"]:
        print ("Ans",i,Solution().numDecodings(i))
