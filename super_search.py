from subprocess import call
import os
import json
import sys

if len(sys.argv) < 2:
    print("Not enough arguments!")

search_type = sys.argv[1]
search_terms = sys.argv[2:]

with open(os.path.expanduser('~/.super_search.json')) as config:
    config_json = json.load(config)

browser = config_json['browser']
search_type_config = config_json['search'][search_type]
delimiter = search_type_config['delimiter']
search_url = search_type_config['url']

search_term = search_url.format(delimiter.join(search_terms))

print(search_term)

call([browser, search_term])
