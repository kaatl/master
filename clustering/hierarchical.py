#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hcluster
import pylab

np.set_printoptions(threshold='nan')


# corpus = [
#     'This is the first document.',
#     'This is the second second document.',
#     'And the third one.',
#     'Is this the first document?',
#     ]


with open('trainingset_text.tsv', 'r') as file:
    corpus = file.readlines()




vectorizer = TfidfVectorizer()

txt_fitted = vectorizer.fit(corpus)
txt_transformed = txt_fitted.transform(corpus)
#print (“The text: “, corpus)
#print vectorizer.tf_

# print vectorizer.vocabulary_

X = vectorizer.fit_transform(corpus)
Z = X.toarray()

# print Z


print "Number of sentences %d" % Z.shape[0]
# https://stackoverflow.com/questions/10136470/unsupervised-clustering-with-unknown-number-of-clusters
thresh = 1.3
clusters = hcluster.fclusterdata(Z, thresh, criterion="distance")

print
print clusters
print
print "Threshold %3.2f" % (thresh)
print
for c in clusters:
    print c

print
print
print len(set(clusters))
print len(clusters)

# plotting
# plt.scatter(np.transpose(Z), c=clusters)
# plt.scatter(*np.transpose(Z), c=clusters)
# plt.axis("equal")
# title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
# plt.title(title)
# plt.show()


# for i in range(5,15):
#    thresh = i/10.
#    # clusters = hcluster.fclusterdata(np.transpose(Z), thresh)
#    pylab.scatter(*Z[:,:], c=clusters)
#    pylab.axis("equal")
#    title = "threshold: %f, number of clusters: %d” % (thresh, len(set(clusters)))"
#    print title
#    pylab.title(title)
#    pylab.draw()
#    time.sleep(0.5)
#    pylab.clf()
