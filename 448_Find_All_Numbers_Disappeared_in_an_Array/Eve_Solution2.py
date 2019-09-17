class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Other people's solution but I don't understand
        # Step 1: If nums[nums[i] - 1] is positive, we make it as a negative number
        # Step 2: If nums[nums[i] - 1] is negative, then remain negative number
        # Step 3: Finally, count how many positive numbers left in this list
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [j + 1 for j in range(len(nums)) if nums[j] > 0]
