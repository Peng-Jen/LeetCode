# 953. Verifying an Alien Dictionary

## Explanation
### Change to Normal (Recommended)
1. Construct a string `alphabet = "abcd...xyz`, which is in normal order.
2. Construct a dictionary `table = {alien order: normal order}`.
3. For every `word` in `words`, map every `char` in `word` to **normal order** and append to `new_words`.
4. Return whether all `new_words[i] <= new_words[i+1]`. 

### Tuple Comparison
#### v1
1. Construct a dictionary `table = {alien order: [0, 25]}`.
2. Construct a list `alien` contains tuples for every `word` in `words`.
Each tuple contains the `table[char]` for `char` in `word`.
3. Return whether all `alien[i] <= alien[i+1]`. 
#### v2
1. Same as `Tuple Comparison-v1` method but **shorter lines** and **pythonic**.

## Complexity
### Change to Normal
- Time: `O(n*s)`
    - `n = len(words)`
    - `s = max len(word) for word in words`
- Space: `O(n*s)`
### Tuple Comparison
- Time: `O(n*s)`
- Space: `O(n*s)`

## Result
### Change to Normal
- Runtimes: 33 ms
> Beats `91.10%`
- Memory: 13.9 MB
> Beats `77.53%`
### Tuple Comparion
- Runtimes: 36 ms
> Beats `81.81%`
- Memory: 14.6 MB
> Beats `31.45%`
