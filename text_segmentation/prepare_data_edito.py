import requests

from edito import get_chapters
from edito.parsers import parse_xml
from os import listdir
from os.path import isfile, join

import tqdm
import json
import os

data_path = "data/"

os.makedirs(data_path, exist_ok=True)

files_paths = "../edito/xml/" # Need to have the repo cloned (https://gitlab.dnm.radiofrance.fr/r-et-d-openapi/datasets/edito.git)
files = [f for f in listdir(files_paths) if isfile(join(files_paths, f))]

transcriptions = []

for file in tqdm.tqdm(files):
    script, mid = parse_xml(f"../edito/xml/{file}")

    transcript = requests.get(
        f"https://apipreprod.priv.radiofrance.dev/troubadour/api/audios/{mid}",
    ).json().get("transcript")

    if transcript :

        chapters = get_chapters(script, transcript)

        chapter_starts = [chap["start"] for chap in chapters]

        for el in transcript:
            el["mid"] = mid

            if el["start"] in chapter_starts:
                el["transition"] = 1
            else:
                el["transition"] = 0

        transcriptions.append(transcript)

with open(f"{data_path}transcription_test.jsonl", "w") as f:
    for data in transcriptions:
        json.dump(data, f)
        f.write('\n')


