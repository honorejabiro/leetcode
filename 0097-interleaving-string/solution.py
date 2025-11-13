class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if not s3:
            return True

        l1, l2 = len(s1), len(s2)
        length = len(s3)

        if l2 > length or l1 > length:
            return False

        answer = False
        a_used, b_used = False, False

        if not s1:
            a_used = True
        
        if not s2:
            b_used = True
        
        @lru_cache
        def f(i, j):

            nonlocal answer
            nonlocal a_used
            nonlocal b_used

            k = i + j

            if k == length:
                if a_used and b_used:
                    answer = True
                return True
            
    
            # Try s1
            if i < l1 and s1[i] == s3[k]:
                path.append(s1[i])
                a_used = True
                if f(i + 1, j):
                    return True
                else:
                    path.pop()
            
            # Try s2  
            if j < l2 and s2[j] == s3[k]:
                b_used = True
                path.append(s2[j])
                if f(i, j + 1):
                    return True
                else:
                    path.pop()
    
        
        f(0, 0)
        return answer
