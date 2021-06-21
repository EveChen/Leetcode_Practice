
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         #0. corner case
#         if not root:
#             return []
        
#         #1. 將起始節點存入queue中
#         queue = [root] 
#         result = []
        
#         #2. 當queue存在(裡面有東西時)，進入while loop去遍歷該層中的節點
#         while queue:
#             next_queue = []
#             result.append([node.val for node in queue])
            
#             #3. 一層遍歷完後再繼續遍歷第二層
#             for node in queue:
#                 if node.left:
#                     next_queue.append(node.left)
#                 if node.right:
#                     next_queue.append(node.right)
#             queue = next_queue
#         return result
        
# Method - Leetcode's iteration solution
from collections import deque
class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        
        queue = deque([root])
        level = 0
        
        while queue:
            res.append([]) #先製造出能夠存放三層queue的list --> [[], [], []]
            for i in range(len(queue)):
                node = queue.popleft() #清空queue
                res[level].append(node.val) #for loop把queue裡面的值壓進res裡
                
                if node.left:   #queue新加入第二層的left
                    queue.append(node.left)
                if node.right:  #queue新加入第二層的right
                    queue.append(node.right)
                    
            level += 1 #每一層都要遍歷
        return res
        
        
        
        
