import os
from subprocess import *

if not os.path.isdir("output"):
    os.makedirs("output")
else:
    os.replace("output", "output")

Popen('python subproject1/indexer_processor.py --path "Data" -o "output/unsorted_data.json"', shell=True).wait()
Popen('python subproject1/indexer_builder.py -i "output/unsorted_data.json"', shell=True).wait()