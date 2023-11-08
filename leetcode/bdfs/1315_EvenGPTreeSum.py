from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # answer = 0
        # q = deque([])
        # if root.val % 2 == 0:
        #     if root.left:
        #         q.append((1,root.left))
        #     if root.right:
        #         q.append((1,root.right))
        # else:
        #     if root.left:
        #         q.append((-1,root.left))
        #     if root.right:
        #         q.append((-1,root.right))

        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         v, node = q.popleft()
        #         if node.val % 2 == 0:
        #             if node.left:
        #                 q.append((1,node.left))
        #             if node.right:
        #                 q.append((1, node.right))
        #         else:
        #             if node.left:
        #                 q.append((-1,node.left))
        #             if node.right:
        #                 q.append((-1, node.right))

        #         if v == 1:
        #             if node.left:
        #                 answer += node.left.val
        #             if node.right:
        #                 answer += node.right.val
        # return answer

        def dfs(curr, p, gp):
            if not curr:
                return 0
            if gp and gp.val % 2 == 0:
                return curr.val + dfs(curr.left, curr, p) + dfs(curr.right, curr, p)
            return dfs(curr.left, curr, p) + dfs(curr.right, curr, p)

        return dfs(root, None, None)









