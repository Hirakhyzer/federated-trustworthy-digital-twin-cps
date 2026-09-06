def estimated_bytes(n_updates: int, model_dim: int, bytes_per_float: int = 8) -> int:
    return int(n_updates*model_dim*bytes_per_float)
