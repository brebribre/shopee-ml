import pandas as pd
from .utils import clean_price_column, save_processed_data_to_excel, apply_styles
from io import BytesIO
import json

columns_to_read = [
        'No. Pesanan', 
        'Status Pesanan', 
        'Nomor Referensi SKU', 
        'Harga Awal', 
        'Harga Setelah Diskon', 
        'Total Harga Produk', 
        'Jumlah', 
        'Nomor Referensi SKU', 
        'Nama Produk'
]

def process_single_sheet(sheet_name, xls, columns_to_read, processed_data):
    # Load data from the specified sheet
    data = pd.read_excel(xls, sheet_name=sheet_name, usecols=columns_to_read, dtype=str)

    # Only process 'finished' orders
    data = data[data['Status Pesanan'] == 'Selesai']

    # Specify missing data
    data['Nomor Referensi SKU'] = data['Nomor Referensi SKU'].fillna('UNKNOWN')

    # Remove commas and convert the columns to float from IDR values
    data = clean_price_column(data, 'Harga Awal')
    data = clean_price_column(data, 'Harga Setelah Diskon')
    data = clean_price_column(data, 'Total Harga Produk')
    data['Jumlah'] = data['Jumlah'].astype(int)

    # Group the data by 'Nomor Referensi SKU' and 'Nama Produk'
    grouped_data = data.groupby(['Nomor Referensi SKU', 'Nama Produk'], as_index=False).agg({
        'Jumlah': 'sum',
        'Total Harga Produk': 'sum'
    })

    # Add a total row at the end of the grouped data
    total_row = {
        'Nomor Referensi SKU': 'TOTAL',
        'Nama Produk': '',
        'Jumlah': grouped_data['Jumlah'].sum(),
        'Total Harga Produk': grouped_data['Total Harga Produk'].sum()
    }

    # Append the total row to the grouped data
    grouped_data = pd.concat([grouped_data, pd.DataFrame(total_row, index=[0])])

    # Store the processed data for the sheet
    processed_data[sheet_name] = grouped_data

def pipeline_all_sheets_as_excel(input_file):
    xls = pd.ExcelFile(input_file, engine='openpyxl')

    processed_data = {}

    for sheet in xls.sheet_names:
        process_single_sheet(sheet, xls, columns_to_read, processed_data)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        save_processed_data_to_excel(writer, processed_data) 
        
        workbook = writer.book
        sheets = {sheet.title: sheet for sheet in workbook.worksheets}
        
        apply_styles(sheets)

    output.seek(0)
    
    return output

def pipeline_all_sheets_as_json(input_file):
    xls = pd.ExcelFile(input_file, engine='openpyxl')

    processed_data = {}

    for sheet in xls.sheet_names:
        process_single_sheet(sheet, xls, columns_to_read, processed_data)

    #this converts it to a serializable data that is readable by json.dumps
    serializable_data = {sheet: df.to_dict(orient='records') for sheet, df in processed_data.items()}
    json_data = json.dumps(serializable_data, ensure_ascii=False)

    return json_data

