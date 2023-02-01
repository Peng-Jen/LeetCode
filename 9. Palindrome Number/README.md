# 9. Palindrome Number

## Explanation 
### One-line
1. If `x < 0`, return `False`. 
2. Use string slicing to check whether input `str(x)` is palindrome.
### Math
1. If `x < 0`, return `False`. 
2. Construct two variables `result = 0`, `p = x`.
3. The main process is to make `result = x in reverse` without string method.
4. Get the result by checking whether `result = x`.
### String
1. If 'x < 0', return `False`.
2. Construct `str_x = str(x)`
3. To check whether `str_x[index] = str_x[~index]`, return `False` if not.
4. Loops `len(str_x) // 2` times is enough. Since for any number greater or equal to, it's **Two's complement** is less or equal to itself, which means it has been checked before. 

## Complexity
### One-line
- Time: `O(n)`
- Space: `O(n)`
### Math
- Time: `O(n)`
- Space: `O(n)`
### String
- Time: `O(n)`
- Space: `O(n)`
## Result
### One-line
- Runtimes: 60 ms
> Beats `80.83%`
- Memory: 13.7 MB
> Beats `99.92%`
### Math
- Runtimes: 60 ms
> Beats `80.83%`
- Memory: 13.8 MB
> Beats `53.41%`
### String
- Runtimes: 56 ms
> Beats `88.86%`
- Memory: 13.8 MB
> Beats `95.43%`
