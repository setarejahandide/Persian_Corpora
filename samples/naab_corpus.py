from datasets import load_dataset

# ==========================================================
# You should just change this part in order to download your 
# parts of corpus.
indices = {
    "train": [5, 1, 2],
    "test": [0, 2]
}
# ==========================================================


N_FILES = {
    "train": 126,
    "test": 3
}
_BASE_URL = "https://huggingface.co/datasets/SLPL/naab/resolve/main/data/"
data_url = {
    "train": [_BASE_URL + "train-{:05d}-of-{:05d}.txt".format(x, N_FILES["train"]) for x in range(N_FILES["train"])],
    "test": [_BASE_URL + "test-{:05d}-of-{:05d}.txt".format(x, N_FILES["test"]) for x in range(N_FILES["test"])],
}
for index in indices['train']:
    assert index < N_FILES['train']
for index in indices['test']:
    assert index < N_FILES['test']
data_files = {
    "train": [data_url['train'][i] for i in indices['train']],
    "test": [data_url['test'][i] for i in indices['test']]
}
print(data_files)
dataset = load_dataset('text', data_files=data_files)
# save to local disk
dataset.save_to_disk("./naab_subset")
