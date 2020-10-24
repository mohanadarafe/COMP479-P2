'''
The following block executes outputs lossy's compression table.

    LOOSY TABLE EXECUTION
    python indexer_builder.py -i "<input_file_name>.json"
    python loosy_compressor_execute.py --path "output/postings_list.json"
    
    <input_file_name>: name of the input file from indexer_builder
'''
import sub3, nltk, time, json, asserts
from tqdm import tqdm

# Read command line arguments
args = asserts.init_params()
path = args.path

start = time.time()
sub3.displayTable(path)
end = time.time()