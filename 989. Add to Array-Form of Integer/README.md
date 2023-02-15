# 989. Add to Array-Form of Integer

## Explanation
### Naive
1. Construct variables `power = len(num)`, `result = 0`, `standard = 0`.
2. Compute the number of given `num`, and let `result = the number`.
3. `result += k`.
4. Return the array-form of `result`.
### One-line (Recommended)
1. Use bulit-in funtion in python to get the result.
2. Different from **step 2** in `Naive`, use `join()` to turn `list` into `str`, and use `int()` to turn `str` into `int` directly.

## Complexity
### Naive
- Time: `O(log(max(N, k)))`
    - `N is the number of num in digit-form`
- Space: `O(log(max(N, k)))`
### One-line
- Time: `O(log(max(N, k)))`
    - `N is the number of num in digit-form`
- Space: `O(log(max(N, k)))`

## Result
### Naive
- Runtimes: 501 ms
> Beats `31.22%`
- Memory: 15.2 MB
> Beats `36.53%`
### One-line
- Runtimes: 315 ms
> Beats `71.21%`
- Memory: 15.2 MB
> Beats `36.53%`
