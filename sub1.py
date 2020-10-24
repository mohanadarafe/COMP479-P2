import glob, os, sys, utils, nltk, json
from tqdm import tqdm

def preprocess_reuters(path):
    print("\nGeting raw files...")
    raw_files = utils.block_reader(path)
    print("\nParsing documents...")
    documents = utils.block_document_segmenter(raw_files)
    print("\nBuilding id-raw document pairs...")
    doc_pairs = utils.block_extractor(documents)
    print("\nTokenizing id-document pairs...")
    F = utils.block_tokenizer(doc_pairs)
    print("\nCreating output file...")
    return F

def build_postings_list(INPUT):
    dictionary = dict()
    print("Removing duplicates...")
    for pairs in tqdm(INPUT, total=3498975):
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

    print("\nBuilding sorted data list...")
    list_dict = list(dictionary.items())
    sorted_list = sorted(list_dict, key=lambda x: x[0])
    tupleList = []
    for sorted_pairs in tqdm(sorted_list):
        for docIDs in sorted_pairs[1][1]:
            tupleList.append((docIDs, sorted_pairs[0]))

    print("\nLoading results...")
    with open("output/sorted_data.json", "w") as sorted_document:
        for tuples in tupleList:
            sorted_document.write(json.dumps(tuples))
            sorted_document.write("\n")

    raw = json.dumps(dictionary)
    with open('output/postings_list.json', 'w') as fp:
        fp.write(str(raw))
