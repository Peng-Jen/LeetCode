class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        num_list = [True for _ in range(n)]
        num_list[0], num_list[1] = False, False
        for num in range(int(n ** 0.5) + 1):
            if num_list[num] == False:
                continue
            num_list[num * num:n:num] = [False] * ((n - 1 - num ** 2) // num + 1)
        return sum(num_list)
    
