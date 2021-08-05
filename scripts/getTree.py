import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    # print(path)
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d

with open("./story/story-tree.json","w", encoding="utf8") as f:
    json.dump(path_to_dict('./SCTranslationData/data/story'),f,ensure_ascii=False,indent=2,separators=(',',':'))
