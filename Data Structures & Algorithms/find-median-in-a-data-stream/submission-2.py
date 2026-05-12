class MedianFinder:

    def __init__(self):
        # small：max heap（用负数模拟）
        #   存放较小的一半数字
        self.small = []
        # large：min heap
        #   存放较大的一半数字
        self.large = []

    def addNum(self, num: int) -> None:
        # 1️⃣ 决定 num 应该进哪个 heap
        # 如果 large 非空，且 num 比 large 中最小的还大
        # 说明 num 属于“较大的一半”
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # 否则，放进 small（注意取负数，模拟 max heap）
            heapq.heappush(self.small, -1 * num)
        # 2️⃣ 平衡两个 heap 的大小
        # 如果 small 比 large 多 2 个及以上
        if len(self.small) > len(self.large) + 1:
            # 把 small 中最大的元素移动到 large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # 如果 large 比 small 多 2 个及以上
        elif len(self.large) > len(self.small) + 1:
            # 把 large 中最小的元素移动到 small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # 如果 small 元素更多
        # 中位数就是 small 的最大值
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
