## 1.1. The Prediction Problem

## Research Question Formulation:

### Objective:
Correlation between Economic Factors and Energy Access

### RQ1: 
How do economic factors such as GDP per capita correlate with energy access disparities across different regions?
#### Significance:  
Energy access is related to economic development, and understanding the correlation with economic factors is essential for formulating targeted interventions. Thus, examining the relationship between GDPs per capita with energy access disparities helps policymakers and researchers identify key drivers of inequality. This knowledge can inform policy decisions, focusing on inclusive economic growth and urban planning that considers energy access as an integral component.

### Objective 2: 
The objective of this second model is to identify and understand the key factors that contribute to the classification of countries into high, medium, and low energy efficiency levels.

### RQ2: 
What factors contribute to the classification of countries into high, medium, and low energy efficiency levels, and can these factors be used to predict a country's energy efficiency?
#### Significance:  
The primary aim is to develop a predictive model that leverages these factors to forecast a country's energy efficiency classification accurately. Look at Figure 1 for a detailed flowchart of this workflow, providing an overview of the task.

## Operational Measures:

### Variables:

- **Dependent Variable (Y):** 
  Total energy consumption in each region per person (`energy_per_capita`).
  
- **Independent Variables (X):** 
  Economic factors, such as GDP per capita (`gdp_per_capita`).
  
- **Data Type:** 
  The dataset is a cross-sectional dataset that captures information for multiple countries or regions.

### Variables 2:

- **Dependent Variable (Y):** 
  Energy efficiency level (Categorical). High, Medium, Low (This variable is created)
  
- **Independent Variables (X) (Features):** 
  - Renewable energy percentage/share (`renewables_share_elec`): Percentage of total energy derived from renewable sources.
  - Energy intensity (`energy_per_gdp`): Energy consumption per unit of GDP, indicating the efficiency of energy use in the economy.
  
#### Hypothesis Development:

**Prediction Hypothesis:** 
Regions with higher GDP per capita will tend to have better energy access, while those with lower economic indicators may face greater energy access disparities.

- **Justification:** 
This hypothesis is grounded in the idea that economic development, as indicated by higher GDP per capita tends to be associated with improved infrastructure and energy access. Wealthier and more developed regions may have the resources to invest in energy infrastructure, reducing disparities in access.

**Machine Learning Algorithm Selection:** 
The goal is to predict or understand relationships between variables, a linear regression model would be appropriate. 

- **Justification:** 
Regression models provide interpretability to understand the impact of each independent variable on the dependent variable. Given that the relationships between variables may not be highly complex, linear regression or decision trees are appropriate. Regression models can provide insights into the direction and strength of relationships, helping to answer the research questions effectively. Thus, the algorithms chosen are linear regression and random forest.

**Prediction Hypothesis 2:** 
The combination of renewable energy share (`renewables_share_elec`) and energy intensity (`energy_per_gdp`) can predict the classification of countries into high, medium, and low energy efficiency levels. Specifically, countries with a higher percentage of renewable energy and lower energy intensity are expected to be classified as having high energy efficiency.

- **Justification:** 
    - Renewable Energy Percentage (X1): Countries with a higher percentage of energy derived from renewable sources are likely to have cleaner and more sustainable energy profiles, contributing positively to their energy efficiency levels. Renewable energy sources are inherently more environmentally friendly and align with global sustainability goals.
    - Energy Intensity (X2): Energy intensity, representing the amount of energy consumed per unit of GDP, is a key indicator of energy efficiency. Lower energy intensity implies that a country can achieve economic output with less energy consumption, reflecting a more efficient use of energy resources.
    - Energy Efficiency Level (Y): The classification into high, medium, and low energy efficiency levels provides a meaningful and actionable categorization. It allows for a practical understanding of a country's energy performance and can guide targeted interventions to improve efficiency.

**Machine Learning Algorithm Selection 2:** 
Using a random forest classifier to test the hypothesis.

- **Justification:** 
Categorical model. Random Forests are capable of capturing complex, non-linear relationships between input features and the target variable. Since the relationship between renewable energy percentage, energy intensity, and energy efficiency levels may not be linear, a Random Forest is well-suited for this task. Random Forests offer a built-in feature importance analysis, allowing us to understand the contribution of each variable to the classification. This aligns with the goal of identifying key factors influencing energy efficiency levels.


## 1.2. The Machine Learning Workflow

## Model Development:

The following workflow was the same for both regression and classification models, for details on how they differed, visit my GitHub repository for the detailed code on both models.

### Data Processing:

- Observe the relevant columns to the prediction problem, specifically, the country column.
- Exclude those that are not a country, remove all regions by creating a boolean mask for rows that don't contain any of the exclusion patterns.
- Group data by country, getting the average of the other variables.
- Address any missing values by removing those variables, considering the impact on the variables of interest.
- **For regression model:** Create a new variable (X variable) GDP per capita using GDP and population variables.
- **For the classification model:** Create the dependent variable based on the previously defined criteria.

### Results Presentation:

- **Training and Testing:** Split the dataset into training and testing sets. A common split might be 80% for training and 20% for testing. Using sklearn train_test_split.
- **Data Visualization:** 
  - **Regression model:** Histogram plot for the true values (`y_test`) and predicted values (`y_pred`).
  - **Classification model:** A heatmap of the confusion matrix will be used to showcase the model's performance in classifying countries into high, medium, and low energy efficiency levels. A bar chart or plot will be generated to illustrate the relative importance of the input features (renewable energy percentage and energy intensity) in making classification decisions.

### Model Evaluation:

- **Evaluation Criteria:** 
  - **Regression model:** Use metrics such as Mean Squared Error (MSE) and R-squared to evaluate the accuracy of predictions.
  - **Classification model:** Use metrics such as accuracy for the overall correctness of the model's predictions. Precision, recall, and f1-score will be used to evaluate the model's performance for each class (high, medium, low) individually. A detailed confusion matrix will provide insights into false positives, false negatives, true positives, and true negatives. An analysis of the features selected to understand the contribution of each feature to the model's decisions.
- **Iterative Improvement:** 
  - **Hyperparameter Tuning:** Adjust model hyperparameters to find the optimal configuration using techniques like grid search or random search.
  - **Feature Selection:** Reassess feature importance and consider removing irrelevant or highly correlated features.
  - **Model Complexity:** Evaluate if the model is overfitting or underfitting and adjust complexity accordingly.
  - **Include Additional Features:** If new relevant data becomes available, incorporate it to improve model accuracy, also to increase the data to train and test the model with.

## References:

- Aydın, Celil, and Ömer Esen. 2018. “Does the Level of Energy Intensity Matter in the Effect of Energy Consumption on the Growth of Transition Economies? Evidence from Dynamic Panel Threshold Analysis.” Energy Economics 69 (January): 185–95. [https://doi.org/10.1016/j.eneco.2017.11.010](https://doi.org/10.1016/j.eneco.2017.11.010).

- “Measurements of Energy Access: A Better Way? - Energy for Growth Hub.” 2023. Energy for Growth Hub. June 12, 2023. [https://energyforgrowth.org/article/measurements-of-energy-access-a-better-way/](https://energyforgrowth.org/article/measurements-of-energy-access-a-better-way/).

- Zabat, Lotfi Hocine, Naima Akli Sadaoui, Abid Mehdi, and Habib Sekrafi. 2022. “Threshold Effects of Renewable Energy Consumption by Source in U.S. Economy.” Electric Power Systems Research 213 (December): 108669. [https://doi.org/10.1016/j.epsr.2022.108669](https://doi.org/10.1016/j.epsr.2022.108669).

