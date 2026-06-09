class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = {}
        for each in strs:
            if "".join(sorted(each)) not in output:
                output["".join(sorted(each))] = [each]
            else:
                output["".join(sorted(each))].append(each)

        return output.values()       
