# LeetCode #1480: Running Sum of 1D Array

## ✅ Problem

Given an array `nums`, return the running sum of `nums`.

## 💡 Idea

This is a prefix sum — each index stores the sum of all previous elements.

### ✅ Normal Version

- Use a separate result list
- Time: O(n), Space: O(n)

### ⚡ In-Place Version

- Modify `nums` as we go
- Time: O(n), Space: O(1)

## ✍️ Prefix Sum Uses

- Subarray sums
- Range queries
- Preprocessing for DP
