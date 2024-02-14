class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = set(["(", "{", "["])
        equivalences = {")": "(", "}": "{", "]": "["}

        openStack = list()

        for char in s:
            if char in opening:
                openStack.append(char)
            else:
                if len(openStack) == 0 or openStack.pop() != equivalences[char]:
                    return False

        return not bool(openStack)
