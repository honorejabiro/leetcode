class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in matrix:
            if i[0] <= target <= i[-1]:
                res = i[:]
                break

        for i in res:
            if i == target:
                return True

        return False
