import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators.MLE import MaximumLikelihoodEstimator
from pgmpy.inference.ExactInference import VariableElimination

def predict(data_train: pd.DataFrame, data_test: pd.DataFrame) -> np.array:
    ######################################################
    # TODO: create a Bayesian network, learn the parameters and return the probabilities
    #       of the 'illness_yes' variable-value pair for the test data.
    # ...
    ######################################################

    model = BayesianNetwork([
      ('asia', 'tub'),   
      ('smoke', 'bronc'), 
      ('smoke', 'lung'), 
      ('tub', 'illness'),    
      ('lung', 'illness'),   
      ('illness', 'xray'), 
      ('illness', 'dysp'),
      ('bronc', 'dysp'), 
    ])

    model.fit(data_train, estimator=MaximumLikelihoodEstimator)

    inference = VariableElimination(model)

    list_evidence_set = data_test.to_dict(orient="records");

    probabilities_illness_yes = []
    
    for evidence_set in list_evidence_set:  
        query_result = inference.query(
            variables=['illness'], 
            evidence=evidence_set
        )
        probabilities_illness_yes.append(query_result.values[1])

    return np.array(probabilities_illness_yes)