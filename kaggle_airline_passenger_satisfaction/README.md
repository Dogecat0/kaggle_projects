# **Kaggle dataset: Airline Passenger Satisfaction**

What factors lead to customer satisfaction for an Airline?

License: Other (specified in description)

[Kaggle Dataset](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

---

## **Exploratory data analysis and model building for prediction of future customers satisfaction**

### **Exploratory data analysis**

<ol type="1">
  <li>Customer types and classes</li>
  <li>Customer age and type of travel</li>
  <li>Satisfaction analysis</li>
  <ol type="a">
      <li>Customer age and satisfaction</li>
      <li>Class, flight distance and satisfaction</li>
  </ol>
</ol>

### **Model building**

<ol type="1">
  <li>Encode the categorical variables</li>
  <li>Check correlation map</li>
  <li>Build the models and gridsearch for best parameters</li>
  <ol type="a">
      <li>Logistic Regression</li>
      <li>K Neighbors Classifier</li>
      <li>Decision Tree classifier</li>
      <li>Random Forest classifier</li>
      <li>XGBoosting classifier</li>
  </ol>
  <li>Result (<em>higher scores without feature selection have been chosen to show here</em>)</li>
  <ol type="a">
    <li>Logistic Regression</li>
    <table>
      <tr>
        <th>Best Parameters</th>
        <th>Accuracy</th>
        <th>F1 Score</th>
      </tr>
      <tr>
        <td>
          <ul>
            <li><strong>C</strong>: 10</li>
            <li><strong>penalty</strong>: l1</li>
            <li><strong>solver</strong>: saga</li>
          </ul>
        </td>
        <td>87.1%</td>
        <td>85.0%</td>
      </tr>
    </table>
    <li>K Neighbors Classifier</li>
    <table>
      <tr>
        <th>Best Parameters</th>
        <th>Accuracy</th>
        <th>F1 Score</th>
      </tr>
      <tr>
        <td>
          <ul>
            <li><strong>metric</strong>: minkowski</li>
            <li><strong>n_neighbors</strong>: 8</li>
            <li><strong>p</strong>: 1</li>
            <li><strong>weights</strong>: distance</li>
          </ul>
        </td>
        <td>93.8%</td>
        <td>92.8%</td>
      </tr>
    </table>
    <li>Decision Tree Classifier</li>
    <table>
      <tr>
        <th>Best Parameters</th>
        <th>Accuracy</th>
        <th>F1 Score</th>
      </tr>
      <tr>
        <td>
          <ul>
            <li><strong>criterion</strong>: gini</li>
            <li><strong>max_depth</strong>: 9</li>
            <li><strong>max_features</strong>: log2</li>
            <li><strong>min_samples_split</strong>: 9</li>
          </ul>
        </td>
        <td>91.0%</td>
        <td>89.8%</td>
      </tr>
    </table>
    <li>Random Forest Classifier</li>
    <table>
      <tr>
        <th>Best Parameters</th>
        <th>Accuracy</th>
        <th>F1 Score</th>
      </tr>
      <tr>
        <td>
          <ul>
            <li><strong>criterion</strong>: entropy</li>
            <li><strong>max_features</strong>: log2</li>
            <li><strong>n_estimators</strong>: 1000</li>
          </ul>
        </td>
        <td>96.4%</td>
        <td>95.8%</td>
      </tr>
    </table>
    <li>Gradient Boosting Classifier</li>
    <table>
      <tr>
        <th>Best Parameters</th>
        <th>Accuracy</th>
        <th>F1 Score</th>
      </tr>
      <tr>
        <td>
          <ul>
            <li><strong>learning_rate</strong>: 0.1</li>
            <li><strong>max_features</strong>: log2</li>
            <li><strong>max_depth</strong>: 6</li>
            <li><strong>n_estimators</strong>: 500</li>
            <li><strong>sub_sample</strong>: 1</li>
          </ul>
        </td>
        <td>96.5%</td>
        <td>95.9%</td>
      </tr>
    </table>
  </ol>
</ol>