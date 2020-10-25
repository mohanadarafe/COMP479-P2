'''
The following block executes outputs lossy's compression table.

    LOSSY TABLE EXECUTION
    python subproject3/lossy_compression_query.py -q <query>
    python subproject3/lossy_compression_query.py -q "apple"
    
    <query>: token to query
'''
import lossy_compression_helper, time, sys, json
sys.path.append('utilities')
import asserts

# Read command line arguments
args = asserts.init_params()
query = args.query
assert len(query) == 1, "Enter only one query term!"
query_term = query[0].replace(" ", "")
PATH = "output/postings_list.json"

start = time.time()
dictionary = lossy_compression_helper.getCompressedDictionary(PATH)
assert type(dictionary) == dict, "Something went wrong with the postings list, make sure you ran module 1 first!"

with open("output/compressedSampleQueries.json", 'a', encoding="utf-8") as outputFile:
    if query_term not in dictionary:
        print("The query term you input is not in the corpus!")
        exit()

    output = {query_term: dictionary[query_term]}
    json.dump(output, outputFile, indent=3)

end = time.time()
print(f'\nDone! Your query was found in {"{:.3f}".format(end-start)} seconds')