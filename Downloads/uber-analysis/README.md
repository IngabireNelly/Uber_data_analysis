


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



## 🔍 **Results: Key Discoveries and Pattern Identification**

The following insights were discovered after analyzing the cleaned and enhanced Uber Fares dataset and visualizing the patterns using Power BI:

---

### 🕒 **High-Demand Periods**

* Ride volumes **peak between 8 AM–10 AM** and again from **4 PM–7 PM**, indicating strong commuting demand.
* **Fridays and Thursdays** show the highest ride volumes, aligning with work-week patterns and pre-weekend travel.
* These trends confirm that **Uber usage is highly tied to office hours and weekly social patterns**.

---

### 💵 **Fare Behavior**

* Most fares range from **\$5 to \$15**, with a strong concentration in this zone.
* Outliers up to **\$200+** suggest the presence of **long-distance or surge-priced** rides.
* Fares are **consistently higher during peak hours**, especially in the early morning and evening commute windows.

---

### ⏰ **Temporal Trends**

* Rides gradually build up starting from **6 AM**, with a major surge from **8 AM–9 AM**, and another peak during **evening rush hours**.
* A noticeable **drop in ride volume after 9 PM**, indicating reduced night demand.
* These patterns reflect typical **urban commuter behavior**.

---

### 📆 **Seasonal Patterns**

* **Spring months** (March–May) showed increased ride counts, potentially due to improved weather conditions and travel readiness.
* **Fall** showed a higher **average fare per ride**, likely due to longer travel distances or event-based surge pricing.

---

### 📍 **Geographic Concentration**

* Ride activity is heavily clustered around **New York City**, particularly **Manhattan and airport zones**.
* **Higher fare amounts** are more common around **JFK, LaGuardia**, and major business hubs—possibly due to airport transfers and premium rides.
* Spatial concentration shows that **urban cores and travel gateways command higher fares and traffic**.

---

These results clearly demonstrate that **time of day, weekday, season, and location** all play a major role in how Uber rides are distributed, priced, and demanded. These insights support strategic planning for operations, pricing, and marketing.

---

## 📌 **Conclusion: Summary of Main Findings & Recommendations**

---

### ✅ **Summary of Main Findings**

* **Fare distribution** is right-skewed, with most rides costing between **\$5 and \$15**.
* **Peak ride times** occur during **rush hours (8–10 AM, 4–7 PM)**, especially on **Fridays**.
* **Urban centers and airports** (JFK, Manhattan) generate **high volumes and high fares**.
* **Spring season** has the **highest ride counts**, while **Fall** shows the **highest average fares**.
* There is a clear **positive correlation between fare amount and ride distance**, validating pricing logic.

---

### 💡 **Recommendations: Data-Driven Business Suggestions**

#### 🎯 **Dynamic Pricing Optimization**

* Adjust surge pricing during **high-demand hours (8 AM, 6 PM)** and **Fridays** to maximize revenue while maintaining ride availability.

#### 🚗 **Strategic Driver Deployment**

* Encourage driver presence near **airports**, **business districts**, and during **peak times** to meet demand and reduce wait times.

#### 📣 **Targeted Promotions**

* Use insights to deploy **off-peak incentives** (e.g., winter months or late-night rides) to smooth out demand variability.

#### 🗺️ **Service Expansion**

* Explore extending coverage in **high-growth areas** outside the Manhattan core to capture untapped demand.

#### 🎁 **Customer Personalization**

* Segment users by ride time and fare behavior to offer **personalized deals or loyalty rewards** (e.g., morning commuter coupons).

#### 🚦 **Surge Preparation**

* Use time and season-based ride forecasting to **prepare infrastructure and support teams** for known surge periods.

---

By integrating these findings, Uber and similar platforms can improve both **operational efficiency and customer satisfaction** through smarter, **data-driven decision-making**.


---

## 👤 Author
```
** Nelly Ingabire**
 ID:27128
 AUCA – Department of Information Systems
 Instructor: Eric Maniraguha ([eric.maniraguha@auca.ac.rw](mailto:eric.maniraguha@auca.ac.rw))

---



```




