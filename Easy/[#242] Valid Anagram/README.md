# LeetCode #242: Valid Anagram

## 🔍 Problem

Check if two strings are anagrams (same letters, same count).

## ❌ Sorting Approach

- Sort both strings, compare
- Time: O(n log n)

## ✅ Optimal (HashMap Frequency Count)

- Count characters in `s`, subtract using `t`
- Time: O(n), Space: O(1)

## 💡 Notes

- Use `defaultdict` for easy frequency tracking
- Efficient for large inputs or advanced variants
