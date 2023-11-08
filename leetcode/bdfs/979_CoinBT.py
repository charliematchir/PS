# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def postOrder(node):
            if not node:
                return 0

            left = postOrder(node.left)
            right = postOrder(node.right)
            self.res += abs(left) + abs(right)
            return node.val + right + left - 1

        postOrder(root)
        return self.res


