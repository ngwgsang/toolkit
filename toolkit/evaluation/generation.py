from typing import List, Dict, Any

def compute_bleu(
    predictions: List[str],
    references: List[str]
) -> float:
    """
    Tính điểm BLEU cho tập hợp câu dự đoán và tham chiếu.

    Args:
        predictions (List[str]): Danh sách các câu dự đoán.
        references (List[str]): Danh sách các câu tham chiếu tương ứng.

    Returns:
        float: BLEU score (0 - 100).
    """
    from sacrebleu import corpus_bleu
    return corpus_bleu(predictions, [references]).score


def compute_rouge(
    predictions: List[str],
    references: List[str]
) -> List[Dict[str, Any]]:
    """
    Tính điểm ROUGE cho tập câu dự đoán và tham chiếu.

    Args:
        predictions (List[str]): Danh sách câu dự đoán.
        references (List[str]): Danh sách câu tham chiếu tương ứng.

    Returns:
        List[Dict[str, Any]]: Danh sách kết quả ROUGE cho từng cặp câu.
    """
    from rouge_score import rouge_scorer
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = [scorer.score(ref, pred) for ref, pred in zip(references, predictions)]
    return scores
