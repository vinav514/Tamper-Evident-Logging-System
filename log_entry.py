import hashlib

class LogEntry:
    def __init__(self, index, timestamp, event_type, description, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.event_type = event_type
        self.description = description
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.timestamp}{self.event_type}{self.description}{self.prev_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self):
        return self.__dict__