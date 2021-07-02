
# Link: https://leetcode.com/problems/reverse-linked-list/

# Solution A: iteration (還不懂)
# 思路: 在原鏈表之前建立一個空的newHead，因為首節點會變，然後從head開始，將之後的一個節點移到newHead之後，重復此操作直到head成為末節點為止
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        return prev
        

