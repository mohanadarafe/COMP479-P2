import nltk

def construct_postings(dic, key, val):
    if(key in dic):
        dic[key][0] += 1
        dic[key][1].append(val)
    else:
        dic[key] = [1, [val]]

def queryProcessor(word, dic):
    if word in dic:
        print(dic[word])
    else:
        print("negatif")

def get_tokens(document):
    tokensList = []
    for tokens in getDocumentTitle(document):
        tokensList.append(tokens)

    for tokens in getDocumentBody(document):
        tokensList.append(tokens)

    for tokens in getDocumentExtraTokens(document):
        tokensList.append(tokens)

    return tokensList

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
    return tokens

def getDocumentDate(document):
    start, end, tokenizer = sanitizer(document, "<DATELINE>", "</DATELINE>", 10)
    tokens = tokenizer.tokenize(document[start:end])
    return tokens

## This gets all tokens in <D> tags which includes people, categories & places.
def getDocumentExtraTokens(document):
    start, end, tokenizer = sanitizer(document, "<D>", "</D>", 3)
    tokens = tokenizer.tokenize(document[start:end])
    return tokens

def getDocumentId(document):
    start = document.find('NEWID="') + 7
    end = document.find(">", start) - 1
    return document[start:end]