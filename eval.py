import pandas as pd
import json

def get_label(w):
    w = w[1:len(w)-1]
    if w[0] == '/':
        w = w[1:]
    return w

def render_dsl(dsl):
    labels = {}
    for i in range(len(dsl)):
        d = dsl[i]
        if len(d) > 1 and '<' in d and '/' not in d:
            labels[get_label(d)] = dsl[i+1]
    return labels

def legal_dsl(dsl):
    l = []
    for d in dsl:
        if '/' in d and len(d)>1:
            if len(l) == 0 or get_label(d)!= get_label(l[-1]):
                return False
            l.pop()
        elif len(d)>1 and '<'in d:
            l.append(d)
    return True

def find_plot_type(dsl):
    for i in range(len(dsl)):
        if get_label(dsl[i]) == 'type': return dsl[i+1]
    return None


def compute_cls_acc(gt, pred):
    acc = []
    for p in pred:
        gt_sent = gt[p]
        pred_sent = pred[p]
        a = gt_sent.split()
        b = pred_sent.split()
        error = 0
        for j in range(len(a)):
            if j>=len(b) or b[j] != a[j]:
                error += 1
        acc.append(1 - float(error)/len(a))
    print('Average Classification Accuracy is %f'%(sum(acc)/len(acc)))

def compute_str_acc(gt, pred):
    acc = []
    for p in pred:
        gt_sen = gt[p].split()
        pred_sen = pred[p].split()
        if legal_dsl(pred_sen):
            pred_type = find_plot_type(pred_sen)
            if pred_type is not None and find_plot_type(gt_sen) == pred_type:
                # Check if all str token belows to type
                acc.append(1)
            else:
                acc.append(0)
        else:
            acc.append(0)
    print('Average Structure Accuracy is %f' % (sum(acc) / len(acc)))

def compute_dec_acc(gt, preds):
    acc = []
    for p in preds:
        score = 0
        src = gt[p].split()
        pred = preds[p].split()
        if legal_dsl(pred):
            pred_type = find_plot_type(pred)
            if pred_type is None or find_plot_type(src) != pred_type or len(pred)>=199:
                acc.append(0)
            else:
                labels_pred = render_dsl(pred)
                labels_src = render_dsl(src)
                for k in labels_src:
                    if k not in ['structure','plot','type']:
                        if k in labels_pred and labels_pred[k] == labels_src[k]:
                            score += 1
                acc.append(float(score)/(len(labels_src)-3))
    print('Average Decoration Accuracy is %f' % (sum(acc) / len(acc)))

if __name__ == "__main__":
    with open('data/tgt_test.txt', 'r') as f:
        dsl = f.readlines()
        dsl = [d.replace('\n', '') for d in dsl]

    with open('data/src_test.txt', 'r') as f:
        imgs = f.readlines()
        imgs = [i.replace('\n', '') for i in imgs]

    gt = {}
    for img, d in zip(imgs, dsl):
        gt[img] = d

    with open('output/predictions.json', 'r') as f:
        pred = json.load(f)
    compute_cls_acc(gt, pred)
    compute_str_acc(gt, pred)
    compute_dec_acc(gt, pred)
