class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        max_freq = 0
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # window size - max_freq > k => shrink
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
