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

