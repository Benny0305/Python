from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
features=   [[150, 1], [120, 0], [140, 1], [170, 1], [110, 0],[100, 0]]
labels=     [1, 1, 1, 1, 0, 0]

clf = DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[114, 0],[150, 1],[145, 0],[130, 0]]))