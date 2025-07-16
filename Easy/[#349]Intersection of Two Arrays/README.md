# LeetCode #349: Intersection of Two Arrays

## ❌ Brute Approach

- For each `i` in `nums1`, check if it exists in `nums2`
- Time: O(n × m)

## ✅ Optimal Approach

- Convert both arrays to sets
- Return `list(set1 & set2)`
- Time: O(n + m)
- Space: O(n + m)

## 🧠 Key Insight

Set operations like intersection are the most efficient way to handle uniqueness + membership.
