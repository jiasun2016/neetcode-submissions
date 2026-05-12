# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root]) 
        ans = []
        while queue:
            lens = len(queue)
            level = []
            for i in range(lens):
                node = queue.popleft() 
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right) 
                level.append(node.val) 
            ans.append(level[-1]) 
        return ans