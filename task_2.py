import pandas as pd
import numpy as np

# Ask for the file path
file_path = input("Enter the path to your sales data file: ")

print("Loading data...")

# Load the CSV into a DataFrame
try:
    sales_data_file = pd.read_csv(file_path, index_col="TransactionID")

    # Display a summary
    print(f"loaded! Total transactions: {len(sales_data_file)}")
    
    # Processing Data & Calculating Results
    
    revenue_per_transaction = sales_data_file['Quantity'] * sales_data_file['UnitPrice']

    # Total Revenue 
    total_rev = np.sum(revenue_per_transaction)
    
    # Average Sale per Transaction
    avg_sale = np.mean(revenue_per_transaction)
    
    # Highest and Lowest Sales
    max_sale  = np.max(revenue_per_transaction)
    min_sale  = np.min(revenue_per_transaction)
    
    # Best-Selling Product
    top_seller = sales_data_file.loc[revenue_per_transaction.idxmax(), 'Product']
    low_seller = sales_data_file.loc[revenue_per_transaction.idxmin(), 'Product']
    best_selling_product = sales_data_file.groupby("Product")["Quantity"].sum().idxmax()

    # Displaying Results in a Report
    print('\nRetail Sales Report')
    print('----------------------------\n')
    print(f'Total Transactions: {len(sales_data_file)}')
    print(f'Total Revenue: ${total_rev:,.0f}')
    print(f'Average Sale: ${avg_sale}')
    print(f'Highest Sale: ${max_sale:,} (Product: {top_seller})')
    print(f'Highest Sale: ${min_sale:,} (Product: {low_seller})')
    print(f'Best-Selling Product: {best_selling_product}')

    print("----------------------------------------- \n")


except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

