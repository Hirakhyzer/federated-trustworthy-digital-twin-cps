def explanation(label: str, reasons: dict) -> str:
    strongest=sorted(reasons.items(), key=lambda kv: abs(kv[1]-0.5), reverse=True)[:3]
    evidence=", ".join(f"{k}={v:.2f}" for k,v in strongest)
    return f"{label}: strongest evidence -> {evidence}"
