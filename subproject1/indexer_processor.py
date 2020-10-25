'''
In order to run subproject 1 entirely & generate the postings list, simply run: python subproject1/run.py 

The following block preprocesses the data from the corpus & produces a docID-term pair file. 
In order to run the preprocessor, execute the following command

    MODULE 1 EXECUTION (EXCLUSIVELY)
    python indexer_processor.py --path "<path to data>" -o "output/<output_file_name>.json"
    e.g. python subproject1/indexer_processor.py --path "Data" -o "output/unsorted_data.json"
    
    <path_to_data>: path to reuters data files
    <output_file_name>: name your file to see output
    MAKE SURE YOU RUN THE COMMAND IN THE PROJECT FOLDER!
'''
import indexer_helper, nltk, time, sys
from tqdm import tqdm
sys.path.append('utilities')
import asserts

# Read command line arguments
args = asserts.init_params()
path = args.path
asserts.common_check_path(path)

try:
    nltk.data.find('tokenizer/punkt')
except:
    nltk.download('punkt')

start = time.time()
for reuters_file_content in tqdm(indexer_helper.preprocess_reuters(path)):
    asserts.output(reuters_file_content)
end = time.time()
print(f'\nDone! Your file was created in {"{:.3f}".format(end-start)} seconds')