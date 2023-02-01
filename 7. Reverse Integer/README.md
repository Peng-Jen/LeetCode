# 7. Reverse Integer
## Explanation
### Math-py
> Ignore the constraints **32-bit integers only**
1. If `x < 0`, `is_negative = True`.
2. Construct two variables `result = 0, p = x`.
3. The main process is to make `result = |x| in reverse`.
4. Check whether `result` is overflow under 32-bit integer.
- If `x >= 0`, `is_negative = False`. Then `result >= 2^31` will be overflow.
- If `x < 0`. Then `result <= 2^31 + 1` will be overflow.
5. If overflow, return `0`. If not, get the result by returning `result * (1 - 2 * is_negative)` (The second term is in `[1, -1]`, which show the sign for any given number).
### Math-cpp (Recommended)
1. If `x < 0`, `is_negative = True`.
2. Construct two variables `result = 0, p = x`.
3. Since `INT_MIN` is invalid input for `abs()`, check whether `x = INT_MIN` first.
- If `x = INT_MIN`, return `0`. It will be overflow since `|x| = INT_MAX + 1 > INT_MAX`
4. The main process is to make `result = |x| in reverse`.  
For every loop, we expected to let `result = 10 * result + p % 10` and then let `p = p / 10`.
- If `10 * result` will be overflow, return `0`.
- If `result + p % 10 ` will be overflow, return `0`.
5. Get the result by returning `result * (1 - 2 * is_negative)` (The second term is in `[1, -1]`, which show the sign for any given number).
## Complexity
### Math-
- Time: `O(n)`
- Space: `O(1)`
### Math-
- Time: `O(n)`
- Space: `O(1)`
## Result
### Math-py
- Runtimes: 35 ms
> Beats `72.32%`
- Memory: 13.7 MB
> Beats `99.95%`
### Math-cpp
- Runtimes: 3 ms
> Beats `60.27%`
- Memory: 5.9 MB
> Beats `61.94%`
