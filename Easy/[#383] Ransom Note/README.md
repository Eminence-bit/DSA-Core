# LeetCode #383: Ransom Note

## 🔍 Problem

Return True if you can construct `ransomNote` using letters from `magazine`.

---

## ❌ Approach 2: `.count()` in loop

- Simple but inefficient
- Time: O(n²)
- Not suitable for interviews

---

## ✅ Approach 1: Two Frequency Maps

- Count characters in both strings
- Compare frequencies
- Time: O(n + m)
- Space: O(1)

---

## ✅ Optimal: Single Map + Decrement

- Count `magazine` frequency
- Decrease while iterating `ransomNote`
- Return False if any count goes negative
- Time: O(n + m)
