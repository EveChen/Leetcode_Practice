
# Link: https://leetcode.com/problems/longest-common-prefix/

# solution A: Vertical scanning
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if strs == None:
#             return ""
#         for i in range(len(strs[0])): 
#             for j in range(1,len(strs)):
# # Case 1: 代表當 strs[0] 的長度和 strs[j] 不相等時，return
# # Case 2: 代表 strs[j][i] 的 char 不等於 strs[0][i] 的 char，return
#                 if i == len(strs[j]) or strs[j][i] != strs[0][i]:
#                     return strs[0][:i]
#         return strs[0]



# Solution A: Vertical scanning 的變形
# 思路: 先找最短長度的那個字，然後遍歷 strs 中的字(i.e. string)，一個個比對 string[i] != shortest_word[i]
# 問題: traverse strs list，再 traverse index，若有相同的就 append res list，若沒有相同的就跳出，但是要怎麼比對 str1[i] == str2[i] == str3[i] ?，用 list 或 dict 都會碰到同樣問題
# Ans: 不需要使用 ==，直接用 != 處理，若不等於，就回傳 shortest_word[:i]。補充，也不需要使用 list/dict 去紀錄
# Time complexity: O(len(shortest_word) * len(strs))?
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         shortest_word = min(strs, key = len)
#         for i in range(len(shortest_word)):
#             for string in strs:
#                 if string[i] != shortest_word[i]:
#                     return shortest_word[:i]
#         return shortest_word
    
    
# Solution B: use enumerate
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         shortest_word = min(strs, key = len)
        
#         for ind, char in enumerate(shortest_word):
#             for string in strs:
#                 if string[ind] != char:
#                     return shortest_word[:ind]
#         return shortest_word
                    
    
# Solution C: use zip
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
        
#         for ind, char in enumerate(zip(*strs)):
#             if len(set(char)) > 1: #代表從這個set(char) > 1的ind開始，出現沒有prefix common的字母
#                 return strs[0][:ind]
#         return min(strs, key = len)

    
# Same logic as solution C
# zip(*strs) traverse = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
# 故 set(i) = {'f'}, {'l'}, {'o', 'i'}, {'g', 'w'}
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         prefix = ""
#         for i in zip(*strs):
#             if len(set(i)) == 1:
#                 prefix += i[0]
#             else:
#                 break
#         return prefix

# Solution D: Built-in function
# import os
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         return os.path.commonprefix(strs)


# Solution E: Divide & Conquer
# Q: Ask CA about the time complexity
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         def find_commonPrefix(left, right):
#             min_length = min(len(left), len(right))
#             for i in range(min_length):
#                 if left[i] != right[i]:
#                     return left[:i]
#             return left[:min_length]
            
#         # recursion    
#         def find_longestCommonPrefix(strs, left_index, right_index):
#             if left_index == right_index:
#                 return strs[left_index]
#             else:
#                 mid_index = (left_index + right_index) // 2
#                 lcpleft = find_longestCommonPrefix(strs, left_index, mid_index)
#                 lcpright = find_longestCommonPrefix(strs, mid_index + 1, right_index)
#             return find_commonPrefix(lcpleft, lcpright)
            
#         return find_longestCommonPrefix(strs, 0, len(strs) - 1)


# Solution F: Binary search
# Q: Ask ca about the time complexity
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        def isCommonPrefix(strs, length):
            substring = strs[0][:length]
            
            for i in range(1, len(strs)):
                if not strs[i].startswith(substring):
                    return False
            return True
        
        # Binary search
        min_length = len(min(strs, key = len))
        low, high = 1, min_length # Q: why low == 1?
        
        while (low <= high):
            mid = (low + high) // 2
            if isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:high]
        

    
                    
        
