from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        value = -float('inf')
        answer = depth = 1
        q = deque([root])
        while q:
            size = len(q)
            v = 0
            for _ in range(size):
                node = q.popleft()
                v += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if v > value:
                value = v
                answer = depth
            depth += 1
        return answer