# LeetCode #1: Two Sum

## Brute Force

- Time: O(n²)
- Approach: Double for loop

## Faulty Semi-Brute

- Uses `in` and `index()` — both O(n) inside loop
- Time: O(n²)

## Optimal (HashMap)

- Time: O(n)
- Space: O(n)
- Idea: Use dictionary to store seen values
