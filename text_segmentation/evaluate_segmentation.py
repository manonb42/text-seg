from nltk.metrics import windowdiff, pk
import json

file_name = "output/transcription_test_treeseg.jsonl"

with open(file_name, "r") as f:
    all_data = [json.loads(line) for line in f]

results = []

for data in all_data : 
    true_transitions = [x["transition"] for x in data]
    pred_transitions = [x["transition_hat"] for x in data]

    true_K = int(sum(true_transitions)) + 1

    diff_k = int(round(len(true_transitions) / (true_K * 2.0)))
    tr_str = "".join([str(lab) for lab in true_transitions])
    tr_hat_str = "".join([str(lab) for lab in pred_transitions])

    results.append(
        {
            "windiff" : windowdiff(tr_str, tr_hat_str, diff_k),
            "pk" : pk(tr_str, tr_hat_str, diff_k)
        }
    )

with open("output/results.json", "w") as f:
    json.dump(results, f)


