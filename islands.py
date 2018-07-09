class Solution():
    
    def check_for_island(self,row,col,grid,visited,islandPath):
        visited[row][col] = True
        islandPath.append((row,col))
        for check in self.get_neighbours(row,col,grid,visited):
            if grid[check[0]][check[1]] == 1:
                self.check_for_island(check[0],check[1],grid,visited,islandPath)
            else:
                visited[check[0]][check[1]] = True
        return islandPath
    
    def get_neighbours(self,row,col,grid,visited):
        myNeighbours = [] 
        for valid in [(row -1,col),(row + 1,col),(row,col -1),(row,col+1)]:
            if valid[0] > -1 and  valid[1] > -1 and valid[0] < len(grid) and valid[1] < len(grid[0]):
                if visited[valid[0]][valid[1]] == False: myNeighbours.append(valid)
                
        return myNeighbours
    
if __name__ == '__main__':
    
    grid = [
           [0,1,0,1,1,0],
           [0,1,0,1,1,0],
           [1,1,0,0,0,1],
           [0,0,1,1,1,1]
          ]

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False for col in range(cols)]for row in range(rows)]
    islandPaths = {}
    islandCount = 0

    for row in range(rows):
        for col in range(cols):
            if visited[row][col] == True or grid[row][col] == 0 :
                pass
            else:
                islandPaths[(row,col)] = Solution().check_for_island(row,col,grid,visited,[])
                islandCount += 1
                
    print(islandCount)
    
    for iStart in islandPaths.keys():
        print("\n\n")
        print(iStart,len(islandPaths[iStart]),islandPaths[iStart])
        path = [[False for col in range(cols)]for row in range(rows)]
        for pathTrue in islandPaths[iStart]:
            path[pathTrue[0]][pathTrue[1]] = True
        print("\n")
        for rowPath  in path:
            print(rowPath)
