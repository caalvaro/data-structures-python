from DoublyLinkedList import DoublyLinkedList

class Queue(DoublyLinkedList):
    def enqueue(self, item):
        self.append(item)
        
    def dequeue(self):
        first_item = self[0]
        
        self.remove(index=0)
        
        return first_item