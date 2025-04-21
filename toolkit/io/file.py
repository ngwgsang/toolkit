import json
import csv
import pickle

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path, indent=2):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)

def load_jsonl(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def save_jsonl(data_list, path):
    with open(path, 'w', encoding='utf-8') as f:
        for entry in data_list:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def save_txt(lines, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def save_pickle(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
