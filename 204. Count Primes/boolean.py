class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        boolean_list = [True for _ in range(n)]
        boolean_list[0], boolean_list[1] = False, False
        for index in range(int(n ** 0.5) + 1):
            if boolean_list[index] == False:
                continue
            for i in range(index ** 2, n, index):
                boolean_list[i] = False
        return sum(boolean_list)
