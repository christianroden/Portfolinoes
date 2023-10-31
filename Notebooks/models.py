from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier

model_settings = {
    'svc': {'model': SVC(cache_size=1000, probability=True, random_state=42),
            'params': {'estimator__C': [1],
                       'estimator__kernel': ['sigmoid'],
                       #'estimator__degree': [3],
                       #'estimator__gamma': ['auto'],
                       'estimator__class_weight': ['balanced']
                      }
           },
    'xgb': {'model': XGBClassifier(objective='binary:logistic', random_state=42), 
            'params': {'estimator__n_estimators': [150], 
                       'estimator__learning_rate': [0.1], 
                       'estimator__max_depth': [15], 
                       'estimator__min_child_weight': [5], 
                       'estimator__subsample': [0.8], 
                       'estimator__colsample_bytree': [1.0], 
                       'estimator__gamma': [0], 
                       'estimator__reg_alpha': [0], 
                       'estimator__reg_lambda': [0.2]
                      }
           },
    'rfc': {'model': RandomForestClassifier(verbose=0, random_state=42),
            'params': {'estimator__n_estimators': [60], 
                       'estimator__max_depth': [10], 
                       #'estimator__min_samples_split': [2], 
                       'estimator__min_samples_leaf': [8], 
                       #'estimator__min_weight_fraction_leaf': [0.0], 
                       #'estimator__max_features': ['sqrt'], 
                       #'estimator__max_leaf_nodes': [None], 
                       #'estimator__min_impurity_decrease': [0.0], 
                       'estimator__class_weight': ['balanced'], 
                       'estimator__max_samples': [None]
                      }
           }
}
    
accessible_models = model_settings.keys()