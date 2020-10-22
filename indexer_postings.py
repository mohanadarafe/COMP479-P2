'''
The following block executes the first block Naive Indexer. In order to run the indexer, execute the following command

    MODULE 3 EXECUTION
    python indexer_sorter.py -i "<input_file_name>.json" -o "<output_file_name>.json"
    python indexer_postings.py -i "output/sorted_data.json" -o "output/postings.json"
    
    <path_to_data>: path to reuters data files
    <input_file_name>: name of the input file from indexer_builder
    <output_file_name>: name of the file you want to output
'''
import asserts, indexer, nltk, time, json
from tqdm import tqdm

# Read command line arguments
args = asserts.init_params()
'''
Module 3

Given the path of the reuter files, the following block will
output the docID-term pairs inside a file of your choice.
'''
start = time.time()
for reuters_file_content in tqdm(indexer.module3((json.loads(line) for line in args.input_file))):
    asserts.output(reuters_file_content)
end = time.time()
print(f'\nDone! Your file was sorted created in {"{:.3f}".format(end-start)} seconds')