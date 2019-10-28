
# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Case 1: The tree does not exist
        if root is None:
            return []
        
        # Case 2: The tree exists
        queue = deque([root])
        res = []
        
        while queue:
            level = []
            # Save each node value by levels
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                # Append each node from a specific level to the queue
                if node.left:
                    queue.append(node.left)
                if node.right: #Q: Why I cannot use "elif"?
                    queue.append(node.right)
            res.append(level)
        return res
