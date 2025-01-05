# Class Queue

class Queue:
    def __init__(self):
        self.queue = []

    # Insert a new value at the rear of the queue
    def insert(self, value):
        self.queue.append(value)
        print(f"Inserted: {value} in Queue!")

    # Remove and return the value from the front of the queue
    def pop(self):
        if self.is_empty():
            print("Empty Queue!")
            return None
        return self.queue.pop(0)

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # For debugging: Print the current queue
    def display(self):
        print("Current Queue:", self.queue)
