class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n 
        prices[src] = 0 

        for i in range(k+1):
            nextPrices = list(prices) # price to next stop
            for s, d, p in flights:
                
                nextPrices[d] = min(prices[s] + p, nextPrices[d])  
            prices = nextPrices 
        
        return prices[dst] if prices[dst] != float("inf") else -1
