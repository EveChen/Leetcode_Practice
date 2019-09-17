class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Although this solution passed, it seems like I use an extra space?!
        return list(set(range(1, len(nums) + 1)) - set(nums))
