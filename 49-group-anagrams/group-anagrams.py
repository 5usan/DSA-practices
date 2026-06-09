class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_sorted_strs = {}
        for each in strs:
            if "".join(sorted(each)) not in word_sorted_strs:
                word_sorted_strs["".join(sorted(each))] = [each]
            else:
                word_sorted_strs["".join(sorted(each))].append(each)

        return word_sorted_strs.values()       
