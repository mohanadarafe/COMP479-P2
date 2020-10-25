import json, os

def queryProcessor(query):
    PATH = "output/sampleQueries.json"
    assert len(query) == 1, "Enter only one query term!"
    query_term = query[0].replace(" ", "")
    dictionary = dict()

    with open("output/postings_list.json", 'r') as json_file: 
        dictionary = json.load(json_file)

    assert type(dictionary) == dict, "The input maybe not the right one. Make sure you import the postings list!"
    
    with open(PATH, 'a', encoding="utf-8") as outputFile:
        if query_term not in dictionary:
            print("The query term you input is not in the corpus!")
            exit()

        output = {query_term: dictionary[query_term]}
        json.dump(output, outputFile, indent=3)
        