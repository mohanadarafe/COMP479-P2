# COMP 479 - Project 2

## Objective
Implement the naive indexer. Implement single term query processing. Implement and compare lossy dictionary compression.

## Data
Use Reuters21578. For docID, use the NEWID values from the Reuters corpus to make your retrieval comparable

### Sub-project 1: Naive Indexer
1. develop a module that while there are still more documents to be processed, accepts a document as a list
of tokens and outputs term-documentID pairs to a list F. Punctuation is not considered to be a token by
itself, but your tokenizer might recognize tokens that include punctuation signs
2. when there is no more input, sort F and remove duplicates
3. turn the sorted file F into an index by turning the docIDs paired with the same term into a postings list
4. find a way to determine, how much time your index takes to compile (not graded in this assignment)

### Sub-project 2: Single term query processing
1. Input: one term
2. Output: append term to postings list. Make sure that the postings list is ordered
3. Turn your output into json format

### Sub-project 3: Implement lossy dictionary compression
1. Implement the lossy dictionary compression techniques of Table 5.1 in the textbook and compile a similar table for Reuters-21578. Are the changes similar? Discuss your findings. (Note that stemming is not required here, if you run out of time before you get the Porter stemmer to work, that is ok for this assignment, the remaining table is fine.)
2. Compare retrieval results for your three sample queries of Subproject II when you run them on your
compressed index. Discuss your findings in your report