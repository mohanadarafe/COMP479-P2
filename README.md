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

## Running the project

### Setup
Make sure you have Conda installed on your machine
```
conda env create --name project2 --file=env.yml
conda activate project2
```

### Sub-project 1
In order to execute sub-project 1, it is divided in 2 modules: data preprocessor & data sorting.

**Module 1 execution | Data Preprocessing**
The following module reads the corpus & produces a list of unsorted docID-term pairs
```
python indexer_processor.py --path "<path to data>" -o "output/<output_file_name>.json"

<path_to_data>: path to reuters data files
<output_file_name>: name your file to see output

ex: python indexer_processor.py --path "./data" -o "output/unsorted_data.json"
```

**Module 2 execution**
The following module reads the unsorted data from the previous module, sorts & removes duplicates to produce both a sorted docID-term pairs list & the postings list.

Check the output folder to see both ```sorted_data.json``` & ```postings_list.json```
```
python indexer_builder.py -i "<output_module_1_file>.json"

<input_file_name>: name of the output file from module 1
ex: python indexer_builder.py -i "output/unsorted_data.json"
```

### Sub-project 2
The following module is a query processor for single-term queries.

Check the output folder to see the results in ```sampleQueries.json```
```
python queryProcessor.py --path "output/postings_list.json" -q "<query>"

<path_to_postings_list>: path to postings list produces in module 1
<query>: token to query

python queryProcessor.py --path "output/postings_list.json" -q "apple"

```
