class RecursionBasic:
    
    def nth_fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        else: 
            return self.nth_fibonacci(n-1) + self.nth_fibonacci(n-2)

    def print_fibonacci_series(self, n: int) -> None:
        m = n-1
        while n:
            print(self.nth_fibonacci(m-n+1))
            n -= 1

    def sum_of_n_natural_number(self, n: int) -> int:
        if n < 1:
            raise Exception("Not a valid Input")
        if n == 1:
            return 1
        return n + self.sum_of_n_natural_number(n-1)

    def get_m_power_n(self, m, n):
        if n == 0:
            return 1
        return self.get_m_power_n(m, n-1) * m

    def get_factorial_of_n(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.get_factorial_of_n(n-1)

    def get_nCr(self, n, r):
        if n == r or r == 0:
            return 1
        return self.get_nCr(n-1, r-1) + self.get_nCr(n-1, r)

    def josephus_problem(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.josephus_problem(n-1, k) + k) % n

    def check_if_array_is_sorted(self, arr: list, n: int) -> bool:
        if n <= 1:
            return True
        elif arr[n-1] < arr[n-2]:
            return False
        return self.check_if_array_is_sorted(arr, n-1)
