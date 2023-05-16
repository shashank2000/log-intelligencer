# Data structures for storing log data in a vectorized format
class Data:
    def __init__(self, timestamp, node, text, embedding):
        self.timestamp = timestamp
        self.node = node
        self.text = text
        self.embedding = embedding