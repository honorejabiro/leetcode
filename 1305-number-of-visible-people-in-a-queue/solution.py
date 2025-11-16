class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        stack = []
        n = len(heights)
        answer = [0] * n

        for i in range(n - 1, -1, -1):

            while stack and stack[-1] < heights[i]:
                stack.pop()
                answer[i] += 1
            
            if stack:
                answer[i] += 1
            
            stack.append(heights[i])
        
        return answer
