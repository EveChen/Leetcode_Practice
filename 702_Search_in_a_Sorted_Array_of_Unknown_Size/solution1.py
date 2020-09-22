
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#     def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Case 1: If the target is the value on the 0 index
        if reader.get(0) == target:
            return 0
        
        # Set the boundary first (i.e. set an endpoint)
        start, end = 0, 1
        while reader.get(end) < target:
            start = end
            end = end * 2
    
        # Binary Search for three other cases
        while start < end:
            mid = start + (end - start) // 2    # To prevent from overflow
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                start = mid + 1
            elif val > target:
                end = mid - 1
                
        # Q: 為什麼不需要這兩行？
        if reader.get(start) == target:
            return start
        return -1
    
    
        # 題目說：You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
        # Q: 要怎麼處理 less than 10000
