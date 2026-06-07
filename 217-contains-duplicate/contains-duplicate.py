class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_duplicate = False
        length = len(nums)
        if length <= 1:
            return is_duplicate
        nums.sort()
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                is_duplicate = True
                break
        return is_duplicate