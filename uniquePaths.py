class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # I will try to resolve this question using recursion
        # and keeping results in the set

        if not m or not n:
            return 0

        if m == 1 and n == 1:
            return 1

        # The calculation will be in the opposite direction,
        # because the total paths are the same.
        total = self.uniquePaths(m-1, n)
        total += self.uniquePaths(m, n-1)

        return total
