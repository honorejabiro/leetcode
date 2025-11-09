class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        answer = ""
        kth = 0

        def dfs(number, seq):

            nonlocal kth
            nonlocal answer
            if len(seq) == n:
                kth += 1
                return

            for j in range(1, n + 1):
                if j == number or j in seq:
                    continue
                seq.append(j)
                dfs(j, seq)
                if kth == k:
                    answer = seq.copy()
                    return
                seq.pop()

        dfs(0, [])
        return "".join(str(x) for x in answer)

