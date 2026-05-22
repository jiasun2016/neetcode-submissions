class Twitter:

    def __init__(self):
        self.time = 0 
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for id in self.followMap[userId]:
            if id not in self.tweetMap:
                continue 
            index = len(self.tweetMap[id]) -1 
            time, tweetId, = self.tweetMap[id][index]
            heapq.heappush(minHeap, [time, tweetId, id, index-1])
        while minHeap and len(res) < 10:
            time, tweetId, id, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[id][index]
                heapq.heappush(minHeap, [time, tweetId, id, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
            
