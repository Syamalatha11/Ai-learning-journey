# ============================================
# DAY 2 - COMPLETE PANDAS GUIDE FOR BEGINNERS
# By Syamalatha | AI-Learning-Journey
# ============================================

import pandas as pd
import numpy as np

# ----------------------------------------
# PART 1 - WHAT IS PANDAS?
# ----------------------------------------
# Pandas = Panel Data
# It helps us work with TABLES (like Excel!)
# Used in ALL AI and ML projects!
# Two main things: Series and DataFrame

print("=" * 40)
print("PART 1 - SERIES (Single Column)")
print("=" * 40)

# Series = single column of data
marks = pd.Series([85, 90, 78, 92, 88])
print("Student marks:")
print(marks)

# Series with names as index
students = pd.Series([85, 90, 78, 92, 88],
                     index=["Syama", "Priya", "Ravi", "Anjali", "Kumar"])
print("\nMarks with names:")
print(students)

# Get one student's mark
print("\nSyama's mark:", students["Syama"])

# ----------------------------------------
# PART 2 - DATAFRAME (Full Table)
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 2 - DATAFRAME (Full Table)")
print("=" * 40)

# DataFrame = full table with rows and columns
# Like an Excel sheet!

data = {
    "Name":    ["Syama", "Priya", "Ravi", "Anjali", "Kumar"],
    "Age":     [20, 21, 19, 22, 20],
    "Marks":   [85, 90, 78, 92, 88],
    "City":    ["Chennai", "Mumbai", "Delhi", "Pune", "Hyderabad"],
    "Passed":  [True, True, True, True, True]
}

df = pd.DataFrame(data)
print("Student Table:")
print(df)

# ----------------------------------------
# PART 3 - BASIC INFO
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 3 - TABLE INFORMATION")
print("=" * 40)

print("Shape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nFirst 3 rows:")
print(df.head(3))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nQuick summary:")
print(df.describe())

# ----------------------------------------
# PART 4 - GETTING DATA
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 4 - GETTING DATA")
print("=" * 40)

# Get one column
print("All names:")
print(df["Name"])

# Get multiple columns
print("\nNames and Marks:")
print(df[["Name", "Marks"]])

# Get one row by index number
print("\nFirst student (row 0):")
print(df.iloc[0])

# Get specific row and column
print("\nSecond student's city:", df.iloc[1]["City"])

# Get row by condition
print("\nStudents with marks above 85:")
print(df[df["Marks"] > 85])

# ----------------------------------------
# PART 5 - FILTERING DATA
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 5 - FILTERING DATA")
print("=" * 40)

# Students from specific city
print("Students from Chennai:")
print(df[df["City"] == "Chennai"])

# Students with marks between 80 and 90
print("\nMarks between 80-90:")
print(df[(df["Marks"] >= 80) & (df["Marks"] <= 90)])

# Students older than 20
print("\nAge above 20:")
print(df[df["Age"] > 20])

# ----------------------------------------
# PART 6 - ADDING DATA
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 6 - ADDING DATA")
print("=" * 40)

# Add a new column
df["Grade"] = ["A", "A+", "B+", "A+", "A"]
print("Added Grade column:")
print(df)

# Add calculated column
df["Marks_Out_50"] = df["Marks"] / 2
print("\nAdded Marks out of 50:")
print(df[["Name", "Marks", "Marks_Out_50"]])

# ----------------------------------------
# PART 7 - SORTING DATA
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 7 - SORTING DATA")
print("=" * 40)

# Sort by marks (highest first)
sorted_df = df.sort_values("Marks", ascending=False)
print("Sorted by marks (highest first):")
print(sorted_df[["Name", "Marks"]])

# Sort by name alphabetically
alpha_df = df.sort_values("Name")
print("\nSorted alphabetically:")
print(alpha_df[["Name", "Marks"]])

# ----------------------------------------
# PART 8 - STATISTICS
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 8 - STATISTICS")
print("=" * 40)

print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())
print("Total marks:", df["Marks"].sum())
print("Median marks:", df["Marks"].median())

# Count students per city
print("\nStudents per city:")
print(df["City"].value_counts())

# ----------------------------------------
# PART 9 - HANDLING MISSING DATA
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 9 - MISSING DATA")
print("=" * 40)

# Create data with missing values
data2 = {
    "Name":  ["A", "B", "C", "D", "E"],
    "Score": [85, None, 78, None, 88],
    "Age":   [20, 21, None, 22, 20]
}
df2 = pd.DataFrame(data2)
print("Data with missing values:")
print(df2)

# Check missing values
print("\nMissing values count:")
print(df2.isnull().sum())

# Fill missing values with average
df2["Score"] = df2["Score"].fillna(df2["Score"].mean())
print("\nAfter filling missing scores with average:")
print(df2)

# Drop rows with any missing values
df2_clean = df2.dropna()
print("\nAfter dropping missing rows:")
print(df2_clean)

# ----------------------------------------
# PART 10 - GROUPBY
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 10 - GROUPBY (Group Data)")
print("=" * 40)

data3 = {
    "Name":       ["Syama", "Priya", "Ravi", "Anjali", "Kumar", "Deepa"],
    "Department": ["CS", "IT", "CS", "IT", "CS", "IT"],
    "Marks":      [85, 90, 78, 92, 88, 76]
}
df3 = pd.DataFrame(data3)
print("Student data:")
print(df3)

# Average marks per department
print("\nAverage marks per department:")
print(df3.groupby("Department")["Marks"].mean())

# Count students per department
print("\nStudents per department:")
print(df3.groupby("Department")["Name"].count())

# ----------------------------------------
# PART 11 - WHY PANDAS IN AI?
# ----------------------------------------
print("\n" + "=" * 40)
print("PART 11 - PANDAS IN AI")
print("=" * 40)

# In AI, we use Pandas to:
# 1. Load datasets
# 2. Clean data (remove nulls)
# 3. Explore data (EDA)
# 4. Prepare data for ML models

# Example: AI dataset preparation
ai_data = {
    "Feature1": [1.2, 2.3, None, 4.5, 5.6],
    "Feature2": [10, 20, 30, None, 50],
    "Label":    [0, 1, 0, 1, 1]
}
ai_df = pd.DataFrame(ai_data)
print("Raw AI dataset:")
print(ai_df)

# Clean it for AI
ai_df = ai_df.fillna(ai_df.mean())
print("\nCleaned AI dataset (ready for ML!):")
print(ai_df)

print("\n" + "=" * 40)
print("DAY 2 COMPLETE! Great job!")
print("Tomorrow: Matplotlib (Graphs!)")
print("=" * 40)
