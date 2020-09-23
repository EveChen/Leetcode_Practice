
# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         start, end = 0, len(arr) - 1
#         maximum = max(arr)
        
#         while start <= end:
#             mid = start + (end - start) // 2
#             if arr[mid] == maximum:
#                 return mid
#             elif arr[mid] < maximum: # maximum一定是最大的，所以比arr[mid]大
#                 if arr[mid] > arr[mid + 1]: #判斷現在在山峰的左邊還右邊
#                     end = mid
#                 else:
#                     start = mid
                
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        
        while start < end: #start == end時才會跳出去
            mid = start + (end - start) // 2
            if arr[mid] > arr[mid + 1]:
                end = mid
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1
        return start #因為while條件達成，start==end, 故return end等於return start
        
            
