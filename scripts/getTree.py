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

story_dict = path_to_dict('./SCTranslationData/data/story')

with open("./story/story-tree.json","w", encoding="utf8") as f:
    json.dump(story_dict,f,ensure_ascii=False,indent=2,separators=(',',':'))

for item in story_dict['children']:
    idol_stories = {}
    story_list = []
    with open("./story/%s.json"%item['name'],"w", encoding="utf8") as f:
        for story_folder in item['children']:
            if story_folder["type"] == "directory":
                story_name = story_folder["name"]
                idol_stories[story_name] = [chapter["name"] for chapter in story_folder["children"]]
                story_list.append(story_folder["name"])
            else: 
                story_name = "其他剧情"
                idol_stories.setdefault(story_name, [])
                idol_stories[story_name].append(story_folder['name'])
                if story_name not in story_list:
                    story_list.append(story_name)
        json.dump({
            "list": story_list,
            "details": idol_stories
        }, f,ensure_ascii=False,indent=2,separators=(',',':'))
