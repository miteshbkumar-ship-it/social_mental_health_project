**Project Goal**  
The main goal of this project is to explore the connection between social media use and mental health indicators. We want to understand how digital habits, such as screen time, choice of platforms, and time spent offline, along with lifestyle factors like sleep, exercise, stress and happiness affects overall well-being. We aim to identify trends and point out factors that could help people improve or maintain better mental wellness.

**Motivation**  
Social media plays a vital role in our daily lives, especially for students. We all use social platforms and know about their positive and negative impacts. This made the dataset both relatable and relevant for analysis. Our goal is to explore these effects more deeply and possibly help promote healthier well-being in the digital age.

**Target Audience**  
The findings from this project can help several groups:

1. **Social media companies:** These companies can learn how their platforms may affect users' mental health. This could lead them to consider features or changes that encourage healthier use.  
2. **Students and general social media users:** By raising awareness about how habits, screen time, and platform choices influence well-being. This can help users make better decisions.  
3. **Well-being educators**: The insights can aid in guidance, awareness campaigns or interventions that promote healthier online behaviors.

Overall, this project can help individuals make better choices about their social media use and understand how their lifestyle habits may impact their mental state.

**About dataset**  
Using a dataset from Kaggle's **social media and mental health dataset**. This dataset examines how digital habits link to mental well-being. It includes information on daily screen time, preferred social media platforms, sleep quality, happiness levels, stress scores, exercise frequency and days without social media. These variables give us a broad view of how different lifestyle choices and digital behaviours may influence overall mental wellness. Throughout this analysis, we hope to answer the following questions:

* **Question 1:** To what extent is the number of days without social media related to an individual's overall well-being score?  
* **Question 2:** What is the typical Age and Gender profile for users of different Social media platforms and how does their average daily screen time compare?  
* **Question 3:** What are the most significant predictors of a user's stress level, and can a model accurately predict whether a user falls into the high or low stress categories based on lifestyle factors?

**Research Questions and Methodology**

**Question 1\.**  
To what extent is the number of days without social media related to an individual's overall well-being score?

**Hypothesis**  
Individuals who spend fewer days without social media will show a lower happiness index.

**Relevant Variables**

* Days\_Without\_Social\_Media (numerical)  
* Wellbeing\_Score (numerical)  
* Happiness\_Index  
* Sleep\_Quality  
* Stress\_Level  
* Exercise\_Frequency

**Analysis Approach**  
We will start by looking at the factors that make up the well-being score. This will include factors such as happiness score, sleep quality, exercise frequency and stress level. We will combine the total scores for Sleep Quality, Exercise Frequency, and Happiness Index, then subtract the inverse of the Stress Level (e.g., 11 \- Stress Level) to get the final overall Wellbeing Score. We will then analyse whether there is a direct correlation and a linear relationship between the calculated Wellbeing Score and Days Without Social Media.

**Question 2\.**  
What is the typical Age and Gender profile for users of different social media platforms and how does their average daily screen time compare?

**Hypothesis**  
Age and gender will significantly influence which social media platforms people use.

**Relevant Variables**

* Age (numerical)  
* Gender (categorical)  
* Social\_Media\_Platform (categorical)  
* Daily\_Screen\_Time(hrs) (numerical)

**Analysis Approach**  
We will begin by selecting the key variables (Age, Gender, Social Media Platform, and Daily Screen Time) and grouping users by platform. For each platform, we will examine the age and gender distributions to understand the typical user profile. We will then compare average daily screen time across platforms to see whether particular groups (e.g., younger users or specific genders) spend more time online.  
To visualise these patterns clearly, we will use bar charts and box plots to show differences across platforms in age, gender, and screen-time behaviour.

**Question 3\.**  
What are the most significant predictors of a user's stress level, and can a model accurately predict whether a user falls into the high or low stress categories based on lifestyle factors?

**Hypothesis**  
Higher daily screen time will be associated with higher stress levels.

**Relevant Variables**

* Stress\_Level (numerical → converted into a binary category)  
* 0 \= low Stress (1-5)  
* 1 \= high Stress (6-10)

**Analysis Approach**  
We will start by converting the continuous Stress Level column into two distinct binary categories: High Stress (6-10) and Low Stress (1-5). To identify the most significant predictors, we can use a correlation heatmap to visually assess the linear relationships between stress and other numerical factors (such as Screen Time, Sleep Quality, and Exercise Frequency).  
We will then build a classification model that uses the identified lifestyle factors as inputs (predictors). The model will be trained to predict which of the two categories ("High" or "Low" Stress) a user belongs to.

**Results and Findings (will work from here just an idea of the layout)**

**Question 1 Results:**

1.1 Wellbeing Score Construction

* How the Wellbeing Score was calculated  
* Mean, median, and range of the Wellbeing Score  
* Distribution characteristics (normal, skewed, etc.)

1.2 Correlation Analysis

* Correlation coefficient between Days\_Without\_Social\_Media and Wellbeing\_Score  
* Statistical significance (p-value)  
* Strength and direction of the relationship

1.3 Component Variable Analysis

* Relationship between Days\_Without\_Social\_Media and Happiness\_Index  
* Relationship between Days\_Without\_Social\_Media and Sleep\_Quality  
* Relationship between Days\_Without\_Social\_Media and Stress\_Level  
* Relationship between Days\_Without\_Social\_Media and Exercise\_Frequency

1.4 Key Findings

* Main discovery about social media breaks and wellbeing  
* Notable patterns or trends observed  
* Hypothesis validation (supported/not supported)  
* Secondary insights

---

**Question 2 Results:** 

2.1 Age Distribution by Platform

* Age range and average age for each platform  
* Platform with youngest/oldest average user age  
* Age trends across platforms

2.2 Gender Distribution by Platform

* Gender breakdown for each platform  
* Platforms with notable gender imbalances  
* Overall gender patterns

2.3 Screen Time by Platform

* Average daily screen time for each platform  
* Platform with highest/lowest screen time  
* Screen time variation across platforms

2.4 Screen Time by Demographics

* Average screen time by age group  
* Average screen time by gender  
* Notable differences between demographic groups

2.5 Key Findings

* Typical user profile for each major platform  
* Main patterns linking demographics to platform choice  
* Screen time insights across user groups  
* Hypothesis validation (supported/not supported)  
* Unexpected discoveries

---

**Question 3 Results:** 

3.1 Stress Category Distribution

* Number and percentage of users in Low Stress (1-5)  
* Number and percentage of users in High Stress (6-10)  
* Overall balance of the dataset

3.2 Predictor Correlation Analysis

* Correlation between Daily\_Screen\_Time and Stress\_Level  
* Correlation between Sleep\_Quality and Stress\_Level  
* Correlation between Exercise\_Frequency and Stress\_Level  
* Correlation between Happiness\_Index and Stress\_Level  
* Strongest and weakest predictors identified

3.3 Classification Model Performance

* Model type used (e.g., Logistic Regression, Random Forest, etc.)  
* Overall accuracy score  
* Confusion matrix results  
* Precision score  
* Recall score  
* F1-score

3.4 Feature Importance Rankings

* Most important predictor (rank 1\)  
* Second most important predictor (rank 2\)  
* Third most important predictor (rank 3\)  
* Direction of impact (positive/negative) for each predictor

3.5 Key Findings

* Main insights about stress level predictors  
* Model's effectiveness at classifying stress categories  
* Hypothesis validation regarding screen time (supported/not supported)  
* Unexpected findings or patterns  
* Practical implications

