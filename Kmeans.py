# K Means
"""
    What is K-means Cluster Analysis
    How to calculate it

What is it?
    Hidden pattern in data with no appahrent relationships
    powerful way to identify hidden groups or clusters on a given number of clusters ( k )
    You must define the number of clusters ( k ) 

Algorithm
    1) define number of clusters
    2) set cluster centers randomly
    3) Assign points to clusters ( distance - smallest distance )
    4) Calculate center of each cluster 
    5) Assign points to the new clusters
    6) steps 4 & 5 are repeated until no change

Cons
    A big disadvantage is the final result depends on intial centroid
    to take into account, the whole procedure is reeated with different initial centroid multiple times

Elbow method to determine the no of clusters
    Graph - Y - sum of squarred distance
            X - no of clusters

"""