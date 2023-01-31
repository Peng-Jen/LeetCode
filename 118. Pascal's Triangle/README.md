# 118. Pascals's Triangle

## Explanation
### Reverse
1. Construct a list `result = [[1]]`.
2. Say the `i-th` row of the pascal's triangle is `(1,...,1)`. The `(i+1)-th` row of the pascal's triangle is `(1,...,1,0) + (0,1,...,1)`. (The second term is the reverse of the first term)
3. Loop `numRows - 1` times to get the result list.

### Map (Recommended)
1. Same as `Reverse` method but **shorter lines** and **pythonic**.
2. Notice that any row of a pascal's triangle **must be palindrome**. Simply make two list for computing the `(i+1)-th` row by `i-th row + [0]` and `[0] + i-th row`.

## Complexity
### Reverse
- Time: `O(n^2)`
- Space: `O(n^2)`
### Map
- Time: `O(n^2)`
- Space: `O(n^2)`

## Result
### Reverse
- Runtimes: 34 ms
  > Beats `72.68%`
- Memory: 13.7 MB
  > Beats `97.51%`
### Map 
- Runtimes: 30 ms
  > Beats `88.91%`
- Memory: 13.7 MB
  > Beats `97.51%`
