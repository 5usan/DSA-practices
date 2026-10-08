class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 0):
            return 0
        sorted_list = sorted(list(dict.fromkeys(nums)))
        result = [1]
        for i in range(len(sorted_list)- 1):
            if sorted_list[i] + 1 == sorted_list[i+1]:
                result[len(result) - 1] += 1
            else:
                result.append(1)
        return max(result)
                