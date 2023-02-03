# 12. Integer to Roman

## Explanation
### Decimal 
1. Construct 4 lists: `thousands`, `hundreds`, `tens`, `units`. Each list contains 10 elements, each element denotes a number in Roman numeral. 
> It's easy to find any number in Roman numeral by using these table. For example, `4 = units[4]`, `60 = tens[6]`, and thus `64 = tens[6] + units[4]`.
2. Combine the Roman numerals for each digit for `num` and get the result by returning `result`.

### Loops (Recommended)
1. Construct a dictionary `table` for **special integers** in Roman numeral.
> For the digits `1`, `4`, `5` and `9` are "special".
2. Construct a list `sort_key = sorted(table.keys(), reverse = True)`. 
> `sort_key = [1000, 900, 500, ..., 1]`.
3. For each `val` in `sort_key`, while `val <= num`, `result += table[val]` and `num -= val`.
4. After every `val` is considered, get the result by returning `result`.

This method is more **expandable** later on.

## Complexity
### Decimal
- Time: `O(1)`
- Space: `O(l)`
> In general, 
> - Time: `O(logn)`, there will be `logn + 1` terms for all the digits
> - Space: `O(logn)`, there will be `logn + 1` lists for all the digits
### Loops
- Time: `O(1)`
- Space: `O(1)`
> In general, 
> - Time: `O(logn * loglogn)`, the length of `sort_key` is `O(logn)`, to sort `sort_key` taking `O(logn * loglogn)` times
> - Space: `O(logn)`, the length of `sort_key` is `O(logn)`
## Result
### Decimal
- Runtimes: 47 ms
> Beats `87.2%`
- Memory: 13.9 MB
> Beats `74.58%`
### Loops
- Runtimes: 43 ms
> Beats `94.8%`
- Memory: 13.8 MB
> Beats `98.70%`
