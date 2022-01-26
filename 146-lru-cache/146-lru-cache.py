class LRUCache: 
    # Douby Linked List with least recently used node at the start & most recently used node is at the end along with dictionary

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0) # dummy head
        self.tail = Node(0, 0) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node) # remove from start
            self._add(node) # add to end
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic: # if already existing remove it and then add a new one
            self._remove(self.dic[key])
            
        newNode = Node(key, value)
        self._add(newNode)
        self.dic[key] = newNode
        
        if len(self.dic) > self.capacity: # if more than capacity remove the least recently used node
            leastUsedNode = self.head.next # start of doubly linked list has least recently used node
            self._remove(leastUsedNode)
            del self.dic[leastUsedNode.key]

    def _remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def _add(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        self.tail.prev = node
        node.prev = lastNode
        node.next = self.tail

        
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)