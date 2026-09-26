# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #for each level, change the left and right nodes values-> so BFS
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            
            node = q.popleft()

            node.right, node.left = node.left, node.right

            if node.left:         
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return root
            
