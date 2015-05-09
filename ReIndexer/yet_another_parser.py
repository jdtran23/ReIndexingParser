import json

data = json.loads(open("video_index_title_source_v2.json").read())
data2 = json.loads(open("dedupped_transcription_index.json").read())

parsedData = []
videoIndex = 0

for captions in data2:
    for video in data:
        if video['videoIndex'] is captions['videoIndex']:
            parsedData.append({"videoIndex" : captions['videoIndex'], "snippet" : captions['snippet'] , "startTime" : captions['startTime'], "title" : video['title'], "source" : video['source']})
    
print json.dumps(parsedData, indent=4)

with open("video_index_title_source_v3.json", "w") as outfile:
    json.dump(parsedData, outfile)