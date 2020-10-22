'''
The following block executes the first block Naive Indexer. In order to run the indexer, execute the following command

    MODULE 1 EXECUTION
    python indexer_processor.py --path "<path to data>" -o "output/<output_file_name>.json"
    python indexer_processor.py --path "./data" -o "output/unsorted_data.json"
    
    <path_to_data>: path to reuters data files
    <output_file_name>: name your file to see output
'''
import asserts, sub1_modules, nltk, time
from tqdm import tqdm

# Read command line arguments
args = asserts.init_params()
path = args.path
asserts.common_check_path(path)

try:
    nltk.data.find('tokenizer/punkt')
except:
    nltk.download('punkt')

'''
Module 1

Given the path of the reuter files, the following block will
output the docID-term pairs inside a file of your choice.
'''
start = time.time()
for reuters_file_content in tqdm(sub1_modules.preprocess_reuters(path)):
    asserts.output(reuters_file_content)
end = time.time()
print(f'\nDone! Your file was created in {"{:.3f}".format(end-start)} seconds')