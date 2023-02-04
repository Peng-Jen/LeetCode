# 204. Count Primes 

## Explanation
### Number
1. For the **special** cases, return `0`.
> In this problem, the **special** cases are `n <= 2`.
2. Consturct a list `num_list = [0, 1, 2, ..., n]`.
> Note that `num_list[i] = i`
3. Set an int `counter = 0`, `number[0] = 0`, and `number[1] = 0`.
4. For every `num < n`, 
    - If `num = 0`, pass.
    - If `num != 0`, say `num` is a prime, `counter += 1`, and set all the `num_list[multiple of num] = 0`.
5. Get the result by returing `counter`.
### Boolean
1. For the **special** cases, return `0`.
2. Consturct a list `boolean_list = [True, True, ..., True]`.
3. Set `boolean_list[0] = Fale` and `boolean_list[1] = False`.
4. For every `num < n`, 
    - If `num = 0`, pass.
    - If `num != 0`, say `num` is a prime, and set all the `boolean_list[multiple of num] = False`.
5. Get the result by returing `sum(boolean_list)`.

This method costs less memory than `Number` because `int` data type is more memory consuming.

### List-slicing (Recommended)
1. Same as `Boolean` method, but the 4-th step uses list-slicing in python.

This method run much more faster but memory consuming for the slicing list is a copy of original list.

## Complexity
### Number
- Time: `O(n*k)`
    - `n = input num`
    - `k = average for-loop size for (n - 1 - i * i) // n + 1`
- Space: `O(n)`
### Boolean
- Time: `sqrt(n)*k`
- Space: `O(n)`
### List-slicing
- Time: `O((n+k)*sqrt(n))`
- Space: `O(n)`

> It seems that `List-slicing` is more complicated than `Boolean` (maybe I'm wrong with computing the complexity of them). However, **list slicing is much more faster than for-loop**, which can be seen in `Result`.
> I've read some documents but cannot make it clear still. 
> The conclusion is avoiding using for-loop in python programming :)


## Result
### Number
- Runtimes: 5673 ms
> Beats `32.94%`
- Memory: 209.6 MB
> Beats `5%`

### Boolean
- Runtimes: 3342 ms
> Beats `62.59%`
- Memory: 67.6 MB
> Beats `51.14%`

### List-slicing
- Runtimes: 1291 ms
> Beats `91.10%`
- Memory: 115.3 MB
> Beats `5%`
