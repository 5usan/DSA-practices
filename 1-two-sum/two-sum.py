class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, item in enumerate(nums):
            hashmap[item] = i
        for i, item in enumerate(nums):
            temp = target - item
            if temp in hashmap and hashmap[temp] != i:
                return [i, hashmap[temp]]
        return []
        
        