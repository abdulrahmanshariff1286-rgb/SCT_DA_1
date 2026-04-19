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
![Main Dashboard]<img width="1104" height="532" alt="Dashboard image of task 1" src="https://github.com/user-attachments/assets/452e7127-b813-4203-8809-8bd01bd20ec0" />


### Performance Breakdowns
| Total Sales KPI | Profit By Category | Sales Over Time |
| :---: | :---: | :---: |
| ![Total Sales]<img width="865" height="473" alt="Total Sales for task 1" src="https://github.com/user-attachments/assets/f7a8767c-d482-467b-827e-d2684985cd90" />
 | ![Profit By Category]<img width="862" height="387" alt="Profit By Category For task 1" src="https://github.com/user-attachments/assets/f0788de3-dcda-4df2-bb03-b782efca0b39" />
 | ![Sales Over Time]<img width="884" height="541" alt="Sale over Time for task 1" src="https://github.com/user-attachments/assets/638dd98d-731d-4526-af81-69ba5012ffd3" />
 |


