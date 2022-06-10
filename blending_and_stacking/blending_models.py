# Importing the necessary libraries
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
    x_train, y_train, test_size=0.25, random_state=0)

model_SVC.fit(x_blend, y_blend)
model_RF.fit(x_blend, y_blend)
model_KNN.fit(x_blend, y_blend)

proba = np.stack([model_SVC.predict_proba(x_holdout)[:, 1],
                  model_RF.predict_proba(x_holdout)[:, 1],
                  model_KNN.predict_proba(x_holdout)[:, 1]]).T


scaler = StandardScaler()
proba = scaler.fit_transform(proba)

# Linear blending KNN since the meta learner is LogisticRegression which is a linear algorithm
blender = LogisticRegression(solver='liblinear')
blender.fit(proba, y_holdout)

print(blender.coef_)

test_proba = np.stack([model_SVC.predict_proba(x_test)[:, 1],
                       model_RF.predict_proba(x_test)[:, 1],
                       model_KNN.predict_proba(x_test)[:, 1]]).T

blending = blender.predict_proba(test_proba)[:, 1]
ras = roc_auc_score(y_true=y_test, y_score=blending)
print(f"ROC-AUC for linear blending KNN is: {ras:0.5f}")

# Non linear blending KNN since the meta learner this time is RF, which is a non linear algorithm
blender = RandomForestClassifier()
blender.fit(proba, y_holdout)

test_proba = np.stack([model_SVC.predict_proba(x_test)[:, 1],
                       model_RF.predict_proba(x_test)[:, 1],
                       model_KNN.predict_proba(x_test)[:, 1]]).T

blending = blender.predict_proba(test_proba)[:, 1]
ras = roc_auc_score(y_true=y_test, y_score=blending)
print(f"ROC-AUC for non-linear blending KNN is: {ras:0.5f}")
