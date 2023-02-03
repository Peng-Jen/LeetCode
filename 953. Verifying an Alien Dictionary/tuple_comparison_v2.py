class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {value: index for index, value in enumerate(order)}
        alien = [tuple(table[i] for i in word) for word in words] 
        return all(i <= j for i, j in zip(alien, alien[1:]))
