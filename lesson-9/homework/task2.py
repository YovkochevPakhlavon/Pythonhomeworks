import csv
from collections import defaultdict

# Step 1: Create 'grades.csv' (if not already created)
grades_data = [
    ["Name", "Subject", "Grade"],
    ["Alice", "Math", 85],
    ["Bob", "Science", 78],
    ["Carol", "Math", 92],
    ["Dave", "History", 74]
]

with open("grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)

print("grades.csv created successfully!\n")

# Step 2: Read 'grades.csv' and store data
grades = []
with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  # Convert grade to integer
        grades.append(row)

# Step 3: Calculate average grade per subject
subject_totals = defaultdict(lambda: {"total": 0, "count": 0})

for row in grades:
    subject = row["Subject"]
    grade = row["Grade"]
    subject_totals[subject]["total"] += grade
    subject_totals[subject]["count"] += 1

average_grades = {
    subject: totals["total"] / totals["count"]
    for subject, totals in subject_totals.items()
}

# Step 4: Write results to 'average_grades.csv'
with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, round(avg_grade, 1)])  # Round to 1 decimal place

print("average_grades.csv created successfully!")