class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        w = "".join(digits)
        number = int(w)
        number += 1
        w = str(number)
        res = []
        for i in w:
            res.append(int(i))

        return res

        
