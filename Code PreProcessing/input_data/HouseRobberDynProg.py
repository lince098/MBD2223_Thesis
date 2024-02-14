class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 2:
            return max(nums)

        k = 2
        results = [0] * len(nums)
        results[0], results[1] = nums[0], nums[1]

        while k < len(nums):
            results[k] = max(results[k - 1], max(results[: k - 1]) + nums[k])
            k += 1

        return results[k - 1]
