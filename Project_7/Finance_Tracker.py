import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_user_input():
    data = []
    while True:
        date = input("Enter date (YYYY-MM-DD) or 'stop' to end: ")
        if date.lower() == 'stop':
            break
        income = float(input("Enter income for the day: "))
        expenses = float(input("Enter expenses for the day: "))
        savings = float(input("Enter savings for the day: "))
        data.append({'Date': date, 'Income': income, 'Expenses': expenses, 'Savings': savings})
    return pd.DataFrame(data)

def generate_reports(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    monthly_summary = df.resample('M').sum()
    yearly_summary = df.resample('Y').sum()

    print("\nMonthly Summary:")
    print(monthly_summary)

    print("\nYearly Summary:")
    print(yearly_summary)
    
    return monthly_summary, yearly_summary

def create_visualizations(monthly_summary):
    monthly_summary[['Income', 'Expenses', 'Savings']].plot(kind='bar', figsize=(10, 5))
    plt.title('Monthly Financial Summary')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.show()

if __name__ == "__main__":
    df = get_user_input()
    monthly_summary, yearly_summary = generate_reports(df)
    create_visualizations(monthly_summary)
