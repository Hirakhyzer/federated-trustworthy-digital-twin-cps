def confusion(truth, pred, positive_label=True):
    tp=sum(1 for t,p in zip(truth,pred) if bool(t)==positive_label and bool(p)==positive_label)
    fp=sum(1 for t,p in zip(truth,pred) if bool(t)!=positive_label and bool(p)==positive_label)
    fn=sum(1 for t,p in zip(truth,pred) if bool(t)==positive_label and bool(p)!=positive_label)
    tn=len(truth)-tp-fp-fn
    precision=tp/(tp+fp) if tp+fp else 0.0
    recall=tp/(tp+fn) if tp+fn else 0.0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
    return {"tp":tp,"fp":fp,"fn":fn,"tn":tn,"precision":precision,"recall":recall,"f1":f1}
