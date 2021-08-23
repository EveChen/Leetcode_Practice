
# Link: https://leetcode.com/problems/game-of-life/submissions/

# Key 1: We actually don't need to care of about either 1 or 0 in the second set of for loops. The only transition states are.
# 2 that represents change from dead to alive
# 3 that represents change from alive to dead

# 0: dead
# 2: dead -> alive
# 1: alive
# 3: alive -> dead

# Solution A: 判斷目前值和周遭總和 (有兩種狀況)，若目前是0而且周遭總和等於3，等於從死亡轉變成存活；若目前是1而且周遭和介於 2<sum()<3，等於從存活變成死亡。這裡用list comprehension去計算「周遭總和」
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return
        
        for iM in range(m):
            for iN in range(n):
                countNeighbor = sum([board[i][j] % 2 for i in range(iM-1, iM+2) for j in range(iN-1, iN+2) if 0 <= i < m and 0 <= j < n]) - board[iM][iN]
                if board[iM][iN] == 0 and countNeighbor == 3:
                    board[iM][iN] = 2
                if board[iM][iN] == 1 and (countNeighbor < 2 or countNeighbor > 3):
                    board[iM][iN] = 3
        
        for iM in range(m):
            for iN in range(n):
                if board[iM][iN] == 2:
                    board[iM][iN] = 1
                if board[iM][iN] == 3:
                    board[iM][iN] = 0

# Solution B: 概念同 solution A，只不過 countNeighbor 改用新建的 function 計算
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return
        
        for iM in range(m):
            for iN in range(n):
                if board[iM][iN] == 0 and self.countNeighbor(board, iM, iN) == 3:
                    board[iM][iN] = 2
                if board[iM][iN] == 1 and (self.countNeighbor(board, iM, iN) < 2 or self.countNeighbor(board, iM, iN) > 3):
                    board[iM][iN] = 3
                    
        for iM in range(m):
            for iN in range(n):
                if board[iM][iN] == 2:
                    board[iM][iN] = 1
                if board[iM][iN] == 3:
                    board[iM][iN] = 0
                    
    def countNeighbor(self, board, i, j):
        m, n = len(board), len(board[0])
        count = 0
        
        if i-1 >= 0 and j-1 >= 0: count += board[i-1][j-1] % 2
        if i-1 >= 0: count += board[i-1][j] % 2
        if i-1 >= 0 and j+1 < n: count += board[i-1][j+1] % 2
        if j-1 >= 0: count += board[i][j-1] % 2
        if j+1 < n: count += board[i][j+1] % 2
        if i+1 < m and j-1 >= 0: count += board[i+1][j-1] % 2
        if i+1 < m: count += board[i+1][j] % 2
        if i+1 < m and j+1 < n: count += board[i+1][j+1] % 2
        
        return count

        
