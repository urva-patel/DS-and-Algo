# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val
        self.dfs(root, target)

        return self.closest
    
    def dfs(self, root, target):
        if not root:
            return
        
        diff = root.val - target

        if abs(diff) < abs(self.closest - target):
            self.closest = root.val

        if abs(diff) == abs(self.closest - target):
            self.closest = min(self.closest, root.val)
        
        if root.val > target:
            self.dfs(root.left, target)
        else:
            self.dfs(root.right, target)
