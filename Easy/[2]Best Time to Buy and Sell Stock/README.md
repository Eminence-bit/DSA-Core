# LeetCode #121: Best Time to Buy and Sell Stock

## 🔍 Problem

Buy low, sell high. Only 1 transaction allowed. Maximize profit.

## ❌ Brute Force

- Try all pairs: Time O(n²)
- Space O(1)

## ✅ Optimal (Kadane’s Inspired)

Track:

- `min_so_far`: lowest seen price
- `profit`: max(current price - min_so_far)
- Time: O(n), Space: O(1)

## 💡 This is Kadane's, adapted to tracking **max difference**
