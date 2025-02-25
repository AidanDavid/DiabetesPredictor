# Diabetes Predictor

This project focuses on developing a predictive model for diabetes classification based on health indicators. Using machine learning techniques, we analyze risk factors such as BMI, physical activity, cholesterol levels, and blood pressure to determine whether an individual is diabetic, pre-diabetes, or non-Diabetic.

## Overview

The goal of this project is to build a machine learning model to predict **diabetes status** (No Diabetes, Pre Diabetes, Diabetes) using **health-related features**. The dataset contains key **lifestyle and medical indicators** that help in identifying diabetes risk.

### Target Variable
- **Diabetes_012**  
  - `0 = No Diabetes`  
  - `1 = Pre Diabetes`  
  - `2 = Diabetes`  

### Key Features

- **BMI** – Body Mass Index (continuous value)  
- **High Blood Pressure** – Indicates if the person has high blood pressure  
  - `0 = No High BP`  
  - `1 = High BP`  
- **High Cholesterol** – Indicates if the person has high cholesterol  
  - `0 = No High Cholesterol`  
  - `1 = High Cholesterol`  
- **Physical Activity** – Engaged in physical activity in the past 30 days (excluding job-related activity)  
  - `0 = No`  
  - `1 = Yes`  
- **General Health Score** – Self-reported health rating on a scale of 1-5  
  - `1 = Excellent`  
  - `2 = Very Good`  
  - `3 = Good`  
  - `4 = Fair`  
  - `5 = Poor`  
- **Age** – 13-level categorical variable representing age groups  
  - `1 = 18-24`  
  - `9 = 60-64`  
  - `13 = 80 or older`  
- **Sex** – Gender of the individual  
  - `0 = Female`  
  - `1 = Male`  


## Table of Contents

- [Usage Guide](#usage-guide)
- [Visualizations](#visualizations)
- [Technologies Used](#technologies-used)
- [References](#references)
- [Credits](#credits)
- [License](#license)


## Usage Guide

### Data Usage Description



### 1. Glone the Repo

To run this project locally, follow these steps:

**Clone the repository**:

   ```bash
   git clone https://github.com/AidanDavid/DiabetesPredictor.git
   cd DiabetesPredictor
   ```

### 2. Running the Analysis

Launch Jupyter Notebook:

```bash
jupyter notebook
```
Ensure all libraries are properly installed:
```
pip install -r requirements.txt
```

Open the relevant notebook file and execute the cells step by step to analyze and visualize the volcanic data.

## Visualizations
- **Tableau Public**: 

## Technologies Used

- **Python**: For data analysis and visualization.  
- **Pandas**: For data manipulation and aggregation.   


## References

### Data Sources
- **Kaggle**: [Kaggle]https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset


## Credits

This project was independently developed by the following developers:

**Yiheng Sun**:

- **Github**: [@Sait0uAsuka](https://github.com/Sait0uAsuka)

**Aidan David**:

- **Github**: [@AidanDavid](https://github.com/AidanDavid)

**Lucas Hejmo Jones**:

- **Github**: [@LucasHejmo](https://github.com/LucasHejmo)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
