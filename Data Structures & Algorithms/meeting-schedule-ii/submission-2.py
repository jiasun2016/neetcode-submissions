"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
     
        ongo =[]
        for interval in intervals:
            ongo.append((interval.start, 1))
            ongo.append((interval.end, -1))
        ongo.sort(key = lambda x: (x[0],x[1]))
        counter = 0
        curr = 0
        for meet in ongo:
            curr += meet[1] 
            counter = max(curr, counter) 
        return counter
