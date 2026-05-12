# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            lev = []
            lens = len(que)
            for i in range(lens):
                n = que.popleft()
                lev.append(n.val)
                if n.left:
                    que.append(n.left)
                if n.right:
                    que.append(n.right) 
            res.append(lev)
        return res