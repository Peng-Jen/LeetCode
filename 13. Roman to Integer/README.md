# 13. Roman to Integer

## Explanation
1. Construct `table = {roman: value}`, `result = 0`.
2. For every index in `s`,
- `result += table[s[index]]` if `table[s[index]] >= table[s[index + 1]]` or `index = len(s) - 1`
- `result -= table[s[index]]` if `table[s[index]] < table[s[index + 1]]`
3. Get the result by returning `result`

## Complexity
- Time: `O(n)`
- Space: `O(n)`
## Result
- Runtimes: 41 ms
> Beats `94.64%`
- Memory: 13.8 MB
> Beats `70.53%`
