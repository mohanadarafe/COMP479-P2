from subprocess import *
Popen('python subproject1/indexer_processor.py --path "Data" -o "output/unsorted_data.json"', shell=True).wait()
Popen('python subproject1/indexer_builder.py -i "output/unsorted_data.json"', shell=True).wait()