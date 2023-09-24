import json
import jsonlines

with open(
    "alpaca-en-zh.json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)

new_list = []

for item in data:
    new_list.append({"inputs":item["instruction"] + ' ' + item["input"], "targets":item["output"]})

with jsonlines.open('alpaca-en-zh.jsonl', 'w') as writer:
    writer.write_all(new_list)
