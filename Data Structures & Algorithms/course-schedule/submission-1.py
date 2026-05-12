class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses 
        adjs = [[] for i in range(numCourses)]
        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            adjs[pre].append(nxt) 
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i) 
        cnt = 0 
        while q:
            cnt += 1 
            curr = q.popleft()
            for nxt in adjs[curr]:
                indegree[nxt] -= 1 
                if indegree[nxt] == 0:
                    q.append(nxt) 
        return cnt == numCourses

