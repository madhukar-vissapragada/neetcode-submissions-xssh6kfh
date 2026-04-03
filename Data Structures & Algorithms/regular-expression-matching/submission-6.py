class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s, p, 0, 0)

    def solve(self, s: str, p: str, i: int, j: int) -> bool:
        if j == len(p):
            return i == len(s)

        first_match = (
            i < len(s) and 
            (s[i] == p[j] or p[j] == '.')
        )

        if j + 1 < len(p) and p[j + 1] == '*':
            return (
                self.solve(s, p, i, j + 2) or
                (first_match and self.solve(s, p, i + 1, j))
            )
        else:
            return first_match and self.solve(s, p, i + 1, j + 1)