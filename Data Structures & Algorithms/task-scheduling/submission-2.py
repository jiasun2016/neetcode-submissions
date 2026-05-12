class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每种任务出现的次数
        count = Counter(tasks)

        # 2. 用负数构建 max heap（Python 只有 min heap）
        #    heap 中的数表示：某个任务还剩多少次（负数）
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        # 3. 当前 CPU 时间
        time = 0
        # 4. 冷却队列，保存正在冷却的任务
        #    每个元素是 [cnt, readyTime]
        #    cnt: 该任务还剩多少次（负数）
        #    readyTime: 这个任务最早可以再次执行的时间
        q = deque()
        # 5. 只要还有任务没执行完（可执行的 or 冷却中的）
        while maxHeap or q:
            # 每一轮表示一个 CPU 时间单位
            time += 1
            # 6. 如果当前没有任何可执行的任务
            #    说明所有任务都在冷却，CPU 只能 idle
            if not maxHeap:
                # 直接把时间跳到最近一个任务冷却结束的时间
                time = q[0][1]
            else:
                # 7. 从 heap 中取出剩余次数最多的任务执行一次
                #    +1 表示执行了一次（因为 cnt 是负数）
                cnt = 1 + heapq.heappop(maxHeap)
                # 8. 如果这个任务还没执行完
                #    把它放入冷却队列，等待 n 个时间单位
                if cnt:
                    q.append([cnt, time + n])
            # 9. 如果有任务冷却完成（readyTime == 当前时间）
            #    把它重新放回 heap，变成可执行状态
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        # 10. 所有任务执行完，返回总时间
        return time
