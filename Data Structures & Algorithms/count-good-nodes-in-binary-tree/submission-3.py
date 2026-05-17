# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        count = 0 
        que = deque([(root, root.val)])
        while que:
            (curr, maxVal) = que.popleft()
            if curr.val >= maxVal:
                count+= 1 
                maxVal = curr.val
            if curr.left:
                que.append((curr.left, maxVal))
            if curr.right:
                que.append((curr.right, maxVal))
        return count 
            

