**Dataset Used:**
- Corpus: Wikitext
- Annotated queries and references were taken from `questions_df.csv`


**Pipeline Components:**
1. **Chunking Algorithm:** FixedTokenChunker
   - Chunk sizes tested: 100, 200, 300, 400, 800
   - Overlap settings: 0, 200, 400

2. **Embedding Model:**
   - Model used: all-MiniLM-L6-v2
   - Applied on both corpus chunks and query texts

3. **Retrieval Strategy:**
   - Semantic search using cosine similarity
   - Top-k retrieval (k = 2, 5, 10)

4. **Evaluation Metrics:**
   - **Recall**: Proportion of relevant chunks retrieved out of all relevant chunks
   - **Precision**: Proportion of retrieved chunks that were actually relevant
   - **IoU**: Intersection over union between retrieved and golden chunks


**Results Summary:**

| Chunk Size | Overlap | Top-k   | Recall | Precision | IoU   |
|------------|---------|---------|--------|-----------|-------|
| 800        | 400     | 10      | 0.984  | 0.170     | 0.170 |
| 400        | 200     | 10      | 0.956  | 0.165     | 0.164 |
| 400        | 0       | 10      | 0.896  | 0.155     | 0.152 |
| 300        | 0       | 10      | 0.867  | 0.150     | 0.147 |
| 200        | 0       | 10      | 0.787  | 0.136     | 0.131 |
| 100        | 0       | 10      | 0.550  | 0.095     | 0.088 |
| 800        | 400     | 5       | 0.900  | 0.311     | 0.301 |
| 400        | 200     | 5       | 0.884  | 0.306     | 0.294 |
| 400        | 0       | 5       | 0.759  | 0.263     | 0.242 |
| 300        | 0       | 5       | 0.739  | 0.256     | 0.234 |
| 200        | 0       | 5       | 0.679  | 0.235     | 0.211 |
| 100        | 0       | 5       | 0.466  | 0.161     | 0.136 |
| 800        | 400     | 2       | 0.727  | 0.628     | 0.508 |
| 400        | 200     | 2       | 0.699  | 0.604     | 0.479 |
| 400        | 0       | 2       | 0.570  | 0.493     | 0.359 |
| 300        | 0       | 2       | 0.526  | 0.455     | 0.323 |
| 200        | 0       | 2       | 0.518  | 0.448     | 0.316 |
| 100        | 0       | 2       | 0.349  | 0.302     | 0.193 |

---


**Key Findings:**
- Larger chunk sizes (400–800 tokens) consistently outperformed smaller ones across all metrics.
- Introducing chunk overlap (e.g., 50% overlap) significantly improved Recall and IoU, especially for larger chunk sizes.
- Reducing `top_k` improved Precision but led to a drop in Recall — a classic trade-off in retrieval systems.
- Best balance (high Recall, Precision and IoU):
  - Chunk size: 800
  - Overlap: 400
  - Top-k: 5
- Best high-precision configuration:
  - Chunk size: 800
  - Overlap: 400
  - Top-k: 2


**Conclusion:**
The retrieval pipeline can demonstrate good results when appropriately tuned. 
Chunk size and overlap are critical parameters. Depending on the application (high-recall vs high-precision), different configurations should be used. 
The use of semantic embeddings (MiniLM) proved effective in capturing relevance between queries and text chunks.


