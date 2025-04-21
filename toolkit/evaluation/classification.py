from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def compute_confusion(y_true, y_pred, labels=None):
    return confusion_matrix(y_true, y_pred, labels=labels)

def classification_summary(y_true, y_pred, labels=None, output_dict=False):
    return classification_report(y_true, y_pred, labels=labels, output_dict=output_dict)

def accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)