from fedtwin.network.model import staleness_weight

def test_staleness_weight_decreases():
    assert staleness_weight(5,5) > staleness_weight(5,2)
