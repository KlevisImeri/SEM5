%reset -f
import numpy as np
import pandas as pd

spambase_df = pd.read_csv("https://share.mit.bme.hu/index.php/s/wgc46gCHRb7bPdF/download/spambase.csv")

from sklearn.model_selection import train_test_split

X = spambase_df.drop("Class", axis=1).values
y = spambase_df["Class"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=42)

from sklearn.model_selection import train_test_split

X = spambase_df.drop("Class", axis=1).values
y = spambase_df["Class"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=42)

from sklearn.metrics import accuracy_score

y_pred = predict(X_train, y_train, X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Ensemble Classifier Accuracy: {accuracy:.3f}")