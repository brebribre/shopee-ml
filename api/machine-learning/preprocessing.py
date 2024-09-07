import pandas as pd

# Load the Excel file
xls = pd.ExcelFile('./assets/sep2022-ag2024.xlsx', engine='openpyxl')

# Specify the columns you want to extract
columns_to_read = ['No. Pesanan', 'Status Pesanan', 'Nomor Referensi SKU', 'Harga Awal', 'Harga Setelah Diskon', 'Jumlah', 'Nomor Referensi SKU']

# Load data from the first sheet (first month)
first_month_data = pd.read_excel(xls, sheet_name=xls.sheet_names[0], usecols=columns_to_read, dtype=str)

# Specify what NaN means
first_month_data['Nomor Referensi SKU'] = first_month_data['Nomor Referensi SKU'].fillna('UNKNOWN')

# Remove commas and convert the columns to float
first_month_data['Harga Awal'] = first_month_data['Harga Awal'].str.replace('.', '').astype(int)
first_month_data['Harga Setelah Diskon'] = first_month_data['Harga Setelah Diskon'].str.replace('.', '').astype(int)

# Display the first few rows of the data
print(first_month_data.head())

# Save the data to a new Excel file (this will override the file each time)
output_file = './assets/first_month_data.xlsx'
first_month_data.to_excel(output_file, index=False)

print(f"Data from the first month has been saved (overwritten) to {output_file}")
