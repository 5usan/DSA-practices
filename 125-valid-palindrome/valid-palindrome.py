class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        upper_cased = "".join(char for char in s if char.isalnum()).upper()
        reversed_string = upper_cased[::-1]
        if(upper_cased == reversed_string):
            return True
        else:
            return False 
        