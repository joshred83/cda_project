"""
Preprocesses the input data frame by imputing missing values with median, standardizing the features, and applying PCA for dimensionality reduction.

Fits a KMeans clustering model on the PCA-transformed data and plots the clusters.
"""

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def preprocess(df):
    imputer = SimpleImputer(strategy="median")
    imputed_df = pd.DataFrame(imputer.fit_transform(df))
    scaled_df = StandardScaler().fit_transform(imputed_df)
    return scaled_df


def display_loadings(fitted_pca, features):
    loadings = fitted_pca.components_
    order = np.argsort(abs(loadings[0, :]))[::-1]
    loadings = loadings[:, order]
    features = [features[i] for i in order]
    loadings = pd.Series(loadings[0, :], index=features)
    loadings.plot(kind="barh")
    return loadings


df = pd.read_csv("data/DS_salary_factors.csv", na_values=0)

numeric_features = df.select_dtypes(include="number").columns
X = df[numeric_features]
X = preprocess(X)
pca = PCA().fit(X)
X_pca = pca.transform(X)
kmeans = KMeans(n_clusters=4, random_state=0).fit(X_pca)
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans.labels_, cmap="viridis")
for i, label in enumerate(df.GeoName):
    ax.text(X_pca[i, 0], X_pca[i, 1], label, fontsize=8)