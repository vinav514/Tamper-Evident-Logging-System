import json

def save_logs(chain, filename="logs/logs.json"):
    data = [log.to_dict() for log in chain]

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_logs(filename="logs/logs.json"):
    with open(filename, "r") as f:
        return json.load(f)