import nltk

def sanitizer(document, starterDelimiter, endDelimiter, index):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    start = document.find(starterDelimiter) + index
    end = document.find(endDelimiter)
    return start, end, tokenizer

def getDocumentBody(document):
    start, end, tokenizer = sanitizer(document, "<BODY>", " Reuter&#3;</BODY>", 6)
    tokens = tokenizer.tokenize(document[start:end])
    return tokens

def getDocumentTitle(document):
    start, end, tokenizer = sanitizer(document, "<TITLE>", "</TITLE>", 7)
    tokens = tokenizer.tokenize(document[start:end])
    return document[start:end]

## This gets all tokens in <D> tags which includes people, categories & places.
def getDocumentExtraTokens(document):
    start, end, tokenizer = sanitizer(document, "<D>", "</D>", 3)
    tokens = tokenizer.tokenize(document[start:end])
    return document[start:end]

def getDocumentId(document):
    start = document.find('NEWID="') + 7
    end = document.find(">", start) - 1
    return document[start:end]