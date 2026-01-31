import sqlite3
import pandas as pd

conn = sqlite3.connect("students.db")

query = """
-- 1. Explore the table 
SELECT * 
FROM students;

--2.  Count the number of international and domestic students
select inter_dom, count(*)
from Students
group by inter_dom;

--3.  Calculate minimum, maximum, and average of all the test scores for the entire data set
select min(todep) as min_phq, max(todep) as max_phq, round(avg(todep), 2) as avg_phq,
	min(tosc) as min_scs, max(tosc) as max_scs, round(avg(tosc), 2) as avg_scs, 
	min(toas) as min_asiss, max(toas) as max_asiss, round(avg(toas), 2) as avg_asiss
from Students;

--4.  Calculate minimum, maximum, and average of all the test scores for international students
select min(todep) as min_phq, max(todep) as max_phq, round(avg(todep), 2) as avg_phq,
	min(tosc) as min_scs, max(tosc) as max_scs, round(avg(tosc), 2) as avg_scs, 
	min(toas) as min_asiss, max(toas) as max_asiss, round(avg(toas), 2) as avg_asiss
from Students
where inter_dom = 'Inter';

--5.  For international students, list the length of stay in descending order
select inter_dom, stay
from students
where inter_dom = 'Inter'
order by stay desc;


--6.  For international students, count the number of students for each length of stay and calculate the average of each test score for each length of stay
select stay, count(inter_dom) as count_int, round(avg(todep), 2) as average_phq,
	round(avg(tosc), 2) as average_scs, 
	round(avg(toas), 2) as average_as
from students
where inter_dom = 'Inter'
group by stay, inter_dom
order by stay desc;
"""

df = pd.read_sql(query, conn)
print(df)

conn.close()
