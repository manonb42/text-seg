# text_segmentation

The objective of this repo is to benchmark different types of segmentation, mainly from the [rf-mosaic](https://gitlab.dnm.radiofrance.fr/r-et-d-openapi/packages/rf-mosaic.git) repo. 

For this, we need to gather data and a way to evaluate the outputs of our segmentation. 

## Getting Started

To work with this project, ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed on your system.

Once Poetry is installed, set up the project environment by running:

```bash
poetry install        # Install project dependencies  
poetry shell          # Activate the virtual environment
```

## Data Preparation

The objective of the data preparation step is to structure the dataset as close as possible from Radio France's data.

### Claire dataset

To prepare the dataset for this project, run the `prepare_data_claire.py` script. This script downloads the [Claire Dataset](https://huggingface.co/datasets/OpenLLM-France/Claire-Dialogue-French-0.1/tree/main/FR) test set from Hugging Face and formats it for segmentation tasks.

❗ Warning : Even if INA used it for evaluation, we don't know how we could use this dataset for segmentation. We still keep this code in the repo in case we ifnd a solution.

### Edito dataset

The Edito dataset was created to combine the journalists' scripts to get a chapter divisions of the transcripts. With the [Edito Dataset](https://gitlab.dnm.radiofrance.fr/r-et-d-openapi/datasets/edito.git) and the package `rf-edito` we can gather 106 segmented transcriptions for our evaluation. 

Please note that to use this data you need to clone the repo of the dataset and launch `prepare_data_edito.py`.

The dataset will be ouput in a **jsonl** format where each line is a transcript in a json format.


## Evaluation

We use `nltk` metrics of [Pk](https://tedboy.github.io/nlps/generated/generated/nltk.pk.html) and [windowdiff](https://tedboy.github.io/nlps/generated/generated/nltk.windowdiff.html#nltk.windowdiff) to evaluate the segmentation.

