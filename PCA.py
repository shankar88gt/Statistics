"""
PCA Basics

Principal Component Analysis (PCA) one step at a time using Singular Value Decomposition (SVD).
what PCA does, how it does it, and how to use it to get deeper insight into your data.






Pratical Tips for PCA
    1) Scale the data ( without scaling - bisased)
            The std practice is to divide by Standard deviation. depending on the variation the scaling changes 
    2) Make sure your data is centered
            not every PCA does this by default. e.g. SVD fits a line thru origin. 
    3) There is PC for each variables int he dataset. if there are fewer samples than variables then the num of samples puts an upper bound
            PC's which explains the maximum variance

"""