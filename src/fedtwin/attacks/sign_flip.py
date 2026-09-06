from dataclasses import replace

def apply(update, factor: float = 5.0):
    return replace(update, vector=-factor*update.vector, condition="sign_flip")
