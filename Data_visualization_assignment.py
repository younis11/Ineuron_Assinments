import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import datasets


iris = datasets.load_iris()
data = iris.data
target = iris.target


pca = PCA(n_components=3)
data_3d = pca.fit_transform(data)


import pandas as pd
df = pd.DataFrame(data=data_3d, columns=['PC1', 'PC2', 'PC3'])
df['Class'] = target


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


colors = ['r', 'g', 'b']


for i in range(3):
    class_data = df[df['Class'] == i]
    ax.scatter(class_data['PC1'], class_data['PC2'], class_data['PC3'], c=colors[i], label=f'Class {i}')


ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

plt.show()
