# 1137. N-th Tribonacci Number

## Explanation
1. Construct a list `prev_3 = [0, 1, 1]` at the beginning.
2. For every next element `e`, `e` equals the summation of `prev_3`, then append `e` to the back of `prev_3`
3. Refresh `prev_3` to be the last three elements of it.
4. Loops `n-2` times to get the result at `prev_3[-1]`.

Note that the special cases in this problem are
- `n = 0`
- `n = 1`
- `n = 2`

Just return `prev_3[n]` to get the result for given special `n`.

## Complexity
- Time: `O(n)`
- Space: `O(1)`

## Result
- Runtimes: 32 ms 
  > Beats `71.71%`
- Memory: 13.8 MB
  > Beats `95.87%`
