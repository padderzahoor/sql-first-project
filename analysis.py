try:
	import matplotlib.pyplot as plt
except ImportError:
	print("matplotlib is not installed. Please install it using 'pip install matplotlib'.")
	exit(1)
try:
	import seaborn as sns
except ImportError:
	print("Seaborn is not installed. Please install it using 'pip install seaborn'.")
	exit(1)
import sqlite3
import pandas as pd
# Load dataset
df = pd.read_csv("students.csv")
print('Head of the DataFrame:')
print(df.head())

conn = sqlite3.connect("students.db")
df.to_sql("students", conn, if_exists="replace", index=False)


query_1 = """
-- 1. Explore the table 
SELECT * 
FROM students;
"""

df2 = pd.read_sql(query_1, conn)
print('Data from students table:')
print(df)

query_2 = """
--2.  Count the number of international and domestic students
select inter_dom, count(*)
from Students
group by inter_dom;
"""
df3 = pd.read_sql(query_2, conn)
print('Count of international and domestic students:')
print(df3)

query_3 = """
--3.  Calculate minimum, maximum, and average of all the test scores for the entire data set
select min(todep) as min_phq, max(todep) as max_phq, round(avg(todep), 2) as avg_phq,
	min(tosc) as min_scs, max(tosc) as max_scs, round(avg(tosc), 2) as avg_scs, 
	min(toas) as min_asiss, max(toas) as max_asiss, round(avg(toas), 2) as avg_asiss
from Students;
"""
df4 = pd.read_sql(query_3, conn)
print('Test scores statistics for the entire dataset:')
print(df4)

query_4 ="""
--4.  Calculate minimum, maximum, and average of all the test scores for international students
select min(todep) as min_phq, max(todep) as max_phq, round(avg(todep), 2) as avg_phq,
	min(tosc) as min_scs, max(tosc) as max_scs, round(avg(tosc), 2) as avg_scs, 
	min(toas) as min_asiss, max(toas) as max_asiss, round(avg(toas), 2) as avg_asiss
from Students
where inter_dom = 'Inter';
"""
df5 = pd.read_sql(query_4, conn)
print('Test scores statistics for international students:')
print(df5)

query_5 = """
--5.  For international students, list the length of stay in descending order
select inter_dom, stay
from students
where inter_dom = 'Inter'
order by stay desc;
"""
df6 = pd.read_sql(query_5, conn)
print('Length of stay for international students in descending order:')
print(df6)

query_6 = """
--6.  For international students, count the number of students for each length of stay and calculate the average of each test score for each length of stay
select stay, count(inter_dom) as count_int, round(avg(todep), 2) as average_phq,
	round(avg(tosc), 2) as average_scs, 
	round(avg(toas), 2) as average_as
from students
where inter_dom = 'Inter'
group by stay, inter_dom
order by stay desc;
"""
df7 = pd.read_sql(query_6, conn)
print('Count and average test scores for international students by length of stay:')
print(df7)
conn.close()

# Visualization of mental health trends by length of stay for international students

# dataframe is named df7
plt.figure(figsize=(10, 6))

# Plotting each metric
sns.lineplot(data=df7, x='stay', y='average_phq', marker='o', label='Depression (PHQ-9)')
sns.lineplot(data=df7, x='stay', y='average_scs', marker='s', label='Social Connectedness (SCS)')
sns.lineplot(data=df7, x='stay', y='average_as', marker='D', label='Acculturative Stress (ASISS)')

plt.title('Mental Health Trends by Length of Stay', fontsize=15)
plt.xlabel('Length of Stay (Years)', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df7.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Mental Health Variables')
plt.show()
