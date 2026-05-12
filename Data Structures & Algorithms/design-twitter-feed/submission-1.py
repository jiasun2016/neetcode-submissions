class Twitter:
    def __init__(self):
        # 全局时间戳，用来给 tweet 排序
        # 用递减的方式：越新的 tweet，count 越小
        self.count = 0
        # tweetMap:每个用户按时间顺序保存自己发的 tweet
        # userId -> [[count, tweetId], [count, tweetId], ...]
        self.tweetMap = defaultdict(list)
        # followMap:记录每个用户关注了谁
        # userId -> set of followeeId
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # [count, tweetId] 用 count 来表示时间顺序
        self.tweetMap[userId].append([self.count, tweetId])
        # 每发一条 tweet，时间戳递减
        # 保证：越新的 tweet，count 越小
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []          # 最终返回的 10 条 tweetId
        minHeap = []      # 用最小堆合并多个用户的 tweet 流
        # 用户必须看到自己的 tweet
        self.followMap[userId].add(userId)
        # 1️⃣ 初始化 heap：
        # 对 userId 关注的每个用户，取他们“最新的一条 tweet”
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # 该 followee 最新 tweet 的索引
                index = len(self.tweetMap[followeeId]) - 1
                # 取出最新 tweet
                count, tweetId = self.tweetMap[followeeId][index]
                # heap 中存四个信息：
                # [count, tweetId, followeeId, 下一条 tweet 的索引]
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, index - 1]
                )
        # 2️⃣ 从 heap 中不断取“全局最新的 tweet”
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # 当前 tweet 是所有候选中最新的
            res.append(tweetId)
            # 如果这个用户还有更早的 tweet
            # 就把它的“下一条 tweet”放回 heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, index - 1]
                )
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
