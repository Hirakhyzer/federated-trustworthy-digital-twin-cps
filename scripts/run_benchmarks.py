from fedtwin.experiments.benchmarks import poisoning_sweep, attack_suite, fault_ambiguity
from fedtwin.experiments.reporting import write_json, write_csv

if __name__ == "__main__":
    p=poisoning_sweep(); a=attack_suite(); f=fault_ambiguity()
    write_json({"poisoning":p,"attacks":a,"fault_ambiguity":f},"results/baseline_benchmarks.json")
    write_csv(p,"results/poisoning_sweep.csv")
    print(f"wrote {len(p)+len(a)+len(f)} experiment rows")
