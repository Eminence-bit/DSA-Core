# LeetCode #344: Reverse String

## 🔍 Problem

Reverse the array of characters **in-place**.

---

## ✅ Approach 1: Middle Swap

- Swap `s[i]` with `s[n - 1 - i]` for first half of string
- Time: O(n), Space: O(1)

## ✅ Approach 2: Two Pointers

- Initialize `left = 0`, `right = n - 1`
- Swap `s[left]` and `s[right]`, then move pointers
- Time: O(n), Space: O(1)

## 💡 Notes

- Two-pointer method is more readable and generalizable

## ✅ Code

See [`Two Pointer Approach`](./two_pointer.py)
See [`Mid Pointer Approach`](./mid_swap.py)
