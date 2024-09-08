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
            cell.background = "00FF00"

    
        

def set_column_widths(worksheet):
    # Optionally adjust column widths to fit the content
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter  # Get the column letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = max_length + 2
        worksheet.column_dimensions[column_letter].width = adjusted_width