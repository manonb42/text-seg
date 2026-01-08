import pandas as pd
import re
import os
from datasets import load_dataset

def split_text(line):
    """
    Get one segment for each line (getting closer to the RF data)
    """
    line_cleaned = re.sub(r"\[.*?:\]\s*", "", str(line)) 
    text_splitted = re.split(r'\.\s+|\n', line_cleaned)
    return [seg.strip() for seg in text_splitted if seg.strip()]

data_path = "data/"

os.makedirs(data_path, exist_ok=True)

csv_path = f"{data_path}claire_dataset.csv"

df = load_dataset("OpenLLM-France/Claire-Dialogue-French-0.1", split="test").to_pandas()

df['transcription_number'] = df.index.map(lambda x: f'transcription_{x}')

df["text"] = df["text"].apply(split_text)

grouped_df = df.groupby("transcription_number", as_index=False)["text"].sum()

grouped_df.to_json(f"{data_path}claire_dataset_clean.jsonl", lines=True, orient="records", force_ascii=False)
