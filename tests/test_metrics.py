from fedtwin.metrics.classification import confusion

def test_confusion_metrics():
    m=confusion([1,1,0,0],[1,0,1,0])
    assert m["tp"]==1 and m["fp"]==1 and m["fn"]==1 and m["tn"]==1
