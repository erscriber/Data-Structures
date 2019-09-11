class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements? linked list
    self.storage = []

  def enqueue(self, item):
    # add element to end of queue
    self.storage.insert(0, item)

  def dequeue(self):
    # delete item from start of queue
    if len(self.storage) < 1:
      return None
    return self.storage.pop()

  def len(self):
    return len(self.storage)
