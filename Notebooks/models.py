from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from global_settings import *

model_settings = {
    'log': {'model': LogisticRegression(penalty='l2', 
                                        tol=0.01, 
                                        C=0.3, 
                                        #class_weight='balanced', 
                                        solver='saga', 
                                        max_iter=10000, 
                                        #l1_ratio=None, 
                                        random_state=random_seed),
            'params': {#'estimator__tol': [0.008, 0.01, 0.012, 0.014, 0.1, 1], 
                       #'estimator__C': [0.3, 0.31, 0.32, 0.33, 0.34, 0.35],
                       #'estimator__solver': ['lbfgs', 'saga']
                      }
           },
    'svc': {'model': SVC(C=1,
                         kernel='sigmoid',
                         #degree=3,
                         #gamma='auto',
                         class_weight='balanced',
                         cache_size=1000, 
                         probability=True, 
                         random_state=42),
            'params': {'estimator__C': [1],
                       'estimator__kernel': ['sigmoid'],
                       #'estimator__degree': [3],
                       #'estimator__gamma': ['auto'],
                       'estimator__class_weight': ['balanced']
                      }
           },
    'xgb': {'model': XGBClassifier(objective='binary:logistic', 
                                   n_estimators=150, 
                                   learning_rate=0.1, 
                                   max_depth=15, 
                                   min_child_weight=5, 
                                   subsample=0.8, 
                                   colsample_bytree=1.0, 
                                   gamma=0, 
                                   reg_alpha=0, 
                                   reg_lambda=0.2,
                                   random_state=42), 
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
    'rfc': {'model': RandomForestClassifier(n_estimators=60, 
                                            max_depth=10, 
                                            min_samples_split=2, 
                                            min_samples_leaf=8, 
                                            min_weight_fraction_leaf=0.0, 
                                            max_features='sqrt', 
                                            max_leaf_nodes=None, 
                                            min_impurity_decrease=0.0, 
                                            class_weight='balanced', 
                                            max_samples=None,
                                            verbose=0, 
                                            random_state=42),
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