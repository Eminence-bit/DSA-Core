# 🧠 3Sum

**LeetCode #15 — Medium**

---

## 📝 Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j != k`
- `nums[i] + nums[j] + nums[k] == 0`
- Triplets must not be duplicates

---

## 💡 Approach

- Sort the array
- Use a fixed element + two-pointer approach
- Skip duplicates to avoid repeated triplets

---

## 🔍 Time & Space Complexity

- Time: `O(n^2)`
- Space: `O(1)` (excluding result)

---

## ✅ Code

See [`solution.py`](./optimal.py)

---
