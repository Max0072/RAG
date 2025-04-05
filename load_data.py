import os
import pandas
import logging as log

def load_corpus(corpus_dir: str) -> dict:
    log.info("Loading corpus from %s", corpus_dir)
    corpus = {}
    for filename in os.listdir(corpus_dir):
        if filename.endswith(".txt"):
            doc_id = os.path.splitext(filename)[0]
            with open(os.path.join(corpus_dir, filename), 'r', encoding='utf-8') as f:
                corpus[doc_id] = f.read()
    return corpus


def load_questions(filepath: str, allowed_doc_ids=None) -> pandas.DataFrame:
    log.info("Loading questions from %s", filepath)
    df = pandas.read_csv(filepath)

    required_cols = {"question", "references", "corpus_id"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV has to contain the following columns: {required_cols}")

    if allowed_doc_ids is not None:
        df = df[df["corpus_id"].isin(allowed_doc_ids)]

    df = df.dropna(subset=["question", "references", "corpus_id"]).reset_index(drop=True)
    return df

