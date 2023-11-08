# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    answer = chr(123)

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, st):
            if not node.left and not node.right:
                st = chr(node.val + 97) + st
                self.answer = min(self.answer, st)
                return

            if node.left:
                dfs(node.left, chr(node.val + 97) + st)

            if node.right:
                dfs(node.right, chr(node.val + 97) + st)
            return

        dfs(root, "")
        return self.answer

