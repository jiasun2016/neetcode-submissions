class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1️⃣ 找到最大石头重量
        # 后面用 bucket（计数数组）时需要知道范围
        maxStone = max(stones)
        # 2️⃣ bucket[i] 表示“重量为 i 的石头有多少个”
        bucket = [0] * (maxStone + 1)
        # 3️⃣ 统计每种重量的石头数量
        for stone in stones:
            bucket[stone] += 1
        # first：当前考虑的“最大重量”
        # second：用于寻找“第二大重量”的起点
        first = second = maxStone
        # 4️⃣ 只要还有重量 > 0 的石头，就继续模拟碰撞
        while first > 0:
            # 如果当前最大重量的石头数量是偶数，全部抵消
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            # 5️⃣ 当前重量 first 是奇数个
            # 至少会剩下一块，需要找第二大的石头来撞
            # 从 min(second, first-1) 开始往下找
            #剪支：second: 上一轮你可能已经找过first-1小的第二大石头
            j = min(second, first - 1)
            while j > 0 and bucket[j] == 0:
                j -= 1
            # 6️⃣ 如果找不到第二块石头 说明 first 是最后一块石头
            if j == 0:
                return first
            # 记录第二大石头的重量
            second = j
            # 7️⃣ 模拟两块石头相撞
            bucket[first] -= 1
            bucket[second] -= 1
            # 新生成一块重量为 first - second 的石头
            bucket[first - second] += 1
            # 8️⃣ 更新下一轮可能的最大重量
            # 新石头是 first-second，原来 second 可能还剩
            first = max(first - second, second)
        # 9️⃣ 如果所有石头都被抵消，返回 0
        return first
