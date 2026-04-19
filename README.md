# Retail Store Sales & Profit Analytics Dashboard

## 📌 Project Overview
This project demonstrates an end-to-end data analytics workflow, starting from raw data manipulation in Python to building a dynamic business intelligence dashboard in Microsoft Excel. The goal of this analysis is to evaluate retail performance over a four-year period, identifying key revenue drivers, category profitability, and temporal sales trends.

**Author:** Abdul Rahman

## 🛠️ Tech Stack & Tools
* **Data Cleaning & Manipulation:** Python (Jupyter Notebook, `pandas`, `numpy`)
* **Data Aggregation:** Microsoft Excel (Pivot Tables)
* **Data Visualization:** Microsoft Excel (Pivot Charts, Interactive Dashboard)

## 🔄 Project Workflow

### Phase 1: Data Preparation (Python)
The raw dataset (`train.csv`) required significant cleaning before analysis. A Python script was developed to handle this seamlessly:
1.  **Data Ingestion:** Loaded the raw CSV file using Pandas.
2.  **Date Standardization:** Formatted the `Order Date` column into strict, standardized Datetime objects to ensure seamless time-series analysis in Excel.
3.  **Feature Engineering:** Simulated a realistic `Profit` column by applying a uniform random distribution (margin between -5% and +35%) over the existing `Sales` data.
4.  **Export:** Saved the processed data as a `.xlsx` file to preserve formatting and prevent data-type degradation.

### Phase 2: Analysis & Visualization (Excel)
The cleaned dataset (`Superstore_Cleaned_Ready.xlsx`) was imported into Excel for metric aggregation and visualization.
* Created distinct Pivot Tables to calculate Total Sales, Profit by Category, and Sales Over Time.
* Designed an interactive dashboard compiling these Pivot Charts to provide a holistic view of store performance.

## 📊 Key Insights & KPIs
* **Total Sales:** The dataset accounts for **$2.26M** in total sales volume.
* **Category Profitability:** **Technology** is the highest-performing category, generating the most profit (~$121K), followed closely by Furniture and Office Supplies.
* **Sales Trends:** There is a clear upward trajectory in sales from 2015 to 2018, with significant spikes occurring consistently in the 4th Quarter (Q4) of each year, indicating strong seasonal/holiday demand.

## 🖼️ Dashboard & Visuals

*(Click to expand the images)*

### Main Dashboard
![Main Dashboard](Dashboard%20image%20of%20task%201.png)

### Performance Breakdowns
| Total Sales KPI | Profit By Category | Sales Over Time |
| :---: | :---: | :---: |
| ![Total Sales](Total%20Sales%20for%20task%201.png) | ![Profit By Category](Profit%20By%20Category%20For%20task%201.png) | ![Sales Over Time](Sale%20over%20Time%20for%20task%201.png) |

## 📂 Repository Structure
```text
├── Data/
│   ├── train.csv                             # Raw dataset
│   └── Superstore_Cleaned_Ready.xlsx         # Final cleaned dataset with dashboard
├── Scripts/
│   └── Python_script_for_task_1.py           # Data cleaning & engineering script
├── Images/
│   ├── Dashboard image of task 1.png
│   ├── Profit By Category For task 1.png
│   ├── Sale over Time for task 1.png
│   └── Total Sales for task 1.png
└── README.md
