class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        M = (10 ** 9) + 7

        @cache
        def backtrack(rolls, face, length):

            if rolls == n:
                return 1

            total = 0
            for next_face in range(6):
                if next_face != face:
                    total += backtrack(rolls + 1, next_face, 0)
                elif length + 1 < rollMax[face]:
                    total += backtrack(rolls + 1, face, length + 1)
            
            return total
        
        return backtrack(0, -1, 0) % M

