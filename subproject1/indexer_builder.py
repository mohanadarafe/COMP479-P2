'''
In order to run subproject 1 entirely & generate the postings list, simply run: python subproject1/run.py 

The following block builds the postings list from the preprocessed data & outputs the postings list file.
In order to run the preprocessor, execute the following command

    MODULE 2 EXECUTION
    python indexer_builder.py -i "<input_file_name>.json"
    e.g. python indexer_builder.py -i "output/unsorted_data.json"
    
    <input_file_name>: name of the input file from indexer_builder
    MAKE SURE YOU RUN THE COMMAND IN THE PROJECT FOLDER!
'''
import indexer_helper, nltk, time, json, sys
from tqdm import tqdm
sys.path.append('utilities')
import asserts

# Read command line arguments
args = asserts.init_params()

start = time.time()
indexer_helper.build_postings_list((json.loads(line) for line in args.input_file))
end = time.time()
print(f'\nDone! Your postings list was created in {"{:.3f}".format(end-start)} seconds')