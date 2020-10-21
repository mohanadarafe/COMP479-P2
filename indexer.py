import glob, os, sys, utils, nltk

def get_documents(path):
    raw_files = block_reader(path)
    documents = block_document_segmenter(raw_files)
    doc_pairs = block_extractor(documents)
    tokenize_doc = block_tokenizer(doc_pairs)
    return tokenize_doc

def block_tokenizer(INPUT_STRUCTURE):
    tupleList = []
    wordTuple = ()

    for dictionary in INPUT_STRUCTURE:
        id = dictionary["ID"]
        text = dictionary["TEXT"]
        for words in utils.get_tokens(text):
            wordTuple = (id, words)
            tupleList.append(wordTuple)
            
    return tupleList

def block_extractor(INPUT_STRUCTURE):
    newsList = []
    newsDictionary = {}

    for document in INPUT_STRUCTURE:
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
        for lines in files.splitlines():
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

        for fileName in files:
            raw = open(fileName, 'r', errors='ignore').read()
            fileContent.append(raw)

        assert len(fileContent) == 22, "There may be a missing file!"
        
    except FileNotFoundError:
        print("File not found!")
    
    return fileContent
