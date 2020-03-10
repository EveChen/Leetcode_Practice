# https://leetcode.com/problems/island-perimeter/

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
   
