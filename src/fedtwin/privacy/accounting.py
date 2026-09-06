def privacy_note(sigma: float, clipping_norm: float) -> dict:
    return {
        "sigma": float(sigma),
        "clipping_norm": float(clipping_norm),
        "formal_dp_guarantee": False,
        "note": "Research noise abstraction only; no epsilon/delta guarantee is claimed.",
    }
