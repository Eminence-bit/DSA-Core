class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,num in enumerate(nums):
            complement = target - num
            if complement in nums:
                if nums.index(complement)!=i:
                    return [nums.index(complement),i]
        return [0,1]
        