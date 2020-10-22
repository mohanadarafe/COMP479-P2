'''
The following block executes the first block Naive Indexer. In order to run the indexer, execute the following command

    MODULE 2 EXECUTION
    python indexer_builder.py -i "<input_file_name>.json"
    python indexer_builder.py -i "output/unsorted_data.json"
    
    <path_to_data>: path to reuters data files
    <input_file_name>: name of the input file from indexer_builder
    <output_file_name>: name of the file you want to output
'''
import asserts, sub1_modules, nltk, time, json
from tqdm import tqdm

# Read command line arguments
args = asserts.init_params()
'''
Module 2

Given the path of the reuter files, the following block will
output the docID-term pairs inside a file of your choice.
'''
start = time.time()
sub1_modules.build_postings_list((json.loads(line) for line in args.input_file))
end = time.time()
print(f'\nDone! Your file was sorted created in {"{:.3f}".format(end-start)} seconds')