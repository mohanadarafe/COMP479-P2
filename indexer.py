import glob, os, sys, utils, nltk, json
from tqdm import tqdm

def module1(path):
    print("\nGeting raw files...")
    raw_files = block_reader(path)
    print("\nParsing documents...")
    documents = block_document_segmenter(raw_files)
    print("\nBuilding id-raw document pairs...")
    doc_pairs = block_extractor(documents)
    print("\nTokenizing id-document pairs...")
    F = block_tokenizer(doc_pairs)
    print("\nCreating output file...")
    return F

def module2(INPUT):
    dictionary = dict()

    for pairs in INPUT:
        docID = int(pairs[0])
        term = pairs[1]

        if term not in dictionary:
            dictionary[term] = [1, set([docID])]
        elif term in dictionary:
            dictionary[term][1].add(docID)
            dictionary[term][0] = len(dictionary[term][1])

    for term in dictionary:
        dictionary[term][1] = sorted(list(dictionary[term][1]))

    list_dict = list(dictionary.items())
    sorted_list = sorted(list_dict, key=lambda x: x[0])
    tupleList = []
    for sorted_pairs in sorted_list:
        for docIDs in sorted_pairs[1][1]:
            tupleList.append((docIDs, sorted_pairs[0]))

    with open("output/sorted_list.json", "w") as f:
        for tuples in tupleList:
            f.write(json.dumps(tuples))
            f.write("\n")
        
    return dictionary

'''
    dictionary.items() -> (term, [freq, [postings list]]).sort(key=lambda x, x[0])
'''
def module3(INPUT):
    dictionary = dict()
    for pairs in INPUT:
        utils.construct_postings(dictionary, pairs[1], int(pairs[0]))

    print(dictionary)
    return dictionary

def block_tokenizer(document_dict):
    tupleList = []
    wordTuple = ()

    for dictionary in tqdm(document_dict):
        id = dictionary["ID"]
        text = dictionary["TEXT"]
        for words in utils.get_tokens(text):
            wordTuple = (id, words)
            tupleList.append(wordTuple)
            
    return tupleList

def block_extractor(documents):
    newsList = []
    newsDictionary = {}

    for document in tqdm(documents):
        newsDictionary = {'ID': utils.getDocumentId(document), 'TEXT': document}
        newsList.append(newsDictionary)
        
    return newsList

def block_document_segmenter(raw_files):
    document_list = []
    document = ""
    keepCopying = False
    START_DELIMITER = '<REUTERS '
    END_DELIMITER = '</REUTERS>'
    
    for files in raw_files:
        for lines in tqdm(files.splitlines()):
            if END_DELIMITER in lines: 
                document += lines
                document_list.append(document)
                document = ""
                keepCopying = False
            if START_DELIMITER in lines: 
                keepCopying = True
            if keepCopying:
                document += " " + lines

    return document_list

def block_reader(path):
    fileContent = []
    try:
        files = []
        for file in glob.glob(path+"/*.sgm"):
            files.append(file)
        
        files.sort()

        for fileName in tqdm(files):
            raw = open(fileName, 'r', errors='ignore').read()
            fileContent.append(raw)

        assert len(fileContent) == 22, "There may be a missing file!"
        
    except FileNotFoundError:
        print("File not found!")
    
    return fileContent
