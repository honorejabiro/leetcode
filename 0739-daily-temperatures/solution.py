class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        n = len(temperatures)
        res = [0] * n
        while i < n:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                res[temp] = i - temp

            stack.append(i)
            i += 1

        return res
