
# https://leetcode.com/problems/island-perimeter/

# CA's solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 特殊技巧, 在旁邊圍一層牆壁, 就不用一直檢查邊界條件
        grid2 = [ [0] + row + [0] for row in grid]
        w = len(grid2[0])
        grid2 = [[0] * w] + grid2 + [[0] * w]
        h = len(grid2)

        edges = 0
        for i in range(1, h-1, 1):
            for j in range(1, w-1, 1):
                if grid2[i][j] == 1:
                    nb = 0
                    nb += grid2[i-1][j]
                    nb += grid2[i+1][j]
                    nb += grid2[i][j-1]
                    nb += grid2[i][j+1]
                    edges += 4- nb
                    
        return edges

# Eve debug version
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # 1. Calculate how many "island" are in this grid? 
        # --> Times 4 as the original perimeter
        total = 0
        neighbor = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total += 1

        # 2. Calculate how many grid does have neighbor on its left and upper side?
        # --> Times 2 because we need to count neighbors on its right and lower side as well
                    if grid[i][j - 1] == 1 or grid[i - 1][j] == 1:
                        neighbor += 1
                    
        # 3. Use original perimetor to deduct the number of grid which has neighbors        
        return total * 4 - neighbor * 2
   




# Eve's solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island = 0
        neighbor = 0
        height = len(grid)
        width = len(grid[0])
        
        # Step 1: for loop 每格方塊，如果是陸地就存 island += 1
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    island += 1
           
        # Step 2: 如果當前的方塊是陸地，且「上面」還有陸地，則 neighbor += 1
        
        # Step 3: 如果當前的方塊是陸地，且「左邊」還有陸地 則 neighbor += 1
        
        # Step 4: 總周長 = 陸地 * 4 - 相交陸地數 * 2 
        return island * 4 - neighbor * 2
        
