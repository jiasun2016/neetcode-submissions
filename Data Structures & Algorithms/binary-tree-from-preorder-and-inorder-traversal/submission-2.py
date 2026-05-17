# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxmap ={val: idx for idx, val in enumerate(inorder)}
        self.rootIndex = 0 
        def dfs(l, r):
            if l > r:
                return 
            rootVal = preorder[self.rootIndex]
            root = TreeNode(rootVal) 
            self.rootIndex += 1 
            mid = idxmap[rootVal] 
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(preorder)-1)