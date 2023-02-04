# 27. Remove Element
## Explanation
### Naive
1. Remove all `val` in `nums` and return `len(nums)`.
### Counter
1. Construct variables `counter = 0`, `index = 0`, `length = len(nums)`.
2. For every element `e` in `nums`,
    - If `e = val`, remove `e` from `nums` and set `couter += 1`.
    - If `e != val`, set `index += 1`.
3. Return the result `length - counter`
### Switch to the end (Recommended)
1. Construct variables `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`,
    - If `nums[left] = val`, switch the value of `nums[left]` and `nums[right]` and set `right -= 1`.
    - If `nums[left] != val`, `left += 1`.
> Note that the `=` of while condition is necessary. `nums[right]` is the last element should be checked.  
> In this method, `nums[right + 1:] = [val, val, ..., val]`. 
3. Return the result `left`.
## Complexity
### Naive
- Time: `O(n^2)`
- Space: `O(1)`
### Counter
- Time: `O(n^2)`
> The complexity of `pop(index)` is `O(n)`
- Space: `O(1)`
### Switch to the end
- Time: `O(n)`
- Space: `O(1)`

## Result
### Naive
- Runtimes: 42 ms
> Beats `36.55%`
- Memory: 13.8 MB
> Beats `96.33%`
### Naive
- Runtimes: 34 ms
> Beats `78.9%`
- Memory: 13.9 MB
> Beats `55.32%`
### Switch to the end
- Runtimes: 32 ms
> Beats `85.92%`
- Memory: 13.7 MB
> Beats `96.33%`
