class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        top_K_frequent_tuples = sorted(hashmap.items(), key = lambda x : x[1], reverse = True)[:k]
        top_k_element = []
        for i in top_K_frequent_tuples:
            top_k_element.append(i[0])
        return top_k_element
        