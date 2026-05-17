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
        ans = []
        que = [root]
        while que:
            levels = []
            for i in range(len(que)):
                curr = que.pop(0)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                # if i == len(que)-1:
                #     ans.append(curr.val)
                levels.append(curr.val)
            ans.append(levels[-1])
        return ans 
