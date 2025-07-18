# LeetCode #3: Longest Substring Without Repeating Characters

## ✅ Problem

Given a string `s`, return the length of the longest substring without repeating characters.

## 💡 Idea

Use the sliding window technique with a `set` to track unique characters in the current window.

### ✅ Sliding Window Approach

- Expand the window by moving `right`
- If a duplicate is found, move `left` and remove from the set
- Track maximum window size during iteration

- Time: O(n)  
- Space: O(k) where `k` is the charset size (e.g., 128 for ASCII)

## ✍️ Pattern Uses

- Substring/window analysis  
- Duplicate removal in real-time  
- Foundation for many sliding window problems

## ✅ Code

See [`solution.py`](./optimal.py)
