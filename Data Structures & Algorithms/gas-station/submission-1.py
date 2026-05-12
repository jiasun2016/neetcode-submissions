class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果总油量 < 总消耗，不可能绕一圈
        if sum(gas) < sum(cost):
            return -1

        total = 0  # 当前起点出发后的油量余额
        res = 0    # 当前候选起点
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]  # 到达下一个站后的剩余油量

            if total < 0:  # 无法到达下一个站，说明当前起点失败
                total = 0  # 重置油量
                res = i + 1  # 下一个位置作为新的候选起点
        
        return res