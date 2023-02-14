# 67. Add Binary

## Explanation
### Add by Bits
1. Pad `0` to `a` and `b` such that `len(a) = len(b)`.
2. Construct variables `result = ""` and `carry = 0`.
3. For every bit `i` in `result`, 
    - `bit = (a[i] + b[i] + carry from bit i-1) % 2`
    -  `carry = (a[i] + b[i] + carry from bit i-1) // 2`
4. After `len(a)` times loop, if `carry = 1`, `result += '1'`.
5. Return the `reverse of result` for the result.
### pythonic (Recommended)
1. Use python built-in funtion `bin()` and `int()` to get the result. Since the output value of `bin()` would be like `0b.....`, we return the substring from the second character to the end.


## Complexity
### Add by Bits
- Time: `O(n^2)`
    -`n = max(len(a), len(b))`
- Space: `O(n)`
### pythonic
- Time: `O(n*logn)`
    - `int()` takes `O(n)`
    - `bin()` takes `O(logn)`
- Space: `O(n)`
## Result
### Add by Bits - py
- Runtimes: 40 ms
> Beats `42.93%`
- Memory: 14 MB
> Beats `18.45%`
### Add by Bits - cpp
- Runtimes: 3 ms
> Beats `67.10%`
- Memory: 6.5 MB
> Beats `39.38%`
### pythonic
- Runtimes: 39 ms
> Beats `48.9%`
- Memory: 13.9 MB
> Beats `63.5%`
