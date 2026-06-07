class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_duplicate = False
        if len(nums) <= 1:
            return is_duplicate
        nums.sort()
        for i, num in enumerate(nums):
            if nums[i] == nums[i-1]:
                is_duplicate = True
                break
        return is_duplicate