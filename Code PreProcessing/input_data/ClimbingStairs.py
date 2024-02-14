class Solution(object):
    def fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for _ in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
