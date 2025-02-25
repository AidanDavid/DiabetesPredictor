# Diabetes Predictor

This project focuses on developing a predictive model for diabetes classification based on health indicators. Using machine learning techniques, we analyze risk factors such as BMI, physical activity, cholesterol levels, and blood pressure to determine whether an individual is diabetic, pre-diabetic, or non-diabetic.

## Overview

The goal of this project is to build a machine learning model to predict **diabetes status** (No Diabetes, Pre-Diabetes, Diabetes) using **health-related features**. The dataset contains key **lifestyle and medical indicators** that help in identifying diabetes risk.

### Target Variable
- **Diabetes_012**  
  - `0 = No Diabetes`  
  - `1 = Pre Diabetes`  
  - `2 = Diabetes`  

### Key Features
- **BMI** (Body Mass Index)  
- **High Blood Pressure** (0 = no high BP 1 = high BP)  
- **High Cholesterol** (0 = no high cholesterol, 1 = high cholesterol)  
- **Physical Activity** (physical activity in past 30 days - not including job. 0 = no, 1 = yes)  
- **General Health Score**  (Would you say that in general your health is: scale 1-5. 
                            1 = excellent 2 = very good 3 = good 4 = fair 5 = poor)
- **Age** (13-level age category. 1 = 18-24 9 = 60-64 13 = 80 or older)
- **Sex** (0 = female, 1 = male)  

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
