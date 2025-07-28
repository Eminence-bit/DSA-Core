# LeetCode #424: Longest Repeating Character Replacement

## ✅ Problem

Given a string `s` and an integer `k`, return the length of the longest substring that can be obtained by replacing at most `k` characters to make all characters in the substring the same.

## 💡 Idea

Use the sliding window technique with a frequency map to track character counts in the current window.

### ✅ Sliding Window Approach

- Expand the window by moving `right`
- Track the frequency of characters using a hash map
- Maintain the count of the most frequent character in the window
- If `(window size - max_freq) > k`, shrink the window from the `left`
- Track the maximum valid window size throughout

- **Time:** O(n)  
- **Space:** O(1) (only 26 uppercase letters)

## ✍️ Pattern Uses

- Substring/window optimization under constraints  
- Real-time frequency tracking  
- Classic base for frequency-based window problems

## ✅ Code

See [`solution.py`](./optimal.py)
