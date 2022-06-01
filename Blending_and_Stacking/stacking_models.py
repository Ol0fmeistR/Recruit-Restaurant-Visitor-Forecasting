# Importing the necessary libraries
from sklearn.model_selection import KFold
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from scipy.stats import mode
import numpy as np
from sklearn.metrics import log_loss, roc_auc_score, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generating some synthetic data for the template, replace with your actual dataset
x, y = make_classification(n_samples=10000, n_features=50,
                           n_informative=10,
                           n_redundant=25, n_repeated=15,
                           n_clusters_per_class=5,
                           flip_y=0.05, class_sep=0.5,
                           random_state=0)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=42)

# Loading SVC, KNN and RF for the template, change as per your requirements
model_SVC = SVC(probability=True, random_state=42)
model_RF = RandomForestClassifier(random_state=42)
model_KNN = KNeighborsClassifier()

# Fitting the models
model_SVC.fit(x_train, y_train)
model_RF.fit(x_train, y_train)
model_KNN.fit(x_train, y_train)

# Blending and stacking different models using a meta learner
# Metric used: ROC AUC
x_blend, x_holdout, y_blend, y_holdout = train_test_split(
    x_train, y_train, test_size=0.5, random_state=0)

model_SVC.fit(x_blend, y_blend)
model_RF.fit(x_blend, y_blend)
model_KNN.fit(x_blend, y_blend)

proba = np.stack([model_SVC.predict_proba(x_holdout)[:, 1],
                  model_RF.predict_proba(x_holdout)[:, 1],
                  model_KNN.predict_proba(x_holdout)[:, 1]]).T

# Adding models to the ensemble until scores don't improve anymore
iterations = 100

proba = np.stack([model_SVC.predict_proba(x_holdout)[:, 1],
                  model_RF.predict_proba(x_holdout)[:, 1],
                  model_KNN.predict_proba(x_holdout)[:, 1]]).T

baseline = 0.5
print(f"starting baseline is {baseline:0.5f}")

models = []

for i in range(iterations):
    challengers = list()
    for j in range(proba.shape[1]):
        new_proba = np.stack(proba[:, models + [j]])
        score = roc_auc_score(y_true=y_holdout,
                              y_score=np.mean(new_proba, axis=1))
        challengers.append([score, j])

    challengers = sorted(challengers, key=lambda x: x[0], reverse=True)
    best_score, best_model = challengers[0]
    if best_score > baseline:
        print(f"Adding model_{best_model+1} to the ensemble", end=': ')
        print(f"ROC-AUC increases score to {best_score:0.5f}")
        models.append(best_model)
        baseline = best_score
    else:
        print("Cannot improve further - Stopping")
        break

freqs = Counter(models)
weights = {key: freq/len(models) for key, freq in freqs.items()}
print(weights)

kf = KFold(n_splits=5, shuffle=True, random_state=0)
scores = list()

first_lvl_oof = np.zeros((len(x_train), 3))
fist_lvl_preds = np.zeros((len(x_test), 3))

for k, (train_index, val_index) in enumerate(kf.split(x_train)):
    model_SVC.fit(x_train[train_index, :], y_train[train_index])
    first_lvl_oof[val_index, 0] = model_SVC.predict_proba(x_train[val_index, :])[
        :, 1]

    model_RF.fit(x_train[train_index, :], y_train[train_index])
    first_lvl_oof[val_index, 1] = model_RF.predict_proba(x_train[val_index, :])[
        :, 1]

    model_KNN.fit(x_train[train_index, :], y_train[train_index])
    first_lvl_oof[val_index, 2] = model_KNN.predict_proba(x_train[val_index, :])[
        :, 1]

model_SVC.fit(x_train, y_train)
fist_lvl_preds[:, 0] = model_SVC.predict_proba(x_test)[:, 1]

model_RF.fit(x_train, y_train)
fist_lvl_preds[:, 1] = model_RF.predict_proba(x_test)[:, 1]

model_KNN.fit(x_train, y_train)
fist_lvl_preds[:, 2] = model_KNN.predict_proba(x_test)[:, 1]

second_lvl_oof = np.zeros((len(x_train), 3))
second_lvl_preds = np.zeros((len(x_test), 3))

for k, (train_index, val_index) in enumerate(kf.split(x_train)):
    skip_X_train = np.hstack([x_train, first_lvl_oof])
    model_SVC.fit(skip_X_train[train_index, :], y_train[train_index])
    second_lvl_oof[val_index, 0] = model_SVC.predict_proba(
        skip_X_train[val_index, :])[:, 1]

    model_RF.fit(skip_X_train[train_index, :], y_train[train_index])
    second_lvl_oof[val_index, 1] = model_RF.predict_proba(
        skip_X_train[val_index, :])[:, 1]

    model_KNN.fit(skip_X_train[train_index, :], y_train[train_index])
    second_lvl_oof[val_index, 2] = model_KNN.predict_proba(
        skip_X_train[val_index, :])[:, 1]

skip_X_test = np.hstack([x_test, fist_lvl_preds])

model_SVC.fit(skip_X_train, y_train)
second_lvl_preds[:, 0] = model_SVC.predict_proba(skip_X_test)[:, 1]

model_RF.fit(skip_X_train, y_train)
second_lvl_preds[:, 1] = model_RF.predict_proba(skip_X_test)[:, 1]

model_KNN.fit(skip_X_train, y_train)
second_lvl_preds[:, 2] = model_KNN.predict_proba(skip_X_test)[:, 1]

arithmetic = second_lvl_preds.mean(axis=1)
ras = roc_auc_score(y_true=y_test, y_score=arithmetic)
scores.append(ras)
print(f"Stacking ROC-AUC is: {ras:0.5f}")
