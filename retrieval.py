import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple

def retrieve_top_k(
    query_embedding: np.ndarray,
    doc_embeddings: np.ndarray,
    doc_chunks: List[str],
    top_k: int = 5
) -> List[str]:

    sims = cosine_similarity([query_embedding], doc_embeddings)[0]
    top_indices = sims.argsort()[::-1][:top_k]
    return [doc_chunks[i] for i in top_indices]
