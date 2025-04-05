from typing import List, Tuple


def retrieval_evaluation(retrieved_chunks: List[str], gold_excerpts: List[str]) -> Tuple[int, int, int]:
    relevant_found = 0
    total_relevant = len(gold_excerpts)
    total_retrieved_chunks = len(retrieved_chunks)
    for gold_excerpt in gold_excerpts:
        for chunk in retrieved_chunks:
            if gold_excerpt.strip() in chunk or chunk in gold_excerpt.strip():
                relevant_found += 1
    if total_relevant < relevant_found:
        relevant_found = total_relevant
    return relevant_found, total_relevant, total_retrieved_chunks
