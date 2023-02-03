class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {value: index for index, value in enumerate(order)}
        alien = [tuple(table[i] for i in word) for word in words] 
        for i in range(len(words) - 1):
            if alien[i] > alien[i+1]:
                return False
        return True
