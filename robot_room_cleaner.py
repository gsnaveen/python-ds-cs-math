class Solution:
    
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        s_row = robot[0]
        s_col = robot[1]
        room = robot[2]
        
        #print(type(s_row))
        
        listing = self.validMove(s_row,s_col,room)
        if room[s_row][s_col] == 1:
            room[s_row][s_col] = 2
            for move in listing:
                self.cleanRoom([move[0],move[1],room])
            
        return
                
    
    def validMove(self,row,col,room):
        #print(type(row),type(col))
        listMoves = [(row - 1,col),(row + 1,col),(row,col - 1),(row,col + 1)]
        returnList = []
        for move in listMoves:
            try:
                val = room[move[0]][move[1]]
                if val == 1: returnList.append(move)
            except:
                pass
        
        return returnList
    
if __name__ == "__main__":
    room = [
          [1,1,1,1,1,0,1,1],
          [1,1,1,1,1,0,1,1],
          [1,0,1,1,1,1,1,1],
          [0,0,0,1,0,0,0,0],
          [1,1,1,1,1,1,1,1]
          ]
    row = 1
    col = 3
    print(room)
    Solution().cleanRoom([row,col,room])
    print(room)
