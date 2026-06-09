class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = {}
        for each in strs:
            sorted_word = "".join(sorted(each))
            if sorted_word not in output:
                output[sorted_word] = [each]
            else:
                output[sorted_word].append(each)

        return output.values()       
