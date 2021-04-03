from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

data = pd.read_csv('../Data/data.csv', header=None)
data = np.asarray(data)

# separate features and labels    
X = data[:,0:2]
y = data[:,2]

# split the data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initiate Decision Tree Model
tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train, y_train)

# get predictions
y_pred = tree_clf.predict(X_test)

# Calculate accuracy score
acc = accuracy_score(y_test, y_pred)
print(acc)