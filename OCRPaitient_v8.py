import pandas as pd
from PyPDF2 import PdfReader

# Function to extract text from a PDF page
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to parse the laboratory results into a pandas DataFrame
def parse_lab_results_to_table(text):
    # Split the text by lines
    lines = text.split('\n')
    
    # Process the lines and extract data
    data = []
    for line in lines:
        # Split the line by whitespace and filter out empty strings
        parts = list(filter(None, line.split(' ')))
        data.append(parts)

    # Convert to DataFrame, dynamically handling the number of columns
    df = pd.DataFrame(data)

    # If the first row is header, set it as the DataFrame header
    df.columns = df.iloc[0]  # Set the first row as the header
    df = df[1:]  # Remove the first row from the data

    # Reset index after dropping the first row
    df.reset_index(drop=True, inplace=True)

    # Optionally, convert columns to the correct data type and handle missing values
    #df = df.apply(pd.to_numeric, errors='ignore')

    return df

# Path to the PDF file
pdf_path = 'ali2.pdf'

# Extract text from PDF
text = extract_text_from_pdf(pdf_path)

# Parse text to table
lab_results_df = parse_lab_results_to_table(text)

# Write the DataFrame to a CSV file
csv_file_path = 'lab_results222.csv'  # Specify the desired CSV file path
lab_results_df.to_csv(csv_file_path, index=False)  # Write DataFrame to CSV file without the index

# Display a message to the user
print(f'The lab results have been written to {csv_file_path}')