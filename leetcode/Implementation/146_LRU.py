class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.hd = self.tl = None
        self.cap = capacity

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_end(node)
        else:
            node = Node(key, value)
            if self.cap == 0:
                self.pophead()
            else:
                self.cap -= 1
            self.cache[key] = node
            self.insert_end(node)

    def insert_end(self, node):
        if self.hd is None:
            self.hd = node
            self.tl = node
        else:
            node.prev = self.tl
            self.tl.next = node
            self.tl = node

    def move_to_end(self, node):
        if node == self.tl:
            return
        if node == self.hd:
            self.hd = node.next
        else:
            node.prev.next = node.next
        node.next.prev = node.prev
        self.insert_end(node)

    def pophead(self):
        key = self.hd.key
        if self.hd == self.tl:
            self.hd = self.tl = None
        else:
            self.hd = self.hd.next
            self.tl.next = self.hd
        del self.cache[key]