import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill

def clean_price_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = df[column_name].astype(str)  # Convert to string
    df[column_name] = df[column_name].str.replace('.', '', regex=False)  # Remove periods
    df[column_name] = df[column_name].astype(int)  # Convert to integer

    return df

# Function to save processed_data to Excel
def save_processed_data_to_excel(writer, processed_data):
    for sheet_name, data in processed_data.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

def apply_styles(sheets):
    for sheet_name, ws in sheets.items():
        # Apply styling to the header row
        for cell in ws[1]:
            cell.font = Font(bold=True)
        
        ws.column_dimensions['A'].width = 20  # Nomor Referensi SKU
        ws.column_dimensions['B'].width = 80  # Nama Produk
        ws.column_dimensions['C'].width = 10  # Jumlah
        ws.column_dimensions['D'].width = 20  # Total Harga Produk
