class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dist = {}
        n = len(nums)
        for i in range(n):
            temp_dist[nums[i]] = i

        for i in range(n):
            compliment = target - nums[i]
            if compliment in temp_dist and i != temp_dist[compliment]:
                return [i, temp_dist[compliment]]
                
        return []
