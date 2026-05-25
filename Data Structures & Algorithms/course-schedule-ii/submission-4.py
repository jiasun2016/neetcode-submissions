class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = [0] * numCourses
        adjs = [[] for i in range(numCourses) ]
        for nxt, pre in prerequisites:
            adjs[pre].append(nxt)
            pres[nxt] += 1 
        q = deque([])
        for i in range(numCourses):
            if pres[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for adj in adjs[curr]:
                pres[adj] -= 1
                if pres[adj] == 0:
                    q.append(adj) 
        return ans if len(ans) == numCourses else []
