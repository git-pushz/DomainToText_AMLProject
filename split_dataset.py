import json
import random

with open("image_descriptions.json", "r") as read_file:
    data = json.load(read_file)

data_names = []
for d in data:
    data_names.append(d['image_name'])

random.shuffle(data_names)

# n_train = int(len(data_names)*0.6)
# n_val = int(len(data_names)*0.15)

# train = data_names[:n_train]

# val = data_names[n_train:n_train+n_val]

# test = data_names[n_train+n_val:]

split_data = {}
split_data['train'] = data_names
# split_data['train'] = train
# split_data['val'] = val
# split_data['test'] = test

with open("image_splits.json", "w") as write_file:
    json.dump(split_data, write_file)
