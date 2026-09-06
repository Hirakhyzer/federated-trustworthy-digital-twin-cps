from fedtwin.attacks import scaling, sign_flip, outlier, stale, replacement, coordinated

def apply_condition(update, condition: str):
    if condition == "scaling_attack": return scaling.apply(update)
    if condition == "sign_flip": return sign_flip.apply(update)
    if condition == "outlier_attack": return outlier.apply(update)
    if condition == "stale_update": return stale.apply(update)
    if condition == "model_replacement": return replacement.apply(update)
    if condition == "coordinated_attack": return coordinated.apply(update)
    return update
