
"""
Seaborn
https://seaborn.pydata.org/generated/seaborn.clustermap.html
"""

#
# import seaborn as sns; sns.set(color_codes=True)
# iris = sns.load_dataset("iris")
# species = iris.pop("species")
# g = sns.clustermap(iris)



"""
http://scikit-learn.org/stable/tutorial/statistical_inference/unsupervised_learning.html
"""
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hcluster
import numpy as np
import pandas as pd
from keras.preprocessing.sequence import pad_sequences
np.set_printoptions(threshold='nan')

input_file = 'testset.tsv'
df = pd.read_csv(input_file, sep="\t", header=0)
df['sequence'] = df['sequence'].apply(lambda x: [e for e in x.split(',')])
df['sequence'] = df['sequence'].apply(lambda liste: [[float(e) for e in x.split()] for x in liste])


data = pad_sequences(df['sequence'], dtype='float', padding="post", maxlen=50)

# print data[0]
print len(data)

# clustering
thresh = 0.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")
# clusters = hcluster.fclusterdata(data[0], 2, criterion='maxclust', metric='euclidean', depth=1, method='centroid')

# for c in clusters:
#     print c


print clusters
print
print
print len(set(clusters))
print len(clusters)

"""Dummy data"""
# generate 3 clusters of each around 100 points and one orphan point

# N=100
# data = np.random.randn(3*N, 2)
# data[:N] += 5
# data[-N:] += 10
# data[-1:] -= 20
# clusters = hcluster.fclusterdata(data, thresh, criterion="distance")


# plotting
# plt.scatter(*np.transpose(data), c=clusters)
# plt.axis("equal")
# title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
# plt.title(title)
# plt.show()
