from sklearn.tree import BaseDecisionTree
from sklearn.tree import DecisionTreeClassifier

class BasicTree(BaseDecisionTree):
    def __init__(self, model=DecisionTreeClassifier()):
        self.model = model

    def fit(self, X, y=None, **kwargs):
        self.model.fit(X, y)
        return self

    def predict(self, X, y=None):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def score(self, X, y):
        return self.model.score(X, y)
