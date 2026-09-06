from dataclasses import replace

def apply(update, factor: float = 6.0):
    return replace(update, vector=update.vector*factor, condition="scaling_attack")
