class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        results = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = length - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < 0:
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return results
