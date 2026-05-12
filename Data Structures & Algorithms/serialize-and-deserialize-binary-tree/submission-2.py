# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        res = []
        que = deque([root])
        while que:
            node = que.popleft()
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                res.append("#")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "#":
            return None 
        root = TreeNode(int(vals[0]))
        que = deque([root])
        index = 1
        while que:
            node = que.popleft()
            if vals[index] != "#":
                node.left = TreeNode(int(vals[index]))
                que.append(node.left)
            index += 1 
            if vals[index] != "#":
                node.right = TreeNode(int(vals[index]))
                que.append(node.right) 
            index += 1  
        return root 


            
