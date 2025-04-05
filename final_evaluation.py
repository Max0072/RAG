import logging as log
import json
# from fixed_token_chunker import FixedTokenChunker
from load_data import load_corpus, load_questions
from fixed_token_chunker import FixedTokenChunker
from embedder import Embedder
from retrieval import retrieve_top_k
from evaluation import retrieval_evaluation


def finalEvaluation(chunk_size, chunk_overlap, top_k):
    # Upload info
    dec_pl = 3
    corpus_dir = "corpora"
    questions_path = "questions/questions_df.csv"
    corpus = load_corpus(corpus_dir)
    questions_df = load_questions(questions_path, allowed_doc_ids=corpus.keys())

    # Chunking
    chunker = FixedTokenChunker(encoding_name="cl100k_base",
                                model_name=None,
                                chunk_size=chunk_size,
                                chunk_overlap=chunk_overlap)
    texts = chunker.split_text(corpus["wikitexts"])

    # Embedding corpus
    embedder = Embedder(model_name="all-MiniLM-L6-v2")
    embeddings = embedder.encode(texts)

    # Embedding questions
    questions = questions_df['question'].tolist()
    question_embeddings = embedder.encode(questions)

    # extract gold excerpts
    golden_excerpts_json = questions_df['references'].tolist()
    golden_excerpts = []
    for golden_excerpt_json in golden_excerpts_json:
        golden_excerpt = [item["content"] for item in json.loads(golden_excerpt_json)]
        golden_excerpts.append(golden_excerpt)

    # retrieval and evaluation process
    all_relevant_found = 0
    all_total_relevant = 0
    all_retrieved_chunks = 0

    for i in range(len(question_embeddings)):
        question_embedding = question_embeddings[i]
        golden_excerpt = golden_excerpts[i]

        retrieved = retrieve_top_k(question_embedding, embeddings, texts, top_k=top_k)
        relevant_found, total_relevant, retrieved_chunks = retrieval_evaluation(retrieved, golden_excerpt)

        all_relevant_found += relevant_found
        all_total_relevant += total_relevant
        all_retrieved_chunks += retrieved_chunks
    info = [all_relevant_found, all_total_relevant, all_retrieved_chunks]
    # calculate recall and precision
    precision = round(all_relevant_found / all_retrieved_chunks, dec_pl)
    recall = round(all_relevant_found / all_total_relevant, dec_pl)
    iou = round(all_relevant_found / (all_retrieved_chunks + all_total_relevant - all_relevant_found), dec_pl)
    return iou, recall, precision, info
