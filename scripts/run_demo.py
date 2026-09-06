from pprint import pprint
from fedtwin.experiments.simulator import run_experiment

if __name__ == "__main__":
    result=run_experiment(method="twintrust",malicious_fraction=0.2,attack_type="scaling_attack",seed=42)
    compact={k:v for k,v in result.items() if k not in {"final_model","final_assessments","accepted_final","final_conditions"}}
    pprint(compact)
