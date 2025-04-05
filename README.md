## Project Structure

- `corpora/` — text corpora used for retrieval.
- `questions/` — input questions and relevant references.
- `result_tables/` — saved results in png format.

- `main.py` — entry point to run the full pipeline.
- `load_data.py` — load corpora and questions into the pipeline.
- `fixed_token_chunker.py` — chunker that splits text.
- `embedder.py` — module for converting text into embeddings.
- `retrieval.py` — retrieval logic using embeddings.
- `evaluation.py` — evaluation metrics computation.
- `final_evaluation.py` — summary of evaluation results.
- `export_table.py` — export results to table format (png).

- `REPORT.md` — explanation of the process, findings, and insights.
