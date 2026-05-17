# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dummy = TreeNode(-1, None, root)
        stack = [dummy]
        curr = root
        while stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            # 核心修正：如果弹出的节点是 dummy，说明真实的整棵树已经彻底遍历完了
            if curr == dummy:
                # 即使 k 还没减到 0（例如 k 超过了树的节点总数），也必须安全退出，避免死循环
                break
            k -= 1
            if k == 0:
                return curr.val
            # 如果当前节点是真正的根节点（root），在它转向右子树前，
            # 斩断 dummy 到它的连接，防止后续通过 dummy 再次重复遍历
            if curr == root:
                dummy.right = None
            curr = curr.right        