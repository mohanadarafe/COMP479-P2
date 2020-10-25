import math, json, lossy_compression_tools
from nltk.stem import PorterStemmer 

def computeTermLossy(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as json_file: 
        dictionary = json.load(json_file)

    stats["unfiltered"] = len(dictionary)

    dictionary = lossy_compression_tools.remove_numbers(dictionary)
    stats["no_number"] = len(dictionary)

    dictionary = lossy_compression_tools.case_folding(dictionary)
    stats["case_folding"] = len(dictionary)
    
    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 30)
    stats["30_stopwords"] = len(dictionary)

    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 150)
    stats["150_stopwords"] = len(dictionary)

    dictionary = lossy_compression_tools.stemming(dictionary)
    stats["stemming"] = len(dictionary)

    return stats

def computeNPLossy(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as json_file: 
        dictionary = json.load(json_file)

    stats["unfiltered"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.remove_numbers(dictionary)
    stats["no_number"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.case_folding(dictionary)
    stats["case_folding"] = lossy_compression_tools.frequency(dictionary)
    
    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 30)
    stats["30_stopwords"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 150)
    stats["150_stopwords"] = lossy_compression_tools.frequency(dictionary)

    dictionary = lossy_compression_tools.stemming(dictionary)
    stats["stemming"] = lossy_compression_tools.frequency(dictionary)

    return stats

def getCompressedDictionary(path):
    dictionary = dict()
    stats = dict()

    with open(path, 'r') as json_file: 
        dictionary = json.load(json_file)

    dictionary = lossy_compression_tools.remove_numbers(dictionary)
    dictionary = lossy_compression_tools.case_folding(dictionary)
    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 30)
    dictionary = lossy_compression_tools.remove_stopwords(dictionary, 150)
    dictionary = lossy_compression_tools.stemming(dictionary)

    return dictionary

def displayTable(path):
    term_data = computeTermLossy(path)
    np_data = computeNPLossy(path)

    print("\n\t\t\tTerms\t\tNP Postings")
    print("-" * 60)
    print("\t\tfreq\tΔ%\tT%\tfreq\tΔ%\tT%")
    print("-" * 60)

    print(f'unfiltered\t{term_data["unfiltered"]}\t\t\t{np_data["unfiltered"]}')

    deltaValueTerms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["no_number"])
    termValueTerms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["no_number"])
    deltaValueNP = lossy_compression_tools.delta(np_data["unfiltered"], np_data["no_number"])
    termValueNP = lossy_compression_tools.delta(np_data["unfiltered"], np_data["no_number"])
    print(f'no numbers\t{term_data["no_number"]}\t{deltaValueTerms*-1 if deltaValueTerms > 0 else deltaValueTerms}\t{termValueTerms*-1 if termValueTerms > 0 else termValueTerms}\t{np_data["no_number"]}\t{deltaValueNP*-1}\t{termValueNP*-1}')

    deltaValueTerms = lossy_compression_tools.delta(term_data["no_number"], term_data["case_folding"])
    termValueTerms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["case_folding"])
    deltaValueNP = lossy_compression_tools.delta(np_data["no_number"], np_data["case_folding"])
    termValueNP = lossy_compression_tools.delta(np_data["unfiltered"], np_data["case_folding"])
    print(f'case folding\t{term_data["case_folding"]}\t{deltaValueTerms*-1 if deltaValueTerms > 0 else deltaValueTerms}\t{termValueTerms*-1 if termValueTerms > 0 else termValueTerms}\t{np_data["case_folding"]}\t{deltaValueNP*-1}\t{termValueNP*-1}')

    deltaValueTerms = lossy_compression_tools.delta(term_data["case_folding"], term_data["30_stopwords"])
    termValueTerms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["30_stopwords"])
    deltaValueNP = lossy_compression_tools.delta(np_data["case_folding"], np_data["30_stopwords"])
    termValueNP = lossy_compression_tools.delta(np_data["unfiltered"], np_data["30_stopwords"])
    print(f'30 stopwords\t{term_data["30_stopwords"]}\t{deltaValueTerms*-1 if deltaValueTerms > 0 else deltaValueTerms}\t{termValueTerms*-1 if termValueTerms > 0 else termValueTerms}\t{np_data["30_stopwords"]}\t{deltaValueNP*-1}\t{termValueNP*-1}')

    deltaValueTerms = lossy_compression_tools.delta(term_data["30_stopwords"], term_data["150_stopwords"])
    termValueTerms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["150_stopwords"])
    deltaValueNP = lossy_compression_tools.delta(np_data["30_stopwords"], np_data["150_stopwords"])
    termValueNP = lossy_compression_tools.delta(np_data["unfiltered"], np_data["150_stopwords"])
    print(f'150 stopwords\t{term_data["150_stopwords"]}\t{deltaValueTerms*-1 if deltaValueTerms > 0 else deltaValueTerms}\t{termValueTerms*-1 if termValueTerms > 0 else termValueTerms}\t{np_data["150_stopwords"]}\t{deltaValueNP*-1}\t{termValueNP*-1}')

    deltaValueTerms = lossy_compression_tools.delta(term_data["150_stopwords"], term_data["stemming"])
    termValueTerms = lossy_compression_tools.delta(term_data["unfiltered"], term_data["stemming"])
    deltaValueNP = lossy_compression_tools.delta(np_data["150_stopwords"], np_data["stemming"])
    termValueNP = lossy_compression_tools.delta(np_data["unfiltered"], np_data["stemming"])
    print(f'stemming\t{term_data["stemming"]}\t{deltaValueTerms*-1 if deltaValueTerms > 0 else deltaValueTerms}\t{termValueTerms*-1 if termValueTerms > 0 else termValueTerms}\t{np_data["stemming"]}\t{deltaValueNP*-1}\t{termValueNP*-1}')
    print('\n')
