import datetime
from log_entry import LogEntry

class TamperEvidentLog:
    def __init__(self):
        self.chain = [self.create_genesis_log()]

    def create_genesis_log(self):
        return LogEntry(0, str(datetime.datetime.now()), "GENESIS", "First Log", "0")

    def add_log(self, event_type, description):
        prev_log = self.chain[-1]

        new_log = LogEntry(
            len(self.chain),
            str(datetime.datetime.now()),
            event_type,
            description,
            prev_log.hash
        )

        self.chain.append(new_log)

    def verify_logs(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return f"Tampering detected at log {i}"

            if current.prev_hash != previous.hash:
                return f"Chain broken at log {i}"

        return "Logs are secure"