#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn import metrics
from sklearn.metrics import silhouette_samples, silhouette_score

from scipy.spatial.distance import cdist
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

import math
import pandas as pd
import numpy as np
import sys
import re
# from nltk.stem import PorterStemmer, SnowballStemmer

from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

from nltk.stem.snowball import NorwegianStemmer
from rippletagger.tagger import Tagger



tagger = Tagger(language="no")
stemmer = NorwegianStemmer()

reload(sys)
sys.setdefaultencoding('utf-8')


df = pd.read_csv('datasets/trainingset_fulltext.tsv', sep="\t", header=0)
# df = pd.read_csv('datasets/testset_text.tsv', sep="\t", header=0)
documents = df['text'].values.tolist()

stopwords = []
with open('datasets/stopword.txt', 'r') as file: lines = file.readlines()
for x in lines: stopwords.append(str(x[:-1]))


data = []

for x in documents:
    string = ""

    sentences = x.split(".")

    for sentence in sentences:
        # sentence = sentence.decode('utf-8')
        sentence_pos = tagger.tag(sentence.decode('utf-8'))
        # print "====="
        # print sentence
        # print sentence_pos
        # print
        # sentence_pos = sentence.split()
        for w in sentence_pos:
            if w in stopwords: continue
            if (w[1] != "PROPN") and (w[1] != "NOUN" ): continue

            word = w[0]
            word = word.lower()
            word = re.sub(r'[.,=())-]','',word)

            try:
                word = stemmer.stem(word)
            except UnicodeDecodeError:
                message = "UnicodeDecodeError"

            string += word + " "

    data.append(string)


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data)
X = X.toarray()


true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1000)
model.fit(X)




def cluster_print_2d():

    pca = PCA(n_components = 2).fit(X)
    data2D = pca.transform(X)
    # plt.scatter(data2D[:,0], data2D[:,1])

    centers2D = pca.transform(model.cluster_centers_)

    # http://www.dummies.com/programming/big-data/data-science/how-to-visualize-the-clusters-in-a-k-means-unsupervised-learning-model/
    c0, c1, c2, c3, c4, c5 = None, None, None, None, None, None
    for i in range(0, data2D.shape[0]):
        if model.labels_[i] == 0:
            c0 = plt.scatter(data2D[i,0],data2D[i,1], c='r', marker='o')
        elif model.labels_[i] == 1:
            c1 = plt.scatter(data2D[i,0],data2D[i,1], c='g', marker='o')
        elif model.labels_[i] == 2:
            c2 = plt.scatter(data2D[i,0],data2D[i,1], c='b', marker='o')
        elif model.labels_[i] == 3:
            c3 = plt.scatter(data2D[i,0],data2D[i,1], c='purple', marker='o')
        elif model.labels_[i] == 4:
            c4 = plt.scatter(data2D[i,0],data2D[i,1], c='orange', marker='o')
        elif model.labels_[i] == 5:
            c5 = plt.scatter(data2D[i,0],data2D[i,1], c='yellow', marker='o')

    plt.legend([c0, c1, c2, c3, c4, c5],['Cluster 0', 'Cluster 1','Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5'])
    plt.show()



#https://stackoverflow.com/questions/28160335/plot-a-document-tfidf-2d-graph

def cluster_print_3d():

    pca = PCA(n_components = 3).fit(X)
    data3D = pca.transform(X)
    centers3D = pca.transform(model.cluster_centers_)


    fig = plt.figure()

    ax = Axes3D(fig)
    # ax.scatter(data3D[0], data3D[1], data3D[2])
    for i in range(0, data3D.shape[0]):
        if model.labels_[i] == 0:
            c0 = ax.scatter(data3D[i,0], data3D[i,1], data3D[i,2], c='r', marker='o')
        elif model.labels_[i] == 1:
            c1 = ax.scatter(data3D[i,0], data3D[i,1], data3D[i,2], c='g', marker='o')
        elif model.labels_[i] == 2:
            c2 = ax.scatter(data3D[i,0], data3D[i,1], data3D[i,2], c='b', marker='o')
        elif model.labels_[i] == 3:
            c3 = ax.scatter(data3D[i,0], data3D[i,1], data3D[i,2], c='yellow', marker='o')
        elif model.labels_[i] == 4:
            c4 = ax.scatter(data3D[i,0], data3D[i,1], data3D[i,2], c='orange', marker='o')
        elif model.labels_[i] == 5:
            c5 = ax.scatter(data3D[i,0], data3D[i,1], data3D[i,2], c='purple', marker='o')

    ax.scatter(centers3D[:,0], centers3D[:,1], centers3D[:,2], c='black', marker='x')
    ax.legend([c0, c1, c2, c3, c4, c5],['Cluster 0', 'Cluster 1','Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5'])
    plt.show()

cluster_print_2d()
cluster_print_3d()

def top_terms_per_cluster():
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :3]:
            print(' %s' % terms[ind]),
        print

top_terms_per_cluster()


def predict():
    print("\n")
    print("Prediction...")

    Y = vectorizer.transform(["Mye svindel i det offentlige.".decode('utf-8')])
    prediction = model.predict(Y)
    print("Cluster: %d" % prediction)

    Y = vectorizer.transform(["Det har vært en arbeidsulykke.".decode('utf-8')])
    prediction = model.predict(Y)
    print("Cluster: %d" % prediction)

    print

# predict()

def exponential_fit(x, a, b, c):
    return a*np.exp(-b*x)


def ockhamz_razor(x,y ):

    #https://stackoverflow.com/questions/48506782/scipy-curve-fit-how-to-plot-the-fitted-curve-beyond-the-data-points
    fitting_parameters, covariance = curve_fit(exponential_fit, x, y)
    a, b, c = fitting_parameters

    x_min = 0
    x_max = len(y) + 1
    x_fit = np.linspace(x_min, x_max, 100)

    return x_fit, exponential_fit(x_fit, *fitting_parameters)


def k_means_elbow(X):
    #https://pythonprogramminglanguage.com/kmeans-elbow-method/
    print ("Elbowwwww")

    plt.plot()
    colors = ['b', 'g', 'r']
    markers = ['o', 'v', 's']

    # k means determine k
    distortions = []
    silhouette = []
    K = range(2,20)
    # print len(X)
    print("Find distortions...")
    for k in K:
        # print k
        kmeanModel = KMeans(n_clusters=k, max_iter=6, n_init=1).fit(X)
        kmeanModel.fit(X)
        distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'hamming'), axis=1)) / X.shape[0])

        labels = kmeanModel.fit(X)
        silhouette_avg = silhouette_score(X, labels.labels_, metric='hamming')

        silhouette.append(silhouette_avg)


# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
#hamming - ok?
#canberra - ok?
#matching - ok?
#rogerstanimoto - ok?
#sokalmichener - ok?

    x = np.arange(2, len(distortions) + 2, 1)
    y = np.array(distortions)

    # Ockhamz razor
    x_fit, regression = ockhamz_razor(x,y)

    print("Plotting")
    # print distortions
    # print silhouette
    # Plot the elbow
    plt.plot(K, distortions, 'bo-', label="Distortion")
    plt.plot(x_fit, regression, 'g-', label='Ockhamz razor')
    # plt.plot(K, silhouette, 'ro-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    axes = plt.gca()
    axes.set_ylim([0, max(distortions) + 0.1])
    # axes.set_xlim([0, len(distortions) + 2])
    plt.xticks(np.arange(0, len(distortions) + 2, 1))
    plt.title('The Elbow Method showing the optimal k')
    plt.legend()
    plt.show()


# k_means_elbow(X)

# print tagger.tag("En mann".decode('utf-8'))
