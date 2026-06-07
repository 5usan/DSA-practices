class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return True if s_sorted == t_sorted else False
    