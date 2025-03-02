import pandas as pd
import zipfile
import os
import requests
from io import BytesIO

# Download and unzip the data
# Since no URL was provided, you'll need to replace this with the actual URL
# response = requests.get("URL_TO_YOUR_ZIP_FILE")
# zip_file = BytesIO(response.content)
# with zipfile.ZipFile(zip_file, 'r') as zip_ref:
#     zip_ref.extractall('.')

# Assuming the files are now unzipped in the current directory
students_df = pd.read_csv('students.csv')
subjects_df = pd.read_csv('subjects.csv')

# Create a dictionary mapping studentId to class
student_to_class = dict(zip(students_df['studentId'], students_df['class']))

# Initialize a dictionary to store subjects taken by each class
class_subjects = {}

# Iterate through subjects data
for _, row in subjects_df.iterrows():
    student_id = row['studentId']
    subject = row['subject']
    
    # Get the class of this student
    student_class = student_to_class.get(student_id)
    if student_class is None:
        continue
    
    # Add subject to the class's set of subjects
    if student_class not in class_subjects:
        class_subjects[student_class] = set()
    class_subjects[student_class].add(subject)

# Calculate number of unique subjects per class
subject_counts = [len(subjects) for subjects in class_subjects.values()]

# Sort the counts in ascending order
subject_counts.sort()

# Get the 3 lowest counts
lowest_three = subject_counts[:3]

# Format the result as requested
result = ','.join(map(str, lowest_three))
print(f"The 3 lowest counts of subjects per class are: {result}")