# 119. Pascal's Triangle II

## Explanation
1. Construct a list `result = [1]`.
2. Say the `i-th` row of the pascal's triangle is `(1,...,1)`. The `(i+1)-th` row of the pascal's triangle is `(1,...,1,0) + (0,1,...,1)` (The second term is the reverse of the first term).
> Notice that any row of a pascal's triangle must be palindrome.
Simply make two list for computing the `(i+1)-th` row by `i-th row + [0]` and `[0] + i-th row`.
3. Loops `rowIndex` times to get the result `result`.

## Complexity
- Time: `O(n)`
- Space: `O(n)`

## Result
- Runtimes: 22 ms
> Beats `98.81%`
- Memory: 13.8 MB
> Beats `96.64%`
