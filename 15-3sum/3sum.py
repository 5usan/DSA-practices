class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        s = set()
        for i in range(length):
            current_element = nums[i]
            l = i + 1
            r = length - 1
            while l < r:
                if current_element + nums[l] + nums[r] == 0:
                    s.add((current_element, nums[l], nums[r]))
                    l+=1
                    r-=1
                elif current_element + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
        return list(s)
