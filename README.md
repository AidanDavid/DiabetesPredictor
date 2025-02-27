# 🏥 Diabetes Predictor

This project focuses on developing a **predictive model for diabetes classification** based on **health indicators**. Using machine learning techniques, we analyze risk factors such as **BMI, physical activity, cholesterol levels, and blood pressure** to determine whether an individual is **diabetic, pre-diabetic, or non-diabetic**.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Target Variable & Key Features](#target-variable--key-features)
- [Usage Guide](#usage-guide)
- [Visualizations](#visualizations)
- [Technologies Used](#technologies-used)
- [References](#references)
- [Credits](#credits)
- [License](#license)

---

## 🎯 Project Overview

The goal of this project is to build a **machine learning model** to predict **diabetes status** (No Diabetes, Pre-Diabetes, Diabetes) using **health-related features**. The dataset contains **key lifestyle and medical indicators** that help in identifying diabetes risk.

- **Goal:** Understand **risk factors contributing to diabetes** for better predictive modeling.  
- **Analyzed Features:**  
  - **Age vs. BMI** (by Diabetes Status)  
  - **High BP vs. High Cholesterol**  
  - **Diabetes Distribution by Key Indicators**  

---

## 🎯 Target Variable & Key Features

### **Target Variable**
- **Diabetes_012**  
  - `0 = No Diabetes`  
  - `1 = Pre-Diabetes`  
  - `2 = Diabetes`  

### **Key Features**
- **BMI** – Body Mass Index (continuous value)  
- **High Blood Pressure (BP)** – Indicator of hypertension  
  - `0 = No High BP`  
  - `1 = High BP`  
- **High Cholesterol (Chol)** – Indicator of cholesterol levels  
  - `0 = No High Cholesterol`  
  - `1 = High Cholesterol`  
- **Physical Activity** – Engagement in physical activity (excluding job-related activity)  
  - `0 = No`  
  - `1 = Yes`    
- **Age** – Originally, the dataset categorized age into only three broad groups:
  - `1 = 18-24`  
  - `9 = 60-64`  
  - `13 = 80 or older`  
  
  For **better visualization and clarity**, the age groups have been **divided into finer categories** (e.g., 18-24, 25-29, 30-34, etc.), making the trends more interpretable.
- **Sex** – Gender of the individual  
  - `0 = Female`  
  - `1 = Male`  

---

## 🛠️ Usage Guide

### 1️⃣ Clone the Repo
To run this project locally, follow these steps:

```bash
git clone https://github.com/AidanDavid/DiabetesPredictor.git
cd DiabetesPredictor
```

### 2️⃣ Running the Analysis
Launch Jupyter Notebook:

```bash
jupyter notebook
```
Ensure all required Python libraries are installed:

```bash
pip install -r requirements.txt
```

Open the relevant notebook file and execute the cells step by step to **analyze and visualize diabetes risk factors**.

---

## 🌊 Visualizations

Explore the **Tableau Public dashboard** to visualize diabetes risk factors:

[![View on Tableau Public](https://img.shields.io/badge/View-Tableau%20Public-blue)](https://public.tableau.com/app/profile/yiheng.sun/viz/diabetes_17406445784920/Story1)

### **How to Use This Visualization**
1. **Click the Tableau Public link** to open the interactive dashboard.  
2. **Use filters** (age group, diabetes status) to explore trends.  
3. **Hover over data points** to view additional insights.  

🔗 **[View the Full Dashboard Here](https://public.tableau.com/app/profile/yiheng.sun/viz/diabetes_17406445784920/Story1)**  

---

## 🔧 Technologies Used
- **Python**: For data analysis and visualization.  
- **Pandas**: For data manipulation and aggregation.  
- **Jupyter Notebook**: For executing data science workflows.  
- **Tableau Public**: For interactive data visualization.  

---

## 📚 References

### **Data Sources**
- **Kaggle**: [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

---

## 💪 Credits

This project was developed by:

👤 **Yiheng Sun**  
- **GitHub**: [@Sait0uAsuka](https://github.com/Sait0uAsuka)

👤 **Aidan David**  
- **GitHub**: [@AidanDavid](https://github.com/AidanDavid)

👤 **Lucas Hejmo Jones**  
- **GitHub**: [@LucasHejmo](https://github.com/LucasHejmo)

---

## 📝 License
This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.  