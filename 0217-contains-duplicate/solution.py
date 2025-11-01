class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set
        # Iterate over the list
        # If number in set return True
        # Else add nunber
        # Return False

        s = set()
        for i in nums:
            if i in s:
                return True
            
            s.add(i)

        return False
