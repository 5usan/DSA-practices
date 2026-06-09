class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        temp_dist = {}
        for i, num in enumerate(nums):
            temp_dist[num] = i

        print(temp_dist)
        for i, value in enumerate(nums):
            compliment = target - value
            if compliment in temp_dist and i != temp_dist[compliment]:
                return [i, temp_dist[compliment]]
                
        return []


