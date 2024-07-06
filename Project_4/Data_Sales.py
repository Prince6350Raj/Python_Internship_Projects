import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_df = pd.read_csv('sales_data.csv')
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

product_sales = sales_df.groupby('Product').agg({'Sales': 'sum', 'Quantity': 'sum'})
region_sales = sales_df.groupby('Region').agg({'Sales': 'sum', 'Quantity': 'sum'})
monthly_sales = sales_df.resample('M', on='Date').agg({'Sales': 'sum'})

average_sales = sales_df[['Sales', 'Quantity']].mean()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
product_sales['Sales'].plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')

plt.subplot(2, 2, 2)
region_sales['Sales'].plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')

plt.subplot(2, 2, 3)
monthly_sales['Sales'].plot(kind='line', marker='o', linestyle='-', color='salmon')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.subplot(2, 2, 4)
average_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral'])
plt.title('Average Sales and Quantity')
plt.ylabel('')

plt.tight_layout()
plt.show()

summary_report = f"""
Sales Data Analysis
===================

Total Sales and Quantity by Product:
{product_sales}

Total Sales and Quantity by Region:
{region_sales}

Monthly Sales Trends:
{monthly_sales}

Average Sales and Quantity:
{average_sales}
"""

print(summary_report)

with open('sales_summary_report.txt', 'w') as file:
    file.write(summary_report)
