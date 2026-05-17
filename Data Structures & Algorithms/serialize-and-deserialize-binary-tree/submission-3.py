# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ""
        if not root:
            return ans
        que = [root]
        while que:
            curr = que.pop(0)
            if curr: 
                ans+= str(curr.val) + ","
                que.append(curr.left)
                que.append(curr.right) 
            else:
                ans+= "#" + ","
        return ans 
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None 
        data = data.split(",")
        root = TreeNode(int(data[0]))
        i = 1 
        que = [root]
        while que:
            curr = que.pop(0)
            if data[i] != "#":
                curr.left = TreeNode(int(data[i]))
                que.append(curr.left)
            i += 1 
            if data[i] != "#":
                curr.right = TreeNode(int(data[i]))
                que.append(curr.right) 
            i += 1 
        return root 

            
            

            

        
