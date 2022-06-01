# Importing the necessary libraries
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

# Taking the weighted average of 3 different models
# Metric used: ROC AUC
proba = np.stack([model_SVC.predict_proba(x_test)[:, 1],
                  model_RF.predict_proba(x_test)[:, 1],
                  model_KNN.predict_proba(x_test)[:, 1]]).T

for i, model in enumerate(['SVC', 'RF ', 'KNN']):
    ras = roc_auc_score(y_true=y_test, y_score=proba[:, i])
    print(f"ROC-AUC for {model} model is: {ras:0.5f}")

# Using arithmetic mean of all 3 models
arithmetic = proba.mean(axis=1)
ras = roc_auc_score(y_true=y_test, y_score=arithmetic)
print(f"Mean averaging ROC-AUC is: {ras:0.5f}")

# Using geometric mean of all 3 models
geometric = proba.prod(axis=1)**(1/3)
ras = roc_auc_score(y_true=y_test, y_score=geometric)
print(f"Geometric averaging ROC-AUC is: {ras:0.5f}")

# Using harmonic mean of all 3 models
harmonic = 1 / np.mean(1. / (proba + 0.00001), axis=1)
ras = roc_auc_score(y_true=y_test, y_score=harmonic)
print(f"Harmonic averaging ROC-AUC is: {ras:0.5f}")

# Using logarithmic averaging of all 3 models
logarithmic = np.expm1(np.mean(np.log1p(proba), axis=1))
ras = roc_auc_score(y_true=y_test, y_score=logarithmic)
print(f"Logarithmic averaging ROC-AUC is: {ras:0.5f}")
