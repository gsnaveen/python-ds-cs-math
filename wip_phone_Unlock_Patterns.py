class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dail = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
               ]
        myDictNumbers = {}
        myDictAdj = {}
        
        rows = len(dail)
        cols = len(dail[0])
        
        #creating Adjunct list  
        for row in range(rows):
            for col in range(cols):
                myDictNumbers[(row,col)] = dail[row][col]
                adjs = self.findAdj(row,col,dail,rows,cols)
                myDictAdj[(row,col)] = adjs
                
#         print(myDictNumbers)
#         print(myDictAdj)
    
    def findAdj(self,row,col,dail,rows,cols):
        toReturn = []
        adjs = [(row -1 ,col -1),(row -1,col),(row -1 ,col + 1),
                  (row,col -1),                 (row,col + 1),
                  (row +1 ,col -1),(row +1,col),(row +1 ,col + 1)                
                 ]              
        for vals in adjs:
            if vals[0] > -1 and vals[1] > -1 and vals[0] < rows and vals[1] < cols:
                toReturn.append(vals)
        return toReturn
        
if __name__ == '__main__':
    m= 1
    n = 4
    Solution().numberOfPatterns(m,n)
