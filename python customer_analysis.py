import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Fill missing ages with median
    data['age'].fillna(data['age'].median(), inplace=True)
    # Fill missing purchases with 0
    data['total_purchases'].fillna(0, inplace=True)
    # Drop rows with missing emails
    data.dropna(subset=['email'], inplace=True)
    return data

def summary_stats(data):
    print("Customer Summary:")
    print(f"Total customers: {len(data)}")
    print(f"Average age: {data['age'].mean():.2f}")
    print(f"Total purchases sum: ${data['total_purchases'].sum():.2f}")

def top_customers(data, n=3):
    top = data.sort_values(by='total_purchases', ascending=False).head(n)
    print("\nTop Customers:")
    print(top[['customer_id', 'name', 'total_purchases']])

def save_clean_data(data, file_path):
    data.to_csv(file_path, index=False)
    print(f"Cleaned data saved to {file_path}")

if __name__ == "__main__":
    data = load_data('customers.csv')
    data = clean_data(data)
    summary_stats(data)
    top_customers(data)
    save_clean_data(data, 'customers_cleaned.csv')

