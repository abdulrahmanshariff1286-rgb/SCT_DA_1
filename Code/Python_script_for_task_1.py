import pandas as pd
import numpy as np

# 1. Load the raw data
# Replace 'train.csv' with the actual path to your downloaded file
df = pd.read_csv('train.csv.zip/train.csv')

# 2. Standardize the 'Order Date' column
# We force Python to read the DD/MM/YYYY format and convert it to a strict Datetime object.
# This ensures Excel recognizes it as a real timeline, not text.
try:
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
except Exception as e:
    # Fallback to standard parsing if the specific format fails
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# 3. Add the missing "Profit" column (Simulate it realistically)
# We set a seed so the random numbers generate exactly the same way every time you run it.
np.random.seed(42) 

# We create a realistic profit margin between -5% (a slight loss) and 35% (a good profit)
df['Profit'] = df['Sales'] * np.random.uniform(-0.05, 0.35, size=len(df))

# Round the new profit numbers to 2 decimal places to look like real currency
df['Profit'] = df['Profit'].round(2)

# 4. Save the cleaned data to an Excel file
# Exporting directly to .xlsx preserves the date formatting and avoids CSV text issues
output_filename = 'Superstore_Cleaned_Ready.xlsx'
df.to_excel(output_filename, index=False)

print(f"Data cleaning complete! File saved successfully as {output_filename}")
