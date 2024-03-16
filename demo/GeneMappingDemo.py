# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Sample genetic data (example)
genetic_data = {
    'Gene1': [0.1, 0.5, 0.3, 0.9],
    'Gene2': [0.4, 0.8, 0.2, 0.6],
    'Gene3': [0.7, 0.2, 0.6, 0.3],
    'Gene4': [0.8, 0.3, 0.1, 0.7],
    'Gene5': [0.2, 0.6, 0.9, 0.4],
    'Gene6': [0.5, 0.9, 0.4, 0.8],
    'Gene7': [0.3, 0.1, 0.8, 0.2],
    'Gene8': [0.6, 0.4, 0.7, 0.1],
    # Add more genes and their expression levels as needed
}

# Create a DataFrame from the genetic data
df = pd.DataFrame(genetic_data)

# Perform principal component analysis (PCA) for dimensionality reduction
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df.T)

# Perform K-means clustering on the principal components
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(principal_components)

# Function to map genes based on expression levels and clustering results
def map_genes(dataframe, clusters):
    gene_mapping = {}
    for i, gene in enumerate(dataframe.columns):
        mean_expression = dataframe[gene].mean()
        cluster = clusters[i]
        if mean_expression > 0.5:
            gene_mapping[gene] = f'Cluster {cluster + 1}: High expression'
        else:
            gene_mapping[gene] = f'Cluster {cluster + 1}: Low expression'
    return gene_mapping

# Perform gene mapping
mapped_genes = map_genes(df, clusters)

# Print the mapped genes
print("Gene Mapping Results:")
for gene, expression_level in mapped_genes.items():
    print(f"{gene}: {expression_level}")

# Visualize gene expression levels and clusters in 2D space using PCA
plt.figure(figsize=(10, 6))
for i, cluster in enumerate(clusters):
    plt.scatter(principal_components[i, 0], principal_components[i, 1], color=f'C{cluster}', label=f'{df.columns[i]}: Cluster {cluster + 1}')
plt.title('Gene Expression Levels and Clusters (PCA)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.tight_layout()
plt.show()
