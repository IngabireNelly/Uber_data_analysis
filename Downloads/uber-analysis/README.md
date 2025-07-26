


# 🚖 Uber Fare Data Analysis with Power BI

![Power BI Badge](https://img.shields.io/badge/Tool-Power%20BI-yellow?logo=powerbi)
![Python Badge](https://img.shields.io/badge/Python-Data--Cleaning-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> A data analytics project exploring Uber fare patterns using Python (Google Colab) and Power BI.  
> Built for the course **INSY 8413 - Introduction to Big Data Analytics** at AUCA.

---

## 📑 Table of Contents

- [📂 Project Structure](#-project-structure)
- [🎯 Objectives](#-objectives)
- [🧪 Methodology](#-methodology)
- [📊 Key Visuals](#-key-visuals)
- [📈 Insights & Recommendations](#-insights--recommendations)
- [🧰 Tools Used](#-tools-used)
- [📷 Screenshots](#-screenshots)
- [🔗 Dataset](#-dataset)
- [👤 Author](#-author)

---

## 📂 Project Structure


```
Uber-Fare-Analysis/
├── data/
│   ├── uber.csv
│   └── enhanced_uber.csv
├── dashboard/
│   └── UberDashboard.pbix
├── screenshots/
│   ├── data_loading.png
│   ├── cleaning_steps.png
│   ├── feature_engineering.png
│   ├── dashboard.png
├── Uber_Fare_Analysis.ipynb
└── README.md
```

---

## 🎯 Objectives

* Analyze Uber fare distribution and ride behavior
* Create time-based features: hour, weekday, peak time
* Build an interactive dashboard in Power BI
* Extract actionable business insights from the data

---

## 🧪 Methodology

### 🔹 Step 1: Data Cleaning (Python - Colab)

* Removed null/missing values
* Dropped irrelevant columns
* Calculated ride distance using the **Haversine formula**

### 🔹 Step 2: Feature Engineering

* Extracted: `hour`, `weekday`, `month`, `peak_status`
* Added to final dataset for Power BI

### 🔹 Step 3: Exploratory Data Analysis

* Descriptive stats (mean, median, std)
* Visuals: histograms, box plots, correlation matrix
* Analyzed ride volume and fare vs. distance/time

### 🔹 Step 4: Dashboard (Power BI)

See the [`screenshots/`](./powerBI) folder for:
* Visualized key KPIs
* Added filters (month, weekday, peak hours)
* Created interactive insights
Power BI file uploaded on a google drive:
https://drive.google.com/file/d/12ii9vmc4RsQEtQVvQah-L2cKr9d6Z0WC/view?usp=sharing
---

## 📊 Key Visuals

* Average Fare by Hour
* Fare Distribution by Weekday
* Ride Volume by Hour
* Correlation Heatmap
* Geographic Ride Map (Pickup Coordinates)
* Peak vs Off-Peak Fare Analysis
* Monthly Fare Trend

---

## 📈 Insights & Recommendations

* 🕒 Rides peak during **morning and evening rush hours**
* 💵 **Average fares increase at night and early morning**
* 🗓️ Weekdays are busier than weekends
* 📍 Longer rides show predictable correlation to fare
* 💡 Recommendation: Use temporal trends to optimize surge pricing and fleet management

---

## 🧰 Tools Used

* 🐍 **Python** (Google Colab): Pandas, Seaborn, Matplotlib
* 📊 **Power BI Desktop**
* 🌍 Haversine Formula (Geo Distance)
* 📄 GitHub for version control

---

## 📷 Screenshots

See the [`screenshots/`](./screenshoots) folder for:

* Data loading and cleaning
* Feature engineering steps
* Dashboard preview
* Filtered and interactive views

---

## 🔗 Dataset

Source: [Uber Fares Dataset - Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)

---

## 👤 Author
```
**Nelly Ingabire**
 AUCA – Department of Information Systems
 Instructor: Eric Maniraguha ([eric.maniraguha@auca.ac.rw](mailto:eric.maniraguha@auca.ac.rw))

---



```




