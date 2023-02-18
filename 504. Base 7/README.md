# 504. Base 7

## Explanation
1. Construct a variable `is_nwgative = num < 0`.
2. Let `num = divmod(abs(num), 7)`.
    - `c = divmod(a, b)` return `(a // b, a % b)`.
3. While `num[0] > 0`, let `num // 7` and pad `n % 7` into the begin of the result.
4. Return the result, if `is_negative`, pad `-` into the begin of the result. 

## Complexity
- Time: `O(logn)`
- Space: `O(1)`

## Result
- Runtimes: 32 ms
> Beats `68.66%`
- Memory: 14 MB
> Beats `95.71%`
