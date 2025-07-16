class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        for i in nums1:
            if i in nums2:
                seen.add(i)
        return list(seen)