class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = {}
        minIndex = float("inf")
        for index,char in enumerate(s):
            if char not in myDict.keys():
                myDict[char] = [index]
            else:
                myDict[char].append(index)
        
        for char in myDict.keys():
            if len(myDict[char]) == 1:
                minIndex = min(minIndex,myDict[char][0])
                
        return -1 if minIndex == float("inf") else minIndex
# s = "leetcode"
# #return 0.
# s = "loveleetcode"
#return 2.
if __name__ == '__main__':
    s = "loveleetcode"
    s = "leetcode"
    print(Solution().firstUniqChar(s))
