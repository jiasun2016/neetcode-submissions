class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = [0] * numCourses
        adjs = [[] for i in range(numCourses) ]
        for pre, nxt in prerequisites:
            adjs[pre].append(nxt)
            pres[nxt] += 1 
        q = deque([])
        for i in range(numCourses):
            if pres[i] == 0:
                q.append(i)
        cnt = 0
        while q:
            curr = q.popleft()
            cnt += 1
            for adj in adjs[curr]:
                pres[adj] -= 1
                if pres[adj] == 0:
                    q.append(adj) 
        return cnt == numCourses
