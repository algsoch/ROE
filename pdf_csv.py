import pdfplumber
import csv
import os

def convert_pdf_to_csv(pdf_path, csv_path):
    """Convert a PDF file to CSV format."""
    try:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Open CSV file for writing
            with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Process each page
                for page in pdf.pages:
                    # Extract tables from the page
                    table = page.extract_table()
                    
                    if table:
                        # Write all rows to CSV
                        for row in table:
                            # Clean the row data (remove None values and strip whitespace)
                            cleaned_row = [str(cell).strip() if cell is not None else '' for cell in row]
                            csv_writer.writerow(cleaned_row)
            
        print(f"Successfully converted {pdf_path} to {csv_path}")
        return True
    
    except Exception as e:
        print(f"Error converting PDF to CSV: {e}")
        return False

# File paths
pdf_file = "vickyp.pdf"
csv_file = "vickyp.csv"

# Convert the PDF to CSV
convert_pdf_to_csv(pdf_file, csv_file)