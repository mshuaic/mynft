import json
import pathlib


template = {
    "external_url": ...,
    "image": ...,
    "name": ...,
}

with open("cids", "r") as f:
    cids = f.read().split()


with open("cids", "r") as f:
    cids = f.read().split()


filenames = list(map(lambda x: x.name, pathlib.Path('dogs').glob('*.jpg')))
filenames = sorted(filenames)

URI_PROVENACE = []

for i, (cid, filename) in enumerate(zip(cids, filenames)):
    template["image"] = f"ipfs://{cid}"
    template["name"] = filename
    template["external_url"] = f"https://mshuaic.github.io/mynft/mint/dogs/{filename}"
    # template["description"] = q
    with open(f"./URIs/{i}", "w") as f:
        json.dump(template, f)

    URI_PROVENACE += template.copy(),


with open("URI_PROVENACE.json", "w") as f:
    json.dump(URI_PROVENACE, f)
