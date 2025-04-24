from sklearn.metrics.pairwise import cosine_similarity, manhattan_distances
from scipy.stats import spearmanr
from typing import List, Union
import numpy as np

# Alias
Vector = List[float]

def compute_cosine_similarity(vec1: Vector, vec2: Vector) -> float:
    return cosine_similarity([vec1], [vec2])[0][0]

def compute_manhattan_distance(vec1: Vector, vec2: Vector) -> float:
    return manhattan_distances([vec1], [vec2])[0][0]

def compute_spearman_correlation(vec1: Vector, vec2: Vector) -> float:
    corr, _ = spearmanr(vec1, vec2)
    return float(corr)  # có thể trả về nan nếu toàn bộ giá trị giống nhau

def compute_average(
    vectors1: List[Vector],
    vectors2: List[Vector],
    method: str = "cosine"
) -> float:
    """
    Tính trung bình độ tương đồng/khoảng cách giữa hai danh sách vector.

    Args:
        vectors1: Danh sách vector thứ nhất.
        vectors2: Danh sách vector thứ hai.
        method: 'cosine', 'manhattan', hoặc 'spearman'.

    Returns:
        float: Giá trị trung bình theo phương pháp đã chọn.
    """
    assert method in {"cosine", "manhattan", "spearman"}, "Method không hợp lệ"

    if method == "cosine":
        fn = compute_cosine_similarity
    elif method == "manhattan":
        fn = compute_manhattan_distance
    elif method == "spearman":
        fn = compute_spearman_correlation

    scores = [fn(v1, v2) for v1, v2 in zip(vectors1, vectors2)]
    return sum(scores) / len(scores) if scores else 0.0
