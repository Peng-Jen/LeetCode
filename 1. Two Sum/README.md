# 1. Two Sum

## Explanation

### Naive
1. Calculate `remaining = target - nums[index]`.
2. Set `nums[index] = None` to avoid same element be selected twice.
3. Find the index of `remaining` in `nums`.
4. Return the result `[index, index of remaining in nums]`

### Binary Search
1. Enumerate the list `nums`.
2. Sort the list `nums` by the value of each element.
3. For any given index, set `index = index + 1` if one of situations satisfied
  - `nums[index][1] + nums[index + 1][1] > target`
  - `nums[index][1] + nums[-1][1] < target`
4. Implement **binary search** to find whether the `remaining` exist in `nums[index + 1:]`.
5. Return the result `[nums[index][0], nums[mid][0]]`, where `mid` is a variable created in binary search part.

### Dictionary look up (Recommended)
1. Construct an empty dictionary `buffer`.
2. For any given index, check whether `nums[index]` in the `buffer`.
3. If not, set `buffer[remaining] = index`.
4. If yes, return the result `[buffer[remaining], index]`.
> `buffer` stores every seen index as value and wanted value as key, i.e. `{remaining: index}`.

Since it guarantees that there is always **exactly one solution** for each input, no special case need to be considered.

## Complexity

### Naive
- Time: `O(n^2)`
- Space: `O(n)`
### Binary Search
- Time: `O(n*logn)`
- Space: `O(n)`
### Dicitonary look up
- Time: `O(n)`
- Space: `O(n)`


## Result
### Naive
- Runtimes: 623 ms 
  > Beats `38.14%`
- Memory: 14.8 MB
  > Beats `92.91%`
### Binary Search
- Runtimes: 73 ms
  > Beats `62.5%`
- Memory: 15.5 MB
  > Beats `7.38%`
### Dictionary look up
- Runtimes: 56 ms
  > Beats `95.87%`
- Memory: 15.5 MB
  > Beats `7.38%`
