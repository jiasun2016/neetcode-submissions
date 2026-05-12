class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjs = [[] for i in range(numCourses)] 
        for nxt, pre in prerequisites:
            indegree[nxt] += 1 
            adjs[pre].append(nxt) 
        res = []
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for nxt in adjs[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt) 
        return res if len(res) == numCourses else []
        