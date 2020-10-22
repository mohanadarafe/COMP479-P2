'''
The following block executes the single term query

    QUERY PROCESSOR
    python queryProcessor.py --path "output/postings_list.json" -q "<query>"
    python queryProcessor.py --path "output/postings_list.json" -q "apple"
    
    <path_to_data>: path to reuters data files
    <query>: token to query
    <output_file_name>: name of the file you want to output
'''
import asserts, sub2, nltk, time, json
from tqdm import tqdm

# Read command line arguments
args = asserts.init_params()
path = args.path
query = args.query
'''
Module 2

Given the path of the reuter files, the following block will
output the docID-term pairs inside a file of your choice.
'''
start = time.time()
sub2.queryProcessor(path, query)
end = time.time()
print(f'\nDone! Your query was found in {"{:.3f}".format(end-start)} seconds')