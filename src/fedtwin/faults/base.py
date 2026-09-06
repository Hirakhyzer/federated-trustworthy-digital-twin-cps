FAULT_CONDITIONS={"sensor_fault","physical_fault","model_mismatch","domain_shift","slow_client","offline_client"}

def is_fault(condition: str) -> bool:
    return condition in FAULT_CONDITIONS
