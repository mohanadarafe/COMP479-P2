'''
The following file contains business logic for the execution of the subproject1
'''
import glob, os, sys, nltk, json
from tqdm import tqdm
sys.path.append('utilities')
import utils

'''
The following function preprocesses data in 4 steps.
Step 1- Read corpus
Step 2- Extract documents
Step 3- Build docID-term pairs (unsorted)
Step 4- Tokenize terms

@input path to reuters corpus files
@output docID-term pairs
'''
def preprocess_reuters(path):
    print("\nGeting raw files...")
    raw_files = utils.block_reader(path)
    print("\nParsing documents...")
    documents = utils.block_document_segmenter(raw_files)
    print("\nBuilding id-raw document pairs...")
    doc_pairs = utils.block_extractor(documents)
    print("\nTokenizing id-document pairs...")
    F = utils.block_tokenizer(doc_pairs)
    print("\nCreating unsorted data file...")
    return F

'''
The following function builds the postings list from the unsorted data file
produced in the previous block

@input unsorted docID-term file
@output postings list file 
'''
def build_postings_list(UNSORTED_FILE):
    dictionary = dict()
    print("Removing duplicates...")
    for pairs in tqdm(UNSORTED_FILE, total=3498975):
        docID = int(pairs[0])
        term = pairs[1]

        if term not in dictionary:
            dictionary[term] = [1, set([docID])]
        elif term in dictionary:
            dictionary[term][1].add(docID)
            dictionary[term][0] = len(dictionary[term][1])

    print("\nSorting doc ID's list...")
    for term in tqdm(dictionary):
        dictionary[term][1] = sorted(list(dictionary[term][1]))

    print("\nCreating postings list file...")
    raw = json.dumps(dictionary)
    with open('output/postings_list.json', 'w') as fp:
        fp.write(str(raw))
