# Importing the necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_auc_score

# Load your datasets
train = pd.read_csv("../input/pathname/train.csv")
test = pd.read_csv("../input/pathname/test.csv")

train = train.fillna(-1).drop(["id", "target"], axis=1)
test = test.fillna(-1).drop(["id"], axis=1)

x = train.append(test)
y = [0] * len(train) + [1] * len(test)

model = RandomForestClassifier()
cv_preds = cross_val_predict(
    model, x, y, cv=5, n_jobs=-1, method='predict_proba')

print(roc_auc_score(y_true=y, y_score=cv_preds[:, 1]))

print(np.sum(cv_preds[:len(x), 1] > 0.5))

model.fit(x, y)

ranks = sorted(list(zip(x.columns, model.feature_importances_)),
               key=lambda x: x[1], reverse=True)

for feature, score in ranks:
    print(f"{feature:10} : {score:0.4f}")
