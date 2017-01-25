# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:01:25 2016

@author: linjen
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
# pca = PCA(n_components=2, svd_solver='full')
# pca = PCA(n_components=1, svd_solver='arpack')
pca.fit(X)
pca_score = pca.explained_variance_ratio_

print(pca.explained_variance_ratio_)

# plot PCA
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca_score, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')
