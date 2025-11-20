class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        scheduled = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= scheduled[-1][1]:
                scheduled[-1][1] = max(end, scheduled[-1][1])
            else:
                scheduled.append([start, end])
        
        return scheduled
        
