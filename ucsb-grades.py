#ucsb-grades.py

import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect("ucsb_easy.db")
cursor = conn.cursor()

# Drop existing tables 
cursor.execute("DROP TABLE IF EXISTS grades")

# Create grades table 
cursor.execute("""
CREATE TABLE grades (
    student_id INTEGER,
    course_code TEXT,
    quarter TEXT,
    grade TEXT
)
""")

conn.commit() # Save changes

# Insert sample data into grades table 
cursor.executemany("""
INSERT INTO grades
(student_id, course_code, quarter, grade)
VALUES (?,?,?,?)
""", [
    (1, "CMPSC 16", "F2023", "A"),
    (2, 'CMPSC 16', 'F2023', 'A-'),
    (3, 'CMPSC 16', 'F2023', 'B+'),
    (4, 'PSTAT 131', 'F2023', 'A'),
    (5, 'PSTAT 131', 'F2023', 'B'),
    (6, 'MATH 4A', 'F2023', 'C+'),
    (7, 'MATH 4A', 'F2023', 'B-'),
    (8, 'ECON 10A', 'F2023', 'B+')
])

conn.commit() # Save changes

# Display all grades
print("\nAll Grades:")
for row in cursor.execute("SELECT * FROM grades"):
    print(row)

# Query grades for CMPSC 16 course
print("\nOnly CMPSC 16:")
for row in cursor.execute("""
SELECT * FROM grades
WHERE course_code = "CMPSC 16"
"""):
    print(row)

# Count number of students per course
print("\nNumber of students per course:")
for row in cursor.execute("""
SELECT
    course_code,
    COUNT(*) AS num_students
FROM grades
GROUP BY course_code
"""):
    print(row)

# Sort courses by enrollment
print("\nCourses sorted by enrollment:")
for row in cursor.execute("""
SELECT
    course_code,
    COUNT(*) AS num_students
FROM grades
GROUP BY course_code
ORDER BY num_students DESC
"""):
    print(row)

conn.close() # Close database connection
