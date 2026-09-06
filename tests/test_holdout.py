from fedtwin.experiments.domain_holdout import leave_one_domain_out

def test_holdout_has_seven_rows():
    rows=leave_one_domain_out()
    assert len(rows)==7 and all(r["representation_gap"]>0 for r in rows)
