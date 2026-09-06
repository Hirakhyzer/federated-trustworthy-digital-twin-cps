from dataclasses import replace

def apply(update, rounds_old: int = 4):
    return replace(update, round_created=max(0, update.round_created-rounds_old), condition="stale_update")
