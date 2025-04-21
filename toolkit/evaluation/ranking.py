def mean_reciprocal_rank(rs):
    """rs: list of list of bools, ví dụ: [[False, True, False], [True, False]]"""
    return sum(1. / (r.index(True) + 1) for r in rs if True in r) / len(rs)

def ndcg_at_k(r, k):
    """r: relevance list (list[int]), k: cutoff"""
    from math import log2
    dcg = sum((2**rel - 1) / log2(i + 2) for i, rel in enumerate(r[:k]))
    ideal = sorted(r, reverse=True)
    idcg = sum((2**rel - 1) / log2(i + 2) for i, rel in enumerate(ideal[:k]))
    return dcg / idcg if idcg else 0.0
