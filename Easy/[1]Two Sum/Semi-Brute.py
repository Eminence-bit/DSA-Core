class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            complement = target - num
            if complement in nums:
                if nums.index(complement)!=i:
                    return [nums.index(complement),i]
        return [0,1]
        