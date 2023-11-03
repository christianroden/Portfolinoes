# Predicting employee attrition and retention strategies
The goal of this project is to provide the HR department with information on a likelihood of an employee attrition (quitting the current job) using prediction driven by a machine learning classification algorithms.
Such a decission might be dictated by a multitude of factors, professional as well as personal.
Upon assessing the information (prediction) a company can settle on a cost-optimal retention strategy and initiate it in order to prevent desired employees from attrition.

## Data Set

[HR Analytics Dataset](https://www.kaggle.com/datasets/saadharoon27/hr-analytics-dataset/data)\
**Structured:** Yes\
**Format:** single .csv file\
**Size:** 1480 observations (unique: 1470)\
**Number of Features:** 38\
**Target Feature (Vector)**: Attrition, imbalanced, 16.1:83.9\
**NA Values**: 57 / 1480, all in one Feature (YearsWithCurrManager)\
**Duplicates**: 7 (All Features) + 3 (EmployeeNumber / EmpID)

## Challenges

- typical binary classification problem
- relatively small amount of observations in the data set for ML Model training
- imbalanced target classes distribution
- finding a good performance metric applicable to scenario's goal (custom scoring - f2)
  - more weight on **recall** (optimizing **False Negative** results - indicating the employees willing to quit) than on **precision** (optimizing **False Positive** results - misclassifying the ones who are willing to stay as wanting to leave)

## Process
- EDA
- models
- pipeline
- hyperparameters fine-tuning

## Models' Performance Metrics

|  | Support Vector Machine | K-Nearest Neighbors | Decision Tree | Logistic Regression | Random Forest | XGBoost |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **F2 Score** | 64.52 % | 32.61 % | 53.36 % | 72.44 % | 60.50 % | 62.16 % |
| **Recall** | 76.60 % | 31.91 % | 57.45 % | 87.23 % | 72.34 % | 48.94 % |
| **Precision** | 39.56 % | 35.71 % | 41.54 % | 43.16 % | 36.56 % | 85.19 % |

## Interpretation
- feature importance
- retention strategies

## Project's highlights

## Additional remarks
- sync and transparency (agile)
- common repository
- keeping naming conventions
- centralized shared files for functions and global settings definitions
- presentation software
- communication platform

## Repository description

## Disclaimer
This project was done in the period of 2 weeks as a follow-up to the StackFuel GmbH courses: Data Analytics and Data Science Certified Courses.

### Team Members
Christian Roden: [GitHub](https://github.com/christianroden)\
Rafal Fedro: [GitHub](https://github.com/RafalFedro)\
Nino Olujic: [GitHub](https://github.com/Niprogram)\
Nigar Hessler: [GitHub](https://github.com/Nigar-Hessler)

### Data Set: HR Analytics Dataset
Obtained from: [kaggle.com](https://www.kaggle.com/datasets/saadharoon27/hr-analytics-dataset/data)\
License: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
