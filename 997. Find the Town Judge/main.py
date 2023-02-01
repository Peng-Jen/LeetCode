class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_list = [0 for _ in range(n+1)]
        for to_trust, be_trusted in trust:
            trust_list[to_trust] -= 1
            trust_list[be_trusted] += 1
        for index in range(1, n+1):
            if trust_list[index] == n - 1:
                return index
        return -1
