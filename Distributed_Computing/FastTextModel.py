# Import packages
from dask.distributed import Client, LocalCluster
from dask import delayed

import dask.bag as db
import dask.dataframe as ddf
import os
import json
from operator import itemgetter
from operator import add

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import word_tokenize

from collections import Counter

import time

import numpy as np

import io
import fasttext


def embed(text, model):
    text_split = text.split()
    text_embedded = []
    #just to be safe that the .bin model does predict everything
    for t in text_split:
        try:
            text_embedded.append(model[t])
        except:
            pass
    text_string = [["%.8f" % n for n in w] for w in text_embedded]

    return text_string


def embed_dict(dict, model):
    return{
        "paper_id": dict["paper_id"],
        "title": embed(dict['title'], model)
    }


def flatten(reco):
    return {
        "paper_id": reco[0],
        "title": reco[1]['title']
    }


def make_titles():
    # Import data
    filename = os.path.join('data', 'papers_in_json_singleline', '*.json')
    lines = db.read_text(filename)
    js = lines.map(json.loads).repartition(10)
    metas = js.pluck(["paper_id", "metadata"])

    # Load the FastText model
    ft = fasttext.load_model('/home/alessandro/Downloads/cc.en.300.bin')

    # Get titles and embed them
    titles = metas.map(flatten).compute()
    ed = [embed_dict(d, ft) for d in titles]
    #print(ed[1])
    
    # Save embedded paper titles
    for i in range(len(ed)):
        fname="data/embedded_papers/embTitle"+str(i)+".json"
        with open (fname, 'w') as wf:
            json.dump(ed[i], wf)
            

if __name__ == "__main__":
    cluster=LocalCluster(n_workers=4)
    client= Client(cluster)   
    
    make_titles()
    client.close()
    cluster.close()