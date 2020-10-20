import asserts
import indexer
import nltk

# Read command line arguments
args = asserts.init_params()
path = args.path
asserts.common_check_path(path)
nltk.download('punkt')

# Calling your solution. Execute your solution in the following method in solutions.py file
for reuters_file_content in indexer.get_documents(path):
    asserts.output(reuters_file_content)
