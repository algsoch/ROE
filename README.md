# ROE
solving question
1 Write a FastAPI proxy server (1 mark)
Write a FastAPI proxy server that serves the data from the given URL but also adds a CORS header Access-Control-Allow-Origin: * to the response.

For example, if your API URL endpoint is http://127.0.0.1:8000/api, then a request to http://127.0.0.1:8000/api?url=https%3A%2F%2Fexample.com%2F%3Fkey%3Dvalue should return the data from https://example.com/?key=value but with the CORS header.

Note: Keep your server running for the duration of the exam.

What is your FastAPI Proxy URL endpoint?
http://127.0.0.1:8000/api
Correct
We'll check by sending a request to this URL with ?url=... check if the response matches the data.

2 Find common tags on StackOverflow (1 mark)
The StackOverflow API lets you find all tags related to a given tag. Associated with each tag is a common question count -- the number of questions tagged with that tag and your tag.

Find the tag that whose common question count with tag windows + common question count with tag regex is the highest.

Which tag is associated most with windows and regex?
python
Correct
Find the tags related to windows and to regex. Add the counts and enter largest tag.

3 Least unique subjects from CSV (1 mark)
Download and unzip . It has 2 files:

students.csv has 2 columns:
studentId: A unique identifier for each student
class: The class (including section) of the student
subjects.csv has 2 columns:
studentId: The identifier for each student
subject: The name of the subject they have chosen
What are the least number of subjects any class has taken up? List the 3 lowest count of subjects in order.
16,119,123
Correct
Find the number of unique subjects in each class. Then calculate the minimum of those. Sort in ascending order. List the first 3 values separated by commas, without spaces (e.g. 45,45,48)

4 Extract tables from PDF (1 mark)
Academic Performance Analysis for EduAnalytics
EduAnalytics Corp. is a leading educational technology company that partners with schools and educational institutions to provide data-driven insights into student performance. By leveraging advanced analytics and reporting tools, EduAnalytics helps educators identify trends, improve teaching strategies, and enhance overall student outcomes. One of their key offerings is the Performance Insight Dashboard, which aggregates and analyzes student marks across various subjects and demographic groups.

EduAnalytics has recently onboarded Greenwood High School, a large educational institution aiming to optimize its teaching methods and improve student performance in core subjects. Greenwood High School conducts annual assessments in multiple subjects, and the results are compiled into detailed PDF reports each semester. However, manually extracting and analyzing this data is time-consuming and prone to errors, especially given the volume of data and the need for timely insights.

To address this, EduAnalytics plans to automate the data extraction and analysis process, enabling Greenwood High School to receive precise and actionable reports without the delays associated with manual processing.

As part of this initiative, you are a data analyst at EduAnalytics assigned to develop a module that processes PDF reports containing student marks. Each PDF, named in the format xxx.pdf, includes a comprehensive table listing student performances across various subjects, along with their respective groups.

Greenwood High School has specific analytical needs, such as:

Subject Performance Analysis: Understanding how students perform in different subjects to identify areas needing improvement.
Group-Based Insights: Analyzing performance across different student groups to ensure equitable educational support.
Threshold-Based Reporting: Focusing on students who meet or exceed certain performance thresholds to tailor advanced programs or interventions.
Your Task
This file,  contains a table of student marks in Maths, Physics, English, Economics, and Biology.

Calculate the total Maths marks of students who scored 67 or more marks in English in groups 60-96 (including both groups).

Data Extraction:: Retrieve the PDF file containing the student marks table and use PDF parsing libraries (e.g., Tabula, Camelot, or PyPDF2) to accurately extract the table data into a workable format (e.g., CSV, Excel, or a DataFrame).
Data Cleaning and Preparation: Convert marks to numerical data types to facilitate accurate calculations.
Data Filtering: Identify students who have scored marks between 67 and English in groups 60-96 (including both groups).
Calculation: Sum the marks of the filtered students to obtain the total marks for this specific cohort.
By automating the extraction and analysis of student marks, EduAnalytics empowers Greenwood High School to make informed decisions swiftly. This capability enables the school to:

Identify Performance Trends: Quickly spot areas where students excel or need additional support.
Allocate Resources Effectively: Direct teaching resources and interventions to groups and subjects that require attention.
Enhance Reporting Efficiency: Reduce the time and effort spent on manual data processing, allowing educators to focus more on teaching and student engagement.
Support Data-Driven Strategies: Use accurate and timely data to shape educational strategies and improve overall student outcomes.
What is the total Maths marks of students who scored 67 or more marks in English in groups 60-96 (including both groups)?
21424
Correct
5 DuckDB: Sales Over Time (1 mark)
You are connected to a DuckDB database with a table called sales containing 10,000 rows of data with 3 columns.

timestamp: When the sale occurred (for the week starting on 2024-01-01 UTC).
category: Category of product sold (e.g. "Electronics", "Clothing", ...).
amount: The sale value as a number (e.g. 12.34).
Write the DuckDB SQL query to find the total sales amounts for each product category, pivoted by hour:

Aggregate total sales amounts into hourly intervals (UTC) and pivot the data.
Show total sales amount per category per hour (filling missing combinations with zeros), to the nearest integer.
Order rows chronologically by hour and columns in any order.
The result should look like this:
What is the DuckDB SQL query to find the total sales amounts for each product category, pivoted by hour?
SELECT 
    EXTRACT(hour FROM CAST(timestamp AS TIMESTAMP)) AS hour,
    COALESCE(SUM(CASE WHEN category = 'Electronics' THEN amount END), 0) AS Electronics,
    COALESCE(SUM(CASE WHEN category = 'Home Goods' THEN amount END), 0) AS "Home Goods",
    COALESCE(SUM(CASE WHEN category = 'Clothing' THEN amount END), 0) AS Clothing
FROM sales
GROUP BY hour
ORDER BY hour;

Correct
We compare your response to the expected result by rounding the values to the nearest integer.

6 Move and rename files (1 mark)
Download  and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.

What does running grep . * | LC_ALL=C sort | sha256sum in bash on that folder show?
a7ee7df8d4d4adb2364a81a398014f7e61ac30dcd70772686a3fb43bf2e3d5eb
Correct
7 LLM Embeddings (1 mark)
SecurePay, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.

Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized verification message to the user's registered email address. This message includes the user's email address and a unique transaction code (a randomly generated number). Here are 2 verification messages:

Dear user, please verify your transaction code 52951 sent to roe-24f2006438@ds.study.iitm.ac.in
Dear user, please verify your transaction code 62289 sent to roe-24f2006438@ds.study.iitm.ac.in
The goal is to capture this message, convert it into a meaningful embedding using OpenAI's text-embedding-3-small model, and subsequently use the embedding in a machine learning model to detect anomalies.

Your task is to write the JSON body for a POST request that will be sent to the OpenAI API endpoint to obtain the text embedding for the 2 given personalized transaction verification messages above. This will be sent to the endpoint https://api.openai.com/v1/embeddings.

Write your JSON body here:
{
  "model": "text-embedding-3-small",
  "input": [
    "Dear user, please verify your transaction code 52951 sent to roe-24f2006438@ds.study.iitm.ac.in",
    "Dear user, please verify your transaction code 62289 sent to roe-24f2006438@ds.study.iitm.ac.in"
  ],
  "encoding_format": "float"
}

Correct
8 Region Containing Point (1 mark)
You are the operations manager for World Courier. You have divided your business across 62 franchisees, giving each a region. All couriers from inside the franchisee's region must be picked up by that franchisee.

You have new requests from these latitudes and longitudes:

Latitude	Longitude
38.4061	-66.7802
16.9363	79.0236
-2.9329	39.6476
-29.2223	-4.5716
38.9693	-7.3672
Here are the franchisee numbers and the cities that mark their region's boundary.
Any point inside a region is served by the corresponding franchisee.

Assume the Earth is flat.

Write the answer as a sequence of franchisee numbers separated by commas (e.g. "20,9,12,12,3").

Incorrect. Try again.
The franchisee numbers should be in the order of the pickup points. We strip spaces around the commas or franchisee numbers before checking. It's OK if multiple points fall into the same franchisee region.

9 Shortest Path Between Cities (1 mark)
You are the operations manager for World Courier. You are trying to find the shortest path between Accra and Vienna.

World Courier has a fleet of aircraft that can fly directly between specific cities. The distance between two cities is the Haversine distance.

What is the sequence of cities that you should fly to minimize the total distance traveled?

Here are the flight connections between cities provided by World Courier:
Here is a list of cities with their latitude and longitude.
Write the answer as a sequence of cities separated by commas.

Accra,Lagos,Nairobi,Addis Ababa,Zurich,Vienna
Error: Incorrect. Hint: There are 7 cities in the shortest path.
The cities should be in the order you would fly them. We strip spaces around the commas or city names before checking.

10 Calculate correlation (1 mark)
Download  . It contains an array of objects, each with 2 numerical columns: A and B.

What is the Pearson correlation coefficient between columns A and B?
