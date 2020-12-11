# Kmeans-algorithm
Kmeans algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups (clusters) where each data point belongs to only one group. It tries to make the intra-cluster data points as similar as possible while also keeping the clusters as different (far) as possible. It assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s centroid (arithmetic mean of all the data points that belong to that cluster) is at the minimum. The less variation we have within clusters, the more homogeneous (similar) the data points are within the same cluster.

A simple K-Means Clustering model implemented in python. The class KMeans is imported from sklearn.cluster library. In order to find the optimal number of cluster for the dataset, use elbow method on parameters. visualize using scatter plot.

Kmean optimal number of clusters using the elbow method. Plot the error vs number of clusters graph while
using the elbow method. 
