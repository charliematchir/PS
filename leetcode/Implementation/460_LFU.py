from collections import defaultdict


class Node:
    def __init__(self, key=None, value=None, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head.prev = self.head
        self.size = 0
    def __len__(self):
        return self.size
    ## head가 있고 append 는 맨 처음에 들어감
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size += 1

    ## pop은 지정하지 않은 경우 맨 뒤에 녀석 out
    def pop(self, node=None):
        if self.size == 0:
            return None

        if not node:
            node = self.head.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

class LFUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.freq = defaultdict(DoublyLinkedList)
        self.minFreq = 1

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            node.value = value
        else:
            if self.cap == 0:
                node = self.freq[self.minFreq].pop()
                del self.cache[node.key]
                self.cap += 1
            node = Node(key, value)
            self.cache[key] = node
            self.freq[1].append(node)
            self.cap -= 1
            self.minFreq = 1

    def update(self, node):
        f = node.freq
        self.freq[f].pop(node)
        if self.minFreq == f and not self.freq[f]:
            self.minFreq += 1
        node.freq += 1
        self.freq[node.freq].append(node)

#
# from collections import defaultdict
#
#
# class ListNode:
#     def __init__(self, key=None, val=None):
#         self.key = key
#         self.val = val
#         self.freq = 1
#
#         self.prev = None
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = ListNode()
#         self.tail = ListNode()
#
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#         self.size = 0
#
#     def addNode(self, node):
#         old_end = self.tail.prev
#         old_end.next = node
#
#         node.prev = old_end
#         node.next = self.tail
#
#         self.tail.prev = node
#         self.size += 1
#
#     def removeNode(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#         self.size -= 1
#
#     def removeHead(self):
#         head = self.head.next
#         self.removeNode(head)
#
#         return head
#
#
# class LFUCache:
#     def __init__(self, capacity):
#         self.cache = {}
#         self.freqTable = defaultdict(LinkedList)
#         self.capacity = capacity
#         self.minFreq = 0
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#
#         return self.updateCache(self.cache[key], key, self.cache[key].val)
#
#     def put(self, key, value):
#         if key in self.cache:
#             self.updateCache(self.cache[key], key, value)
#         else:
#             if len(self.cache) == self.capacity:
#                 prevHead = self.freqTable[self.minFreq].removeHead()
#                 del self.cache[prevHead.key]
#
#             node = ListNode(key, value)
#             self.freqTable[1].addNode(node)
#             self.cache[key] = node
#             self.minFreq = 1
#
#     def updateCache(self, node, key, value):
#         node = self.cache[key]
#         node.val = value
#         prevFreq = node.freq
#         node.freq += 1
#
#         self.freqTable[prevFreq].removeNode(node)
#         self.freqTable[node.freq].addNode(node)
#
#         if prevFreq == self.minFreq and self.freqTable[prevFreq].size == 0:
#             self.minFreq += 1
#
#         return node.val
#
# class Node:
#     def __init__(self, key, value, freq=1):
#         self.key = key
#         self.value = value
#         self.freq = freq
#         self.prev = self.next = None
#
# class DoublyLinkedList:
#     def __init__(self, hd=None, tl=None):
#         self.hd = hd
#         self.tl = tl
#
#     def append(self, node):
#         if self.hd == None:
#             self.hd = self.tl = node
#         else:
#             node.next = self.tl.next
#             node.prev = self.tl
#             self.tl.next = self.hd.prev = node
#             self.tl = node
#
#     def pop(self, node=None):
#         if self.tl == None:
#             return None
#
#         if not node:
#             node = self.tl
#             self.tl.prev.next = self.tl.next
#             self.tl = self.tl.prev
#             self.hd.prev = self.tl
#             return node
#         else:
#             node.prev.next = node.next
#             node.next.prev = node.prev
#             return node
#
#
# class LFUCache(object):
#     def __init__(self, capacity):
#         self.cap = capacity
#         self.cache = {}
#         self.freq = defaultdict(DoublyLinkedList)
#         self.minFreq = 10
#
#     def get(self, key):
#         if key in self.cache:
#             node = self.cache[key]
#
#             return node.value
#         return -1
#
#     def put(self, key, value):
#         if key in self.cache:
#             node = self.cache[key]
            # node.value = value
#             self.removeCon(node)

#             self.cap -= 1
#         else:
#             node = Node(key, value)
#             self.cache[key] = node
#             if self.cap == 0:
#                 dl = self.freq[self.minFreq]
#                 k = dl.hd.key
#                 if dl.hd == dl.tl:
#                     self.freq.discard(self.minFreq)
#                 else:
#                     dl.hd.prev.next = dl.hd.next
#                     dl.hd.next.prev = dl.hd.prev
#                     dl.hd = dl.hd.next
#                 del self.cache[k]
#                 self.createCon(node)
#             else:
#                 self.createCon(node)
#             self.minFreq = 1
#
#     def removeCon(self, node):
#         print(self.freq)
#         if node.next == node.prev:
#             del self.freq[node.freq]
#             if node.freq == self.minFreq:
#                 self.minFreq += 1
#         else:
#             node.prev.next = node.next
#             node.next.prev = node.prev
#         node.freq += 1
#         self.createCon(node)
#
#     def createCon(self, node):
#         if node.freq in self.freq:
#             dl = self.freq[node.freq]
#             node.next = dl.tl.next
#             dl.tl.next = node
#             node.prev = dl.tl
#             dl.tl = node.prev
#             print(dl.tl.value)
#         else:
#             self.freq[node.freq] = DoublyLinkedList(node, node)
#             node.next = node.prev = node
#
#         if node.freq < self.minFreq:
#             self.minFreq = node.freq