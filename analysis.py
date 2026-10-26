import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("OnlineRetail.csv", encoding="cp1252")

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())


# Step 3: Check data quality

print("\nTotal duplicate rows:")
print(df.duplicated().sum())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nNegative quantities:")
print((df["Quantity"] < 0).sum())

print("\nNegative or zero prices:")
print((df["UnitPrice"] <= 0).sum())


# Step 4: Clean the dataset

# Create a copy so the original data remains unchanged
clean_df = df.copy()

# Remove duplicate rows
clean_df = clean_df.drop_duplicates()

# Remove rows with missing product descriptions
clean_df = clean_df.dropna(subset=["Description"])

# Keep only positive quantities and prices
clean_df = clean_df[
    (clean_df["Quantity"] > 0) &
    (clean_df["UnitPrice"] > 0)
]

# Convert InvoiceDate to datetime
clean_df["InvoiceDate"] = pd.to_datetime(
    clean_df["InvoiceDate"],
    errors="coerce"
)

# Remove rows with invalid dates
clean_df = clean_df.dropna(subset=["InvoiceDate"])

# Calculate revenue
clean_df["Revenue"] = (
    clean_df["Quantity"] * clean_df["UnitPrice"]
)

# Display cleaning results
print("\n--- CLEANING RESULTS ---")
print("Original rows:", len(df))
print("Rows after cleaning:", len(clean_df))
print("Remaining duplicates:", clean_df.duplicated().sum())
print("Remaining missing descriptions:",
      clean_df["Description"].isnull().sum())
print("Remaining invalid quantities:",
      (clean_df["Quantity"] <= 0).sum())
print("Remaining invalid prices:",
      (clean_df["UnitPrice"] <= 0).sum())

print("\nCleaned dataset preview:")
print(clean_df.head())

print("\nTotal revenue:", round(clean_df["Revenue"].sum(), 2))


# Step 5: Business analysis

# Total revenue
total_revenue = clean_df["Revenue"].sum()

# Total unique orders
total_orders = clean_df["InvoiceNo"].nunique()

# Best-selling products by quantity
top_products = (
    clean_df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Country-wise revenue
country_revenue = (
    clean_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Display results
print("\n--- BUSINESS INSIGHTS ---")
print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)

print("\nTop 10 Best-Selling Products:")
print(top_products)

print("\nTop 10 Countries by Revenue:")
print(country_revenue.head(10))


# Step 6: Visualize Top 10 Best-Selling Products

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    color="steelblue"
)

plt.title("Top 10 Best-Selling Products", fontsize=16)
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Description")
plt.tight_layout()

# Save the chart
plt.savefig("top_10_products.png", dpi=300)

# Display the chart
plt.show()


# Step 7: Monthly Revenue Analysis

# Extract month from InvoiceDate
clean_df["Month"] = clean_df["InvoiceDate"].dt.to_period("M")

# Calculate monthly revenue
monthly_revenue = (
    clean_df.groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)

print("\n--- MONTHLY REVENUE ---")
print(monthly_revenue)

# Create the chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save and display the chart
plt.savefig("monthly_revenue.png", dpi=300)
plt.show()


# Step 8: Country-wise Revenue Analysis

# Calculate revenue for each country
country_revenue = (
    clean_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Select top 10 countries
top_countries = country_revenue.head(10)

print("\n--- TOP 10 COUNTRIES BY REVENUE ---")
print(top_countries.round(2))

# Create the chart
plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    color="teal"
)

plt.title("Top 10 Countries by Revenue", fontsize=16)
plt.xlabel("Total Revenue")
plt.ylabel("Country")
plt.tight_layout()

# Save and display the chart
plt.savefig("country_revenue.png", dpi=300)
plt.show()


# Step 9: Monthly Revenue Growth

# Calculate month-to-month growth percentage
monthly_growth = monthly_revenue.pct_change() * 100

print("\n--- MONTHLY REVENUE GROWTH (%) ---")
print(monthly_growth.round(2))

# Create growth chart
plt.figure(figsize=(12, 6))

plt.bar(
    monthly_growth.index.astype(str),
    monthly_growth.values
)

plt.title("Month-to-Month Revenue Growth", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Revenue Growth (%)")
plt.xticks(rotation=45)
plt.axhline(y=0, linestyle="--")
plt.tight_layout()

# Save chart
plt.savefig("monthly_growth.png", dpi=300)
plt.show()


# Step 10: Final KPI Summary

# Total revenue
total_revenue = clean_df["Revenue"].sum()

# Total orders
total_orders = clean_df["InvoiceNo"].nunique()

# Top-selling product by quantity
best_product = (
    clean_df.groupby("Description")["Quantity"]
    .sum()
    .idxmax()
)

# Country with highest revenue
top_country = (
    clean_df.groupby("Country")["Revenue"]
    .sum()
    .idxmax()
)

# Month with highest revenue
best_month = monthly_revenue.idxmax()

# Display KPI summary
print("\n========== FINAL KPI SUMMARY ==========")
print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Best-Selling Product:", best_product)
print("Top Country by Revenue:", top_country)
print("Highest Revenue Month:", best_month)
print("=======================================")
