# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node, minVal=-float('inf'), maxVal=float('inf')):
            if not node: return True
            if node.val >= maxVal or node.val <= minVal: return False
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)

        return dfs(root)