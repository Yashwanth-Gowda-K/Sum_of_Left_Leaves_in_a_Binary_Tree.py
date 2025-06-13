# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
        
                if not node.left.left and not node.left.right:
                    result += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
