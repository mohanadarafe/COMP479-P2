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
1. Implement the lossy dictionary compression techniques of Table 5.1 in the textbook and compile a similar table for Reuters-21578. Are the changes similar ? Discuss your findings. (Note that stemming is not required here, if you run out of time before you get the Porter stemmer to work, that is ok for this assignment, the remaining table is fine.)
2. Compare retrieval results for your three sample queries of Subproject II when you run them on your
compressed index. Discuss your findings in your report

## Running the project

### Setup
Make sure you have Conda installed on your machine
```
conda env create --name project2 --file=env.yml
conda activate project2
```

### Before starting
Make sure you run **all commmands** from the project directory.

### Sub-project 1
Sub-project 1 is divided in 2 modules: preprocessor & postings list builder

```
python subproject1/run.py
```

### Sub-project 2
Check the output folder to see the results in ```sampleQueries.json```

```
python subproject2/queryProcessor.py -q "<query>"
e.g. python subproject2/queryProcessor.py -q "apple"

<query>: token to query
```

### Sub-project 3

**Lossy Table Compressor**

The lossy table compressor is displayed in the console.

```
python subproject3/loosy_compressor_execute.py
```

**Lossy Table Compressor Query**

Check the output folder to see the results in ```compressedSampleQueries.json```
NOTE: It is normal that many query terms don't appear to have results, this is due to the Porter Stemmer.

```
python subproject3/lossy_compression_query.py -q <query>
e.g. python subproject3/lossy_compression_query.py -q "apple"

<query>: token to query
```
