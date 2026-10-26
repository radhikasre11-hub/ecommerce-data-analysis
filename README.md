# E-Commerce Data Analysis

## Project Overview
This project analyzes online retail transaction data to identify sales trends, best-selling products, and top-performing countries. Python is used to clean, analyze, and visualize the dataset to generate meaningful business insights.

## Objectives
- Clean and prepare the retail dataset.
- Identify duplicate records, missing values, and invalid transactions.
- Calculate total revenue and order counts.
- Identify the best-selling products and highest-revenue countries.
- Analyze monthly revenue and month-to-month growth.
- Present findings through visualizations.

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code

## Dataset
The project uses the Online Retail dataset, containing transaction information such as invoice numbers, product descriptions, quantities, unit prices, invoice dates, customer IDs, and countries.

## Data Cleaning
- Removed duplicate records.
- Removed records with missing product descriptions.
- Excluded transactions with non-positive quantities or unit prices from the main sales analysis.
- Converted invoice dates to datetime format.
- Calculated revenue using Quantity × UnitPrice.

## Key Performance Indicators
- Total Revenue
- Total Orders
- Best-Selling Product
- Top Country by Revenue
- Month with Highest Revenue

## Visualizations
The project includes the following charts:
1. Top 10 Best-Selling Products
2. Monthly Revenue Trend
3. Top 10 Countries by Revenue
4. Month-to-Month Revenue Growth

Charts are stored in the `visuals` folder.

## How to Run the Project
1. Install Python.
2. Install the required libraries:
   `python -m pip install pandas numpy matplotlib seaborn`
3. Keep `OnlineRetail.csv` and `analysis.py` in the same project folder.
4. Run:
   `python analysis.py`

## Conclusion
This project demonstrates how Python can be used to clean retail transaction data, analyze sales performance, identify trends, and communicate business insights through charts.

## Dataset

The Online Retail dataset is available on Kaggle:

https://www.kaggle.com/datasets/vijayuv/onlineretail

Download the dataset and place `OnlineRetail.csv` in the same folder as `analysis.py` before running the project.

The dataset is not included in this repository because of its large file size.