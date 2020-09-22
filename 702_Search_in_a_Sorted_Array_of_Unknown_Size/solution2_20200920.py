
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
        start, end = 0, 1 # end is not a candidate
        while reader.get(end) < target:
            start = end
            end = end * 2
    
        # Binary Search for three other cases
        while start < end:
            mid = start + (end - start) // 2    #Q: To prevent from overflow
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                start = mid + 1
            elif val > target:
                end = mid - 1
                
        # Q: 為什麼 end 不是 candidate 時需要這兩行？
        if reader.get(start) == target:
            return start
        return -1
    
    
        
class Solution:
    def search(self, reader, target):
        start, end = 0, 0 # end is candidate 從長度一的開始跑起
        while target > reader.get(end):
            start = end + 1
            end = start * 2
        
        while start <= end:
            mid =  start + (end - start) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
