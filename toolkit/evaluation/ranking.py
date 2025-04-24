from typing import List

def compute_precision_at_k(r: List[int], k: int) -> float:
    r_k = r[:k]
    return sum(r_k) / k

def compute_recall_at_k(r: List[int], k: int) -> float:
    r_k = r[:k]
    total_relevant = sum(r)
    return sum(r_k) / total_relevant if total_relevant else 0.0

def compute_average_precision(r: List[int]) -> float:
    hits = 0
    sum_precisions = 0.0
    for i, rel in enumerate(r):
        if rel:
            hits += 1
            sum_precisions += hits / (i + 1)
    return sum_precisions / hits if hits else 0.0

def compute_mean_average_precision(rs: List[List[int]]) -> float:
    return sum(compute_average_precision(r) for r in rs) / len(rs)

def compute_mean_reciprocal_rank(rs: List[List[bool]]) -> float:
    return sum(1. / (r.index(True) + 1) for r in rs if True in r) / len(rs)

def compute_ndcg_at_k(r: List[int], k: int) -> float:
    from math import log2
    dcg = sum((2**rel - 1) / log2(i + 2) for i, rel in enumerate(r[:k]))
    ideal = sorted(r, reverse=True)
    idcg = sum((2**rel - 1) / log2(i + 2) for i, rel in enumerate(ideal[:k]))
    return dcg / idcg if idcg else 0.0
