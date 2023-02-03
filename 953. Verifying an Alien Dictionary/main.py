class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        table = dict(zip(order, alphabet))
        new_words = []
        for word in words:
            alien = ""
            for char in word:
                alien += table[char]
            new_words.append(alien)
        for i in range(len(new_words) - 1):
            if new_words[i] > new_words[i+1]:
                return False
        return True
