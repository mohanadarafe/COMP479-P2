# COMP 479 - Project 2

## Objective
Implement the naive indexer. Implement single term query processing. Implement and compare lossy dictionary compression.

## Data
Use Reuters21578. For docID, use the NEWID values from the Reuters corpus to make your retrieval comparable

### Sub-project 1: Naive Indexer
1. Develop a module that while there are still more documents to be processed, accepts a document as a list of tokens and outputs term-documentID pairs to a list F.
2. When there is no more input, sort F and remove duplicates
3. Turn the sorted file F into an index by turning the docIDs paired with the same term into a postings list

### Sub-project 2: Single term query processing
1. Implement a query processor for single term queries
2. Validate query returns for three sample queries (you have to decide on your sample queries)

### Sub-project 3: Implement lossy dictionary compression
1. Implement the lossy dictionary compression techniques of Table 5.1 in the textbook and compile a similar table for Reuters-21578. Are the changes similar? Discuss your findings. (Note that stemming is not required here, if you run out of time before you get the Porter stemmer to work, that is ok for this assignment, the remaining table is fine.)
2. Compare retrieval results for your three sample queries of Subproject II when you run them on your
compressed index. Discuss your findings in your report