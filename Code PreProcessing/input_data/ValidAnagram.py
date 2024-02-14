class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 0

        t_dict = {}
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 0

        return s_dict == t_dict
