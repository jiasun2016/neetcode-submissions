class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return "" 
        vals = self.keyStore[key] 
        l, r = 0, len(vals)-1
        while l + 1 < r:
            mid = l + (r-l)//2 
            time = vals[mid][1] 
            if time > timestamp:
                r = mid 
            elif time < timestamp:
                l = mid 
            else:
                return vals[mid][0]  
        if vals[l][1] == timestamp:
            return vals[l][0] 
        if vals[r][1] == timestamp:
            return vals[r][0]  
        if vals[r][1] < timestamp:
            return vals[r][0] 
        if vals[l][1] < timestamp:
            return vals[l][0]
        return ""

        
        
