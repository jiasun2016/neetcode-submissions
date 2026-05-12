class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = [] 
        self.keyStore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key,[])  
        if not values:
            return ""
        l, r = 0, len(values) -1
        while l + 1 < r: 
            mid = (l+r)//2 
            time = values[mid][1] 
            if time == timestamp:
                return values[mid][0]  
            elif time < timestamp: 
                l = mid 
            else:
                r = mid 

        if values[l][1] == timestamp:
            return values[l][0] 
        if values[r][1] == timestamp:
            return values[r][0]
        if values[r][1] < timestamp:
            return values[r][0]  
        if values[l][1] < timestamp:
            return values[l][0]   
        return ""

        



        
