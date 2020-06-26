#Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                nums[i-count] = nums[i]
        return len(nums) - count