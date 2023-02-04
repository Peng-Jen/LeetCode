# 35. Search Insertion Position

## Explanation
1. Construct two variables `left = 0`, `right = len(nums)` for **binary search**.
2. Check **special cases**,
    - If `target > nums[right]`, push `target` back to `nums`. Return `right + 1`.
    - If `target = nums[right]`, return `right`.
    - If `targer <= nums[left]`, insert `target` to `nums`. Return `0`.
3. Implement **Binary Search**, set `mid = (left + right) // 2` and return early if `nums[mid] = target`.
4. Return `left` as wanted result.

## Complexity
- Time: `O(logn)`
- Space: `O(1)`

## Result
- Runtimes: 43 ms
> Beats `97.32%`
- Memory: 14.6 MB
> Beats `98.65%`
