# 1523. Count Odd Numbers in an Interval Range

## Explanation
### Math (Recommended)
1. Construct a variable `nums = high - low + 1`, which is the total amount of numbers in range.
2. The following cases show the result,
- If `nums % 2 = 0`, then there must be exactly half amount of numbers are odd. 
- If `nums % 2 = 1`, then `nums - 1` is even.
Thus, there must be `nums // 2` at least.
 And the number `low`(or `high`) have to be checked if it's odd.
3. Return the result by
- `nums // 2` if `nums % 2 = 0`
- `nums // 2 + (low % 2)` if `nums % 2 = 1`
### one-line
1. Same as `Math`.
2. Combine the **if-condition** in **step 3.** by returning
`nums // 2 + (nums % 2) * (low % 2)`

## Complexity
### Math
- Time: `O(1)`
- Space: `O(1)`
### one-line
- Time: `O(1)`
- Space: `O(1)`

## Result
### Math-python
- Runtimes: 32 ms
> Beats `65.45%`
- Memory: 13.9 MB
> Beats `50.4%`
### Math-cpp
- Runtimes: 0 ms
> Beats `100%`
- Memory: 6 MB
> Beats `63.61%`
### one-line
- Runtimes: 34 ms
> Beats `52.54%`
- Memory: 13.8 MB
> Beats `95.7%`

