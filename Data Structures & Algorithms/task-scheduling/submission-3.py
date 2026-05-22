class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            a = ord('A')
            count[ord(t)- a] += 1
        maxFreq = max(count) 
        maxFreqCount = 0
        for freq in count:
            if maxFreq== freq:
                maxFreqCount += 1 
        # (max_freq - 1) 个大小为 (n + 1) 的分组，加上最后一组中剩余的任务数
        time = (n+1) * (maxFreq-1) + maxFreqCount
        # 与实际任务总数取最大值，防止框架被“撑爆”
        return max(time, len(tasks))