
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        operationList = []
        for row in range(rows):
            for col in range(cols):
                
                adj = self.getAdj(row,col,rows,cols)
                counter0 = 0
                counter1 = 0
                
                for checkPix in adj:
                    if board[checkPix[0]][checkPix[1]] == 0:
                        counter0 += 1
                    else:
                        counter1 += 1
                
                if board[row][col] == 0 and counter1 == 3:
                    operationList.append((row,col,1))
                elif board[row][col] == 1 and (counter1 not in [2,3]):
                    operationList.append((row,col,0))
                
        #print(operationList)
        for update in operationList:
            board[update[0]][update[1]] = update[2]
       
        
    def getAdj(self, row,col,rows,cols):
        return_valid_list = []
        
        adjx = [(row -1,col-1)
              ,(row -1,col)
              ,(row -1,col+1)
              ,(row ,col-1)
              ,(row ,col+1)
              ,(row +1,col-1)
              ,(row +1,col)
              ,(row +1,col+1) 
              ]
        
        for adjcheck in adjx:
            check_row = adjcheck[0]
            check_col = adjcheck[1]
            if (check_row > -1 and check_row < rows) and (check_col > -1 and check_col < cols): 
                return_valid_list.append(adjcheck)

        return return_valid_list
                
if __name__ == '__main__':
    Input = [
              [0,1,0],
              [0,0,1],
              [1,1,1],
              [0,0,0]
            ]
    
    print(Input)
    Solution().gameOfLife(Input)
    print(Input)
