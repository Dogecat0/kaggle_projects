## **Kaggle dataset: Airline Passenger Satisfaction**
### What factors lead to customer satisfaction for an Airline?
https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

---

License: refer to https://www.kaggle.com/datasets/johndddddd/customer-satisfaction

---

Exploratory data analysis and model building for prediction of future customers satisfaction:
<br><br>
- **Exploratory data analysis**:
  1. Customer types and classes
  2. Customer age and type of travel
  3. Satisfaction analysis:
     
    - Customer age and satisfaction
    - Class, flight distance and satisfaction
  <br><br>
- **Model building**:
  1. Encode the categorical variables
  2. Check correlation map
  3. Build the models and gridsearch for best parameters :
    - Logistic regression
    - K neighbors classifier
    - Decision tree classifier
  4. Result :
  <br><br>
    - **Logistic Regression**: 
    <br><br>
    Best parameters: 
    <br>*--C: 10,*<br>*--penalty: 'l1'*, <br>*--solver: 'saga'*<br>
    Accuracy: 87%
    <br>
    F1 Score: 85%
    
   <br><br>
    - **K Neighbors classifier**: 
    <br><br>
    Best parameters: <br>*--metric: 'minkowski'*, <br>*--n_neighbors: 8,*<br>*--p: 1*,<br> *--weights: 'distance'*
    <br>
    Accuracy: 94%
    <br>
    F1 Score: 93%      

    <br><br>
    - **Decision Tree calssifier**:
    <br><br>
    Best parameters:<br>*--criterion: 'gini',*<br> *--max_depth: 9,*<br>*--max_features: 'log2',*<br>*--min_samples_split': 9*
    <br>
    Accuracy: 91%
    <br>
    F1 Score: 90%           