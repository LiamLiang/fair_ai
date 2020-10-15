import os 
import wget
import gzip
import numpy as np
from tqdm import tqdm


def get_glove_100d():
    if 'glove.6B.100d.txt.gz' not in os.listdir():
        wget.download('https://github.com/allenai/spv2/raw/master/model/glove.6B.100d.txt.gz', './glove.6B.100d.txt.gz')
    embeddings_dict = {}
    with gzip.open('glove.6B.100d.txt.gz', 'r') as f:
        for line in tqdm(f):
            values = line.decode().split()
            word = values[0]
            vector = np.asarray(values[1:], "float32")
            embeddings_dict[word] = vector
    return embeddings_dict