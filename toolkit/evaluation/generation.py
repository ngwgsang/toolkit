def compute_bleu(predictions, references):
    from sacrebleu import corpus_bleu
    return corpus_bleu(predictions, [references]).score

def compute_rouge(predictions, references):
    from rouge_score import rouge_scorer
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = [scorer.score(ref, pred) for ref, pred in zip(references, predictions)]
    return scores  # hoặc tính trung bình
