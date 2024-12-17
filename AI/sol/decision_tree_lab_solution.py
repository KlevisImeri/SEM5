from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier

def predict(X_train, y_train, X_test):
    categorical_cols = ['manufacturer', 'model'] 

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), categorical_cols),
            ('num', 'passthrough', X_train.columns.difference(categorical_cols))  
        ]
    )

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),  
        ('classifier', DecisionTreeClassifier(random_state=42))  
    ])


    pipeline.fit(X_train, y_train)

    return pipeline.predict(X_test)
