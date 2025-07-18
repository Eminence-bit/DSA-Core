# LeetCode #217: Contains Duplicate

## 🔍 Problem

Return `True` if any value appears at least twice in the array.

## ✅ Optimal Solution

- Use a `set` to track seen values.
- If a value is already in the set → duplicate found.

## 🔢 Time Complexity

- Time: O(n)
- Space: O(n)

## 💡 Notes

- Avoid brute force: `list.count()` or nested loops = O(n²)
- Sorting + linear check is O(n log n) and less readable

## ✅ Code

See [`solution.py`](./optimal.py)