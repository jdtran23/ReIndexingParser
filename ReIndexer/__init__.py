import json
from pprint import pprint

data = json.loads(open("reverse_index.json").read())

parsedData = []

for key in data:
    for obj in data[key]:
        parsedData.append({'snippet' : obj['snippet'], 'videoIndex' : obj['videoIndex'], 'startTime' : obj['startTime']})
        
print json.dumps(parsedData, indent=4)

# code snippet to remove duplicates
# http://stackoverflow.com/questions/17076345/remove-duplicates-from-json-data
all_snippets = [ each['snippet'] for each in parsedData ] # get 'ds' from above snippet
unique_stuff = [ parsedData[ all_snippets.index(id) ] for id in set(all_snippets) ]


with open("dedupped_transcription_index.json", "w") as outfile:
    json.dump(unique_stuff, outfile)
    
    
