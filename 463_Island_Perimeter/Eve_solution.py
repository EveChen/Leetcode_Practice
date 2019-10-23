
# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island = 0
        neighbor = 0
        height = len(grid)
        width = len(grid[0])
        
        # Step 1: for loop 每格方塊，如果是陸地就存周長 4
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    island += 1
           
        # Step 2: 如果當前的方塊是陸地，且「上面」還有陸地，減去周長 2
        
        # Step 3: 如果當前的方塊是陸地，且「左邊」還有陸地，減去周長 2
        
        # Step 4: 總周長 = 陸地 * 4 - 相交陸地數 * 2 
        return island * 4 - neighbor * 2
        

