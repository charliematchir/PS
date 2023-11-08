# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # q = deque([root.left, root.right])
        # level = 1
        # while q:
        #     if level % 2 != 0:
        #         if q[0] is None:
        #             return root
        #         l, r = 0, len(q) - 1
        #         while l < r:
        #             q[l].val, q[r].val = q[r].val, q[l].val
        #             l += 1
        #             r -= 1
        #
        #     if q[0].left is None:
        #         return root
        #     size = len(q)
        #     for _ in range(size):
        #         node = q.popleft()
        #         q.append(node.left)
        #         q.append(node.right)
        #     level += 1
        # return root

        # q = deque([root.left, root.right])
        # tmp = deque()
        # dq = deque()
        # level = 1
        # while q or tmp:
        #     if level % 2 != 0:
        #         tmp = deque()
        #         if q[0] is None:
        #             return root
        #
        #         while q:
        #             l, r = q.popleft(), q.pop()
        #             temp = l.val
        #             l.val = r.val
        #             r.val = temp
        #             dq.append(r)
        #             tmp.append(l.left)
        #             tmp.append(l.right)
        #
        #         while dq:
        #             node = dq.pop()
        #             tmp.append(node.left)
        #             tmp.append(node.right)
        #
        #     else:
        #         if tmp[0] is None:
        #             return root
        #         while tmp:
        #             node = tmp.popleft()
        #             q.append(node.left)
        #             q.append(node.right)
        #     level += 1
        #
        # return root
        # def dfs(l, r, cnt):
        #     if l is None:
        #         return
        #
        #     if cnt == 0:
        #         l.val, r.val = r.val, l.val
        #         dfs(l.left, r.right, 1)
        #         dfs(l.right, r.left, 1)
        #     else:
        #         dfs(l.left, r.right, 0)
        #         dfs(l.right, r.left, 0)
        #
        # dfs(root.left, root.right, 0)
        # return root
