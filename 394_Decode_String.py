
# Link: https://leetcode.com/problems/decode-string/

# My solution - follow by Leetcode solution 1 (see the graph)
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        base = 1
        stack = []
        tmp = ""
        res = ""
        
        for string in s:
            if string != "]":
                stack.append(string)
            elif string == "]":
                pop_item = stack.pop()
                if pop_item.isalpha():
                    tmp += pop_item
                elif pop_item == "[":
                    pass
                elif pop_item.isdigit():
                    break
                    num = int(pop_item)
                    stack.append(''.join(reversed(tmp)) * num)
            print("tmp = {} and num = {} and stack = {}".format(tmp, num, stack))
                
#                     tmp *= num
#                     break
#             for i in tmp[::-1]: #Q: 這裡如何讓tmp*num?
#                 stack.append(i)
#             tmp = ""
            
#         for s in stack[::-1]:
#             res += s
#         return res


# Solution from 九章
# class Solution:
#     """
#     @param s: an expression includes numbers, letters and brackets
#     @return: a string
#     """
#     def decodeString(self, s):
#         stack = []
#         for c in s:
#             if c != ']':
#                 stack.append(c)
#                 continue #Q: 為什麼要加continue?
                
#             strs = []
#             while stack and stack[-1] != '[':
#                 strs.append(stack.pop())
            
#             # skip '['
#             stack.pop()
            
#             repeats = 0
#             base = 1  #Q: 不懂為什麼要有base = 1
#             while stack and stack[-1].isdigit():
#                 repeats += repeats * 10 + int(stack.pop())
#             print("repeats = {}, strs = {}, stack = {}".format(repeats, strs, stack))
# #             stack.append(''.join(reversed(strs)) * repeats)
        
# #         return ''.join(stack)
