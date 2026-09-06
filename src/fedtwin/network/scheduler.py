def select_available(clients):
    return [c for c in clients if c.available and c.condition != "offline_client"]
