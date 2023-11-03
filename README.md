# Predicting employee attrition and retention strategies
The goal of this project is to provide the HR department with the information on a likelihood of an **employee attrition** (quitting the organization) using predictions driven by a machine learning classification algorithms.
Such a decission might be dictated by a multitude of factors: professional as well as personal.

Upon assessing the information (prediction) a company can settle on a **cost-optimal retention strategy** and initiate it in order to prevent desired employees from attrition.

## Data Set

[HR Analytics Dataset](https://www.kaggle.com/datasets/saadharoon27/hr-analytics-dataset/data)\
**Structured:** Yes\
**Format:** single .csv file\
**Size:** 1480 observations (unique: 1470)\
**Number of Features:** 38\
**Target Feature (Vector)**: `Attrition`, imbalanced, 16.1:83.9\
**NA Values**: 57 / 1480, all in one Feature (`YearsWithCurrManager`)\
**Duplicates**: 7 (All Features) + 3 (`EmployeeNumber` / `EmpID`)

## Problem Space

- typical binary classification problem
- relatively small amount of observations in the data set for ML Model training
- imbalanced target classes distribution
- developing a robust model, where solution model's performance metrics are independent from the `random_state` (data split as well as models)
- finding a good performance metric applicable to the project's goal (custom scoring - f2 (f-beta with beta=2)
  - more weight on **recall** (optimizing **False Negative** results - indicating the employees willing to quit) than on **precision** (optimizing **False Positive** results - misclassifying the ones who are willing to stay as wanting to leave)
- lack of aim set

## Process

### 1. Conventions
Conventions are discussed and agreed on: coding convention (programming style), variable names, random parameters (`random_state` for data splits and models), internal JupyterLab notebooks' structure, Git's repository folder structure.\
Early establishment of project's conventions is crucial, since:
- allows for unbiased models performance's metrics comparison
- increases code / JupyterLab's notebooks readability 
- in the later project's phases: prevents time overhead required for cleanups (code, repository)

### 2. Exploratory Data Analysis
In order to prevent bias in analytics - each team-member proceeds with EDA independently. The results are then exchanged and compared to include potentially missed-, as well as valuable-, insights.

### 3. Models
Distributed throughout team-members. Each one develops chosen base classification algorithms: Support Vector Machines (SVC) | Logistic Regression | K-Nearest Neighbors | Decision Tree / Random Forest.\
Additional models / methods are taken into consideration (Artificial Neural Networks, XGBoost, Adaboost, Gradient Boost, VotingClassifier), but will be developed as a bonus - only upon main models being properly developed and fine-tuned.\
From the additional models pool the project only accompanied for **XGBoost**.

### 4. Pipeline
Main pipeline is created by one team-member while other models are following its JupyterNotebook structure.

### 5. Hyperparameters Fine-Tuning
Model-specific search spaces are defined and fed into GridSearches. Performance Metrics between the models are compared and discussed. Potential improvements and model-specific issues are brainstormed.

### 6. Model's Interpretation
Feature importance are interpreted by utilizing model-specific methods (feature importance, permutation feat. importance, decision tree visualization)

### 7. Feature Engineering
Taking into consideration learnings from models' interpretation - new features are being brainstormed. Main pipeline is readjusted to acompany for feature engineering function.

## Models' Performance Metrics

|  | Support Vector Machine | K-Nearest Neighbors | Decision Tree | Logistic Regression | Random Forest | XGBoost |
| :--- | --- | --- | --- | --- | --- | --- |
| **F2 Score** | 64.52 % | 32.61 % | 53.36 % | 72.44 % | 60.50 % | 62.16 % |
| **Recall** | 76.60 % | 31.91 % | 57.45 % | 87.23 % | 72.34 % | 48.94 % |
| **Precision** | 39.56 % | 35.71 % | 41.54 % | 43.16 % | 36.56 % | 85.19 % |

## Choosing the best model

The best-performing model is **the Logistic Regression**. It's tuned toward the **F2 score**, with more weight on the recall, what shows in the model's performance metrics.\
Additional advantages of the chosen model:

- fast to compute
- getting prediction probabilities for the target classes allowing deeper analysis and potential decision threshold shift
- straightforward intepretation allowing for further development

## Model Interpretation

### Feature Importance
![Feature Importance](/Images/feature_importance.png)
According to the classification model, and as per feature importance - the biggest impact on employee's attrition have following factors:

- if an employee is doing **`overtime`**
- what is the **`marital status`** of the employee
- their level of **`job involvement`**
- the amount of **`years they are professionally active`**
- what is their **`role within the organization`**
- if they do **`business travel`** or not
- what is their **`level of job satisfaction`**

### Retention Strategies

Should address the observations listed in the Feature Importance point, prioritizing from top to bottom.\
Obviously we cannot have a direct influence on some of the employee's attributes, like for instance: **`marital status`**, **`years they are professionally active`**.

Couple of suggestions:

- **`Overtime`**: lower whenever possible, if not: be transparent regarding the reasons of overtime, delegate some of the ownership to the employees. Potentially the problem could also be planning-related and have its source in the Production Dept. It would be worth to assess the situation further and potentially train the Production Dept. in order to increase their planning precission.
- **`Marital Status`**: it's difficult to be addressed because it's not work-related
- **`Job Involvement`** and **`Level of Job Satisfaction`**: keywords here would be: motivate and delegate ownership (appointing chapions of specific production cycles or features)
- **`Business Travel`**: investigate and limit whenever possible, but inspect further if it's not correlated with employee's **`marital status`**
- **`Role within the organization`**:
<p align="center">
<img src="/Images/attrition_JobRole.png" />
</p>

As per above chart we can observe that we have higher than average `Attrition` in the roles: Human Resources, Laboratory Technician, Sale Representative. We would recommend further assessment of those departments and coming up with specific retention strategies per roles / dept.

## Project's highlights
- shared files for functions and global settings allowing for streamlined editing of global parameters (i.e. `random_state`), as well as uniform / consistent visualization's style throught Jupyter Notebooks
- main pipeline with external model-definitions .py file allowing for streamlined model switching and comparison
- advanced confussion matrix with meaningful color-coding with custom color maps additionally accompanying for color-blindness
- bulk-generation of data visualizations streamlining the process of EDA 

## Repository description
- how to install
- files description

## Disclaimer
This project was done in the period of 2 weeks as a follow-up to the [StackFuel GmbH](https://stackfuel.com/en/) courses: Data Analytics Certification and Data Science Certification.

### Team Members
Christian Roden: [GitHub](https://github.com/christianroden)\
Rafal Fedro: [GitHub](https://github.com/RafalFedro)\
Nino Olujic: [GitHub](https://github.com/Niprogram)\
Nigar Hessler: [GitHub](https://github.com/Nigar-Hessler)

### Data Set: HR Analytics Dataset
Obtained from: [kaggle.com](https://www.kaggle.com/datasets/saadharoon27/hr-analytics-dataset/data)\
License: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
