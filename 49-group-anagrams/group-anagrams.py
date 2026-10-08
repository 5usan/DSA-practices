class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for each in strs:
            temp = "".join(sorted(each))
            if temp in hashmap:
                hashmap[temp].append(each)
            else:
                hashmap[temp] = [each]
        result = []
        for key, value in hashmap.items():
            result.append(value)
        return result