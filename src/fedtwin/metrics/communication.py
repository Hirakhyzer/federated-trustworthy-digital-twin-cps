def communication_mb(n_updates: int, model_dim: int, rounds: int, bytes_per_float: int = 8):
    return n_updates*model_dim*rounds*bytes_per_float/(1024**2)
