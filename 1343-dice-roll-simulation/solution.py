class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(maxsize=None)
        def f(face, consecutive, length):

            if length == n:
                return 1

            total = 0
            for nxt in range(1, 7):
                if nxt == face:
                    if consecutive < rollMax[face - 1]:
                        total += f(face, consecutive + 1, length + 1)
                else:
                    total += f(nxt, 1, length + 1)

            return total

        count = 0
        for i in range(1, 7):
            count += f(i, 1, 1)

        return count % (10**9 + 7)

