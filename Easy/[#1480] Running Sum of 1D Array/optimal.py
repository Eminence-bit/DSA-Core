class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        current_sum = 0
        for i in nums:
            current_sum += i
            result.append(current_sum)
        return result