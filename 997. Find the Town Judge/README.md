# 997. Find the Town Judge

## Explanation
1. Constuct a list `trust_list = [0, 0, ...]` to calculate the **score** for every person in the town.
2. For every pair `[to_trust, be_trusted]` in `trust`, the one who trusts other will get `-1` and the one be trusted will get `1` point.
3. The judge is the person who got `n-1` points, which is equivalent to that he/she is trusted by the others and doesn't trust any of them.
4. If such a judge exists, return `index`, or return `-1` if there's no such person.

## Complexity
- Time: `O(n+T)`
> `n = num of people`, `T = len(trust)`
- Space:`O(n)`

## Result
- Runtimes: 752 ms
> Beat `82.54%`
- Memory: 18.8 MB
> Beat `91.26%`
