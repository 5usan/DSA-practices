class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        o = {}
        for each in strs:
            if "".join(sorted(each)) not in o:
                o["".join(sorted(each))] = [each]
            else:
                o["".join(sorted(each))].append(each)

        return o.values()       
