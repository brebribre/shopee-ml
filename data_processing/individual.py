import pandas as pd
from .utils import clean_price_column, save_processed_data_to_excel, apply_styles
from io import BytesIO
import json

columns_to_read = [
        'No. Pesanan', 
        'Status Pesanan', 
        'Nama Produk',
        'Nomor Referensi SKU', 
        'Jumlah', 
        'Harga Setelah Diskon', 
        'Total Harga Produk', 
        'Diskon Dari Shopee',
]

def process_single_sheet_as_individual(sheet_name, xls, columns_to_read, processed_data):
    # Load data from the specified sheet
    data = pd.read_excel(xls, sheet_name=sheet_name, usecols=columns_to_read, dtype=str)

    # Only process 'finished' orders
    data = data[data['Status Pesanan'] == 'Selesai']

    # Specify missing data
    data['Nomor Referensi SKU'] = data['Nomor Referensi SKU'].fillna('UNKNOWN')

    print('starting')

    # Remove commas and convert the columns to float from IDR values
    data = clean_price_column(data, 'Harga Setelah Diskon')
    data = clean_price_column(data, 'Total Harga Produk')
    data = clean_price_column(data, 'Diskon Dari Shopee')
    data['Jumlah'] = data['Jumlah'].astype(int)

    #add needed empty rows

    # Store the processed data for the sheet
    processed_data[sheet_name] = data

def pipeline_all_sheets_as_excel_individual(input_file):
    xls = pd.ExcelFile(input_file, engine='openpyxl')

    processed_data = {}

    for sheet in xls.sheet_names:
        process_single_sheet_as_individual(sheet, xls, columns_to_read, processed_data)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        save_processed_data_to_excel(writer, processed_data) 
        
        workbook = writer.book
        sheets = {sheet.title: sheet for sheet in workbook.worksheets}
        
        apply_styles(sheets)

    output.seek(0)
    
    return output
