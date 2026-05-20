class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        vals = self.dic[key]
        l, r = 0, len(vals)-1
        while l + 1 < r:
            mid = l + (r-l)//2 
            if vals[mid][1] == timestamp:
                return vals[mid][0]
            elif vals[mid][1] > timestamp:
                r = mid 
            else:
                l = mid 
        if vals[r][1] == timestamp:
            return vals[r][0]
        if vals[l][1] == timestamp:
            return vals[l][0]
        if vals[r][1] < timestamp:
            return vals[r][0]
        if vals[l][1] < timestamp:
            return vals[l][0]
        return ""
        
