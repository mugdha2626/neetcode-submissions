# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs recursive

        # Base case: empty node contributes 0 to depth
        if not root:
            return 0
        
        # Recurse on left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Depth at current node is 1 + max depth of subtrees
        return 1 + max(left_depth, right_depth)



        
        