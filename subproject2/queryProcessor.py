'''
The following block executes the single term query

    QUERY PROCESSOR
    python subproject2/queryProcessor.py -q "<query>"
    e.g. python subproject2/queryProcessor.py -q "apple"
    
    <query>: token to query
'''
import queryHelper, time, json, sys
from tqdm import tqdm
sys.path.append('utilities')
import asserts

# Read command line arguments
args = asserts.init_params()
query = args.query

start = time.time()
queryHelper.queryProcessor(query)
end = time.time()
print(f'\nDone! Your query was found in {"{:.3f}".format(end-start)} seconds')