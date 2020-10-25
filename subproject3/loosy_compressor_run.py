'''
The following block executes outputs lossy's compression table.

    LOSSY TABLE EXECUTION
    python subproject3/loosy_compressor_execute.py

'''
import lossy_compression_helper, time, sys
sys.path.append('utilities')
import asserts

# Read command line arguments
args = asserts.init_params()
PATH = "output/postings_list.json"

start = time.time()
lossy_compression_helper.displayTable(PATH)
end = time.time()