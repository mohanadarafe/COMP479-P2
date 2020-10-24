import math, json, lossy_compression_tools
from nltk.stem import PorterStemmer 
from tqdm import tqdm

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

def displayTable(path):
    term_data = computeTermLossy(path)
    # np_data = computeNPLossy(path)

    print("\n\t\t\tTerms\t\tNP Postings")
    print("-" * 60)
    print("\t\tfreq\tΔ%\tT%\tfreq\tΔ%\tT%")
    print("-" * 60)

    print(f'unfiltered\t{term_data["unfiltered"]}\t\t\t{term_data["unfiltered"]}')

    deltaValue = lossy_compression_tools.delta(term_data["unfiltered"], term_data["no_number"])
    termValue = lossy_compression_tools.delta(term_data["unfiltered"], term_data["no_number"])
    print(f'no numbers\t{term_data["no_number"]}\t{deltaValue*-1 if deltaValue > 0 else deltaValue}\t{termValue*-1 if termValue > 0 else termValue}')

    deltaValue = lossy_compression_tools.delta(term_data["no_number"], term_data["case_folding"])
    termValue = lossy_compression_tools.delta(term_data["unfiltered"], term_data["case_folding"])
    print(f'case folding\t{term_data["case_folding"]}\t{deltaValue*-1 if deltaValue > 0 else deltaValue}\t{termValue*-1 if termValue > 0 else termValue}')

    deltaValue = lossy_compression_tools.delta(term_data["case_folding"], term_data["30_stopwords"])
    termValue = lossy_compression_tools.delta(term_data["unfiltered"], term_data["30_stopwords"])
    print(f'30 stopwords\t{term_data["30_stopwords"]}\t{deltaValue*-1 if deltaValue > 0 else deltaValue}\t{termValue*-1 if termValue > 0 else termValue}')

    deltaValue = lossy_compression_tools.delta(term_data["30_stopwords"], term_data["30_stopwords"])
    termValue = lossy_compression_tools.delta(term_data["unfiltered"], term_data["150_stopwords"])
    print(f'150 stopwords\t{term_data["150_stopwords"]}\t{deltaValue*-1 if deltaValue > 0 else deltaValue}\t{termValue*-1 if termValue > 0 else termValue}')

    deltaValue = lossy_compression_tools.delta(term_data["30_stopwords"], term_data["stemming"])
    termValue = lossy_compression_tools.delta(term_data["unfiltered"], term_data["stemming"])
    print(f'stemming\t{term_data["stemming"]}\t{deltaValue*-1 if deltaValue > 0 else deltaValue}\t{termValue*-1 if termValue > 0 else termValue}')

