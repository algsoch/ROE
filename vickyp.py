import pandas as pd
import csv

def process_csv_with_groups(input_file, output_file):
    # Read the CSV file
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Identify the group boundaries based on header
    header = "Maths,Physics,English,Economics,Biology\n"
    group_boundaries = [i for i, line in enumerate(lines) if line == header]
    
    print(f"Found {len(group_boundaries)} group headers")
    
    # Prepare output file
    with open(output_file, 'w', newline='') as outfile:
        # Add Group column to our header
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Group', 'Maths', 'Physics', 'English', 'Economics', 'Biology'])
        
        # Process each group
        for i in range(len(group_boundaries)):
            start_idx = group_boundaries[i] + 1  # Skip the header
            end_idx = group_boundaries[i+1] if i+1 < len(group_boundaries) else len(lines)
            
            # Determine current group number
            group_num = i + 1
            
            # Extract and process the data lines for this group
            for j in range(start_idx, end_idx):
                line = lines[j].strip()
                if line and not line.startswith("Maths"):  # Skip empty lines and headers
                    values = line.split(',')
                    if len(values) == 5:  # Ensure we have the right number of columns
                        # Write to the new file with group number
                        csv_writer.writerow([group_num] + values)
    
    print(f"Successfully processed {input_file} and saved results to {output_file}")

if __name__ == "__main__":
    process_csv_with_groups('vickyp.csv', 'groupmark.csv')
