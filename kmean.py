
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score



#read the dataset and convert in csv
data = pd.read_csv('/content/gdrive/My Drive/ML_Assignment4/iris.data',header=None,delimiter=",")
data.columns=['1','2','3','4','target']
data.to_csv(r'/content/gdrive/My Drive/ML_Assignment4/iris.csv',index=None)

data=pd.read_csv('/content/gdrive/My Drive/ML_Assignment4/iris.csv')

#convert target to numeric
data['target'].unique()

target = {'Iris-setosa': 0,'Iris-versicolor': 1,'Iris-virginica': 2}

data.target = [target[item] for item in data.target]

data

#divide in X and y
x = data.iloc[:, [1,2,3,4]].values
Y=data["target"]

#split data in test and training data
X_train, X_test, y_train, y_test = train_test_split(x, Y, train_size=0.7,test_size=0.3, random_state=142)

y_new=y_test.values.tolist()


#find error and optimal cluster 
distortions = []
error = []
sum=[]
K = range(1,26)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X_train,y_train)
    y_pred=kmeanModel.predict(X_test)
    y_new=y_test.values.tolist()
    for i in y_pred:
      sum.append((y_new[i]-y_pred[i])**2)
    error.append(np.sum(sum))
    distortions.append(kmeanModel.inertia_)

#craete plot for showing error on diffrent number of cluster
plt.figure(figsize=(16,8))
plt.plot(K, error,'bx-', color = 'orange')
plt.xlabel(' cluster')
plt.ylabel('error')
plt.title('error for cluster')
plt.show()

#showing no of cluster through elbow method
plt.figure(figsize=(16,8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('Cluster')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()



#plot scatter graph for cluster
plt.figure(figsize=(16,8))
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
label = kmeans.fit_predict(x)
plt.scatter(x[:,0],x[:,1], c=label,cmap='plasma')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], s=200,color='red')

#accuracy score for trainig data
y_pred = kmeans.predict(X_train)
acc=accuracy_score(y_train, y_pred)
print("training accuracy:",acc)
#accuracy score for testing data
y_pred=kmeans.predict(X_test) 
acc=accuracy_score(y_test, y_pred)
print("testing accuracy:",acc)

correct=0
for i in range(len(x)):
    predict_me = np.array(x[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == Y[i]:
        correct += 1

print(correct/len(x))

