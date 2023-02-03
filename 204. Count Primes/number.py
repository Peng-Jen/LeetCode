class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        num_list = [i for i in range(n)]
        counter = 0
        num_list[0], num_list[1] = 0, 0
        for num in num_list:
            if num == 0:
                continue
            counter += 1
            for i in range(num ** 2, n, num):
                num_list[i] = 0
        return counter
