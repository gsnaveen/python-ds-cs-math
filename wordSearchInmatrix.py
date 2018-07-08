class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        rows = len(board)
        cols = len(board[0])
        foundedWord = []
        for word in words:
            word_index = 0 
            for row in range(rows):
                for col in range(cols):
                    if board[row][col]== word[word_index]:
                        if len(word) > 1:
                            if self.mapNext(word_index,word,row,col,board):
                                foundedWord.append(word)
                        else:
                            foundedWord.append(word)
                        
        return foundedWord         
            
        
    def mapNext(self,word_index,word,row,col,board):
        found = False
        adj = [(row,col -1),(row,col+1),(row-1,col),(row+1,col)]
        validMoves = []
        for toBeValid in adj:
            if (toBeValid[0] < len(board) and toBeValid[0] > -1)  \
                        and (toBeValid[1] < len(board[0]) and toBeValid[1] > -1):
                validMoves.append(toBeValid)
                
        for checkNext in validMoves:
            if board[checkNext[0]][checkNext[1]] == word[word_index + 1] and word_index + 1 == len(word) -1:
                found = True
                break
            elif board[checkNext[0]][checkNext[1]] == word[word_index + 1]:
                found = self.mapNext(word_index+1,word,checkNext[0],checkNext[1],board)
         
        return found
        
        
        
if __name__ == '__main__':
    words = ["oath","pea","eat","rain"] 
    words = ["oeii","otkv","ihkr","o"]
    board = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]

    print(Solution().findWords(board, words))
