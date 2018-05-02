import numpy as np
import pandas as pd

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD

from sklearn.feature_extraction.text import TfidfVectorizer

import matplotlib.pyplot as plt


df = pd.read_csv('trainingset_text.tsv', sep="\t", header=0)
documents = df['text'].values.tolist()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
# X = X.toarray()

"""
DBSCAN
"""

from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors(radius=1)
neigh.fit(X)
NearestNeighbors(algorithm='auto', leaf_size=30,)
A = neigh.radius_neighbors_graph(X)
A.toarray()

print A


db = DBSCAN(eps=1000000.0, min_samples=1, metric='euclidean').fit(A)

print (db.labels_)



# X = [[0], [3], [1]]
