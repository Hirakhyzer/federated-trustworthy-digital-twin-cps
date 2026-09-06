from fedtwin.trust.history import TrustHistory

def test_history_updates_smoothly():
    h=TrustHistory(momentum=.5)
    first=h.update("c",0.1)
    second=h.update("c",0.9)
    assert 0.1 < second < 0.9
