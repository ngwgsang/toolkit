from typing import List, Optional, Union
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

def compute_confusion(
    y_true: List[Union[int, str]],
    y_pred: List[Union[int, str]],
    labels: Optional[List[Union[int, str]]] = None
) -> List[List[int]]:
    return confusion_matrix(y_true, y_pred, labels=labels)

def compute_wf1(
    y_true: List[Union[int, str]],
    y_pred: List[Union[int, str]],
    labels: Optional[List[Union[int, str]]] = None
) -> float:
    return f1_score(y_true, y_pred, average='weighted', labels=labels)

def compute_mf1(
    y_true: List[Union[int, str]],
    y_pred: List[Union[int, str]],
    labels: Optional[List[Union[int, str]]] = None
) -> float:
    return f1_score(y_true, y_pred, average='macro', labels=labels)

def compute_recall(
    y_true: List[Union[int, str]],
    y_pred: List[Union[int, str]],
    labels: Optional[List[Union[int, str]]] = None
) -> float:
    return recall_score(y_true, y_pred, average='macro', labels=labels)

def compute_pre(
    y_true: List[Union[int, str]],
    y_pred: List[Union[int, str]],
    labels: Optional[List[Union[int, str]]] = None
) -> float:
    return precision_score(y_true, y_pred, average='macro', labels=labels)
