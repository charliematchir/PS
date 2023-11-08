
################## rec naive #####################################
# class Node(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.total = 0
#         self.left = None
#         self.right = None
#
# class NumArray(object):
#     def __init__(self, nums):
#         def createTree(l, r):
#             if l > r:
#                 return None
#
#             n = Node(l, r)
#
#             if l == r:
#                 n.total = nums[l]
#                 return n
#
#             # mid = l + (r - l) // 2
#             mid = (r + l) // 2
#             n.left = createTree(l, mid)
#             n.right = createTree(mid + 1, r)
#             n.total = n.left.total + n.right.total
#             return n
#
#         self.root = createTree(0, len(nums) - 1)
#
#     def update(self, index, val):
#         def upd(node, value):
#             if node.start == node.end:
#                 node.total = value
#             else:
#                 # mid = node.start (node.end + node.start)/2
#                 mid = (node.end + node.start) / 2
#                 if index <= mid:
#                     upd(node.left, value)
#                 else:
#                     upd(node.right, value)
#                 node.total = node.left.total + node.right.total
#
#         upd(self.root, val)
#
#     def sumRange(self, left, right):
#
#         def sr(node, l, r):
#             if node.start == l and node.end == r:
#                 return node.total
#             else:
#                 mid = (node.end + node.start) / 2
#                 # mid = node.start + (node.end - node.start)/2
#                 if mid >= r:
#                     return sr(node.left, l, r)
#                 elif mid + 1 <= l:
#                     return sr(node.right, l, r)
#                 else:
#                     return sr(node.left, l, mid) + sr(node.right, mid + 1, r)
#
#         return sr(self.root, left, right)

######################## rec more space ####################################
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.tree = [0] * (len(nums) + 1)

        def createTree(pos, start, end):
            if start == end:
                self.tree[pos] = nums[start]
                return self.tree[pos]
            mid = (start + end) / 2
            self.tree[pos] = createTree(pos * 2, start, mid) + createTree(pos * 2 + 1, mid + 1, end)
            return self.tree[pos]
        createTree(1, 1, len(nums))

    def update(self, index, val):
        value = val - self.nums[index]
        self.nums[index] = val

        def upd(pos, start, end, diff):
            if start > index or index > end:
                return

            self.tree[pos] += diff
            if start != end:
                mid = (start + end) / 2
                upd(pos*2, start, mid, diff)
                upd(pos*2+1, mid+1, end, diff)

        upd(1, 1, self.length, value)

        def upd(node, value):
            if node.start == node.end:
                node.total = value
            else:
                mid = (node.end + node.start) / 2
                if index <= mid:
                    upd(node.left, value)
                else:
                    upd(node.right, value)
                node.total = node.left.total + node.right.total

        upd(self.root, val)

    def sumRange(self, left, right):

        def sr(pos, start, end):
            if end < left or start > right:
                return 0
            if left <= start and end <= right:
                return self.tree[pos]
            mid = (start + end)/ 2
            return sr(pos*2, start, mid) + sr(pos*2+1, mid+1, end)
        return sr(1, 1, self.length)


        def sr(node, l, r):
            if node.start == l and node.end == r:
                return node.total
            else:
                mid = (node.end + node.start) / 2
                # mid = node.start + (node.end - node.start)/2
                if mid >= r:
                    return sr(node.left, l, r)
                elif mid + 1 <= l:
                    return sr(node.right, l, r)
                else:
                    return sr(node.left, l, mid) + sr(node.right, mid + 1, r)

        return sr(self.root, left, right)


####################### FanWick Tree ##########################################
# https://www.crocus.co.kr/666
class BinaryTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] + nums

        # p는 LSB에 1 더한 것, 현재 노드를 포함하는 가장 가까운 범위
        for i in range(1, self.n+1):
            p = i + (i & -i)
            if p <= self.n:
                self.tree[p] += self.tree[i]

    def update(self, i, v):
        while i <= self.n:
            self.tree[i] += v
            i += (i & -i)

    # 0 ~ i 까지의 합을 나타냄
    # i의 bit에서 LSB의 1을 뺀 값의 노드에서 의미는, 자신이 포함하지 않는 연속적인 범위을 뜻함
    def summation(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.tree = BinaryTree(nums)

    def update(self, index, val):
        self.tree.update(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left, right):
        return self.tree.summation(right + 1) - self.tree.summation(left)
