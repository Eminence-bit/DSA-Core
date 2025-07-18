# 🧱 Container With Most Water

**LeetCode #11 — Medium**

---

## 📝 Problem

Given `n` non-negative integers `height[i]`, where each represents the height of a vertical line on the x-axis, find two lines that form a container which holds the **maximum amount of water**.

---

## 💡 Approach

- Use two pointers: one at the beginning, one at the end
- Calculate area = `min(height[left], height[right]) * (right - left)`
- Move the pointer with smaller height inward
- Track the max area

---

## 🔍 Time & Space Complexity

- Time: `O(n)`
- Space: `O(1)`

---

## ✅ Code

See [`solution.py`](./optimal.py)

---

## 📚 Related Patterns

- Two Pointer Optimization
- Greedy Scan
