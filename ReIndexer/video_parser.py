import json

data = json.loads(open("video_title_source.json").read())

parsedData = []
videoIndex = 0

for video in data:
    parsedData.append({"videoIndex" : videoIndex, "title" : video[0] , "source" : video[1][45:-4]})
    videoIndex = videoIndex + 1
    
print json.dumps(parsedData, indent=4)

with open("video_index_title_source_v2.json", "w") as outfile:
    json.dump(parsedData, outfile)