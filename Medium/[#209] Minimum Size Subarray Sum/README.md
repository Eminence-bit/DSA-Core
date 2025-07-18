# LeetCode #209: Minimum Size Subarray Sum

## ✅ Problem

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray for which the sum is ≥ `target`. If there is no such subarray, return 0.

## 💡 Idea

Use a sliding window to dynamically adjust the subarray until it meets the target sum condition.

### ✅ Sliding Window Approach

- Expand window by moving `end`
- Shrink window from `start` while sum ≥ target
- Track minimum length during iteration

- Time: O(n)  
- Space: O(1)

## ✍️ Pattern Uses

- Dynamic range-based problems  
- Efficient alternative to prefix sums  
- Real-time constraint checking

## ✅ Code

See [`solution.py`](./optimal.py)
