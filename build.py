import json, os

with open("projects/hou-minghao-world/gallery_data.json") as f:
    gallery = json.load(f)

template = open("projects/hou-minghao-world/template.html").read()
out = template.replace("__GALLERY_JSON__", json.dumps(gallery))

with open("projects/hou-minghao-world/index.html", "w") as f:
    f.write(out)

print("Built index.html! Size:", os.path.getsize("projects/hou-minghao-world/index.html") / 1024 / 1024, "MB")
