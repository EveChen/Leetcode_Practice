
# Link: https://leetcode.com/problems/valid-parentheses/

# Solution A: From Eve, use only stack and if/elif/else
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
        
#         for p in s:
#             if p == "{" or p == "(" or p == "[":
#                 stack.append(p)
#             elif p == "}" or p == ")" or p == "]":
#                 if len(stack) > 0:
#                     if (stack[-1] == "{" and p == "}") or (stack[-1] == "[" and p == "]") or (stack[-1] == '(' and p == ")"):
#                         stack.pop()
#                     else:
#                         return False # prevent case like "(])"
#                 else:
#                     return False # if len(stack) == 0 but we still have p
                                   # 這代表stack裡面已經沒有值了(左括號)，可是p還有值(右括號)
#         if len(stack) == 0:
#             return True
#         else:
#             return False
                    
# Solution B: From CA, use stack and if/elif/else, beautiful solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ["[", "(", "{"]:
                stack.append(p)
            elif len(stack) == 0: #如果stack裡沒有值了(左括號)但還有p(右括號)
                return False
            else: # p in ["]", "}", ")"]
                num = stack.pop()
                res = num + p
                if res not in ["[]", "()", "{}"]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

# Solution C: Use a hashmap and a stack
# 思路: 用stack, 先存左半部，match右半部，有match上的就pop, 最後判斷stack是否為空，是空的話代表全部match上，return True
# class Solution:
#     def isValid(self, s: str) -> bool:
#         hashmap = {")" : "(", "]" : "[", "}" : "{"}
#         stack = []
        
#         for p in s:
#             if p not in hashmap: # p in ["[", "{", "("]，如果p in hashmap，那p = [')', ']', '}']，會return hashmap的key
#                 stack.append(p)
#             else:
#                 if len(stack) != 0 and stack[-1] == hashmap[p]:
#                     stack.pop()
#                 else:
#                     return False
#         return not stack #如果 Stack 是空的，就回傳 True；如果裡面還有剩東西，就回傳 False



# Same as solution C's logic
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Create a dictionary and an empty stack
#         hashmap = {')' : '(', ']' : '[', '}' : '{'}
#         stack = []
        
#         # 第一種 if/elif/else 寫法
#         for p in s:
#             if p not in hashmap:
#                 stack.append(p)
#             elif p in hashmap:
#                 if len(stack) == 0:
#                     return False
#                 elif hashmap[p] == stack[-1]:
#                     stack.pop()
#                 else:
#                     return False
#         return not stack #Q: 這個 return 的位置是在 for loop 之下? 
    
    
    
# Same as solution C's logic
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Create a dictionary and an empty stack
#         hashmap = {')' : '(', ']' : '[', '}' : '{'}
#         stack = []
    
#         for p in s:
#             if p not in hashmap:
#                 stack.append(p)
#             elif p in hashmap:
#                 if len(stack) != 0 and hashmap[p] == stack[-1]:
#                     stack.pop()
#                 else:
#                     stack.append(p)
# 把「不匹配的右括號」也塞進 Stack 裡，好讓最後一行的 if len(stack) == 0 來判定它失敗
#         return not stack 
    

# Same as solution C's logic
# class Solution:
#     def isValid(self, s):
#         stack = []
#         hashmap = {'}' : '{', ')' : '(', ']' : '['}
#         for p in s:
#             if p in hashmap: #case1: 遍歷到} or ) or ]
#                 left_parethsis = stack.pop() if stack else '#'
#                 if left_parethsis != hashmap[p]: #left_parethsis e.g. '[', '(', '{'
#                     return False                 #hashmap[p]: '{', '[', '('
#             else: # case2: 遍歷到{ or ( or [ or 其他符號
#                 stack.append(p)
#         return not stack

                
