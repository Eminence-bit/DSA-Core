class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        start = 0
        min_len = float('inf')

        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                min_len = min(min_len, end - start + 1)
                total -= nums[start]
                start += 1

        return 0 if min_len == float('inf') else min_len
