from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

def predict(X_train, y_train, X_test):

    ensemble_model = AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=3),  
        n_estimators=50,
        learning_rate=1.0, 
        random_state=42,
        algorithm="SAMME"
    )
    

    ensemble_model.fit(X_train, y_train)
    return ensemble_model.predict(X_test)