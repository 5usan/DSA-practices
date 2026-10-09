class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, item in enumerate(numbers):
            hashmap[item] = i + 1
        for i, item in enumerate(numbers):
            temp = target - item
            if temp in hashmap and hashmap[temp] != i:
                return [i+1, hashmap[temp]]
        return []
        