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

# Taking the majority vote out of all 3 models
# Metric used: Accuracy
preds = np.stack([model_SVC.predict(x_test),
                  model_RF.predict(x_test),
                  model_KNN.predict(x_test)]).T
max_voting = np.apply_along_axis(mode, 1, preds)[:, 0]

# Individual accuracies of the 3 different models
for i, model in enumerate(['SVC', 'RF ', 'KNN']):
    acc = accuracy_score(y_true=y_test, y_pred=preds[:, i])
    print(f"Accuracy for {model} model is: {acc:0.3f}")

# Check accuracy of majority voting
max_voting_accuray = accuracy_score(y_true=y_test, y_pred=max_voting)
print(f"Accuracy for majority voting is: {max_voting_accuray:0.3f}")
