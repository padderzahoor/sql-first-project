# SQL & Python Data Analysis Project: International Student Mental Health

## Overview

This project demonstrates my foundational skills in SQL and Python for data analysis.
I worked with a real-world survey dataset from a Japanese international university (published in 2019) to explore mental health patterns among international students. Analytical SQL queries were used to examine factors such as social connectedness and acculturative stress, and these queries were executed within a Python/Jupyter environment.

## Objective

- Practice real-world SQL querying using the `students` dataset.
- Understand how SQL integrates with Python for data analysis.
- Develop clean, readable, and reusable analysis scripts to explore relationships between length of stay and mental health scores (depression, social connectedness, and acculturative stress).

## Skills Demonstrated

- **SQL**: `SELECT`, `WHERE` (filtering international students), `GROUP BY`, `ORDER BY`, and aggregate functions such as `AVG` and `ROUND`.
- **Python**: Database connectivity, query execution within Jupyter notebooks, and basic data processing.
- **Data Reasoning**: Analyzing how external factors such as length of stay may relate to psychological metrics.
- **Python**: Database connectivity, SQL execution, basic data processing, and data visualization using Matplotlib.


## Project Structure

- `queries.sql` → Standalone SQL queries used to aggregate and analyze student mental health data.
- `analysis.py` → Python script that executes SQL queries and processes results.

## Dataset

The dataset consists of survey responses collected in 2018 at a Japanese international university. Key fields include:

- `inter_dom`: Student type (International or Domestic)
- `stay`: Length of stay in years
- `todep`: Total depression score (PHQ-9)
- `tosc`: Total social connectedness score (SCS)
- `toas`: Total acculturative stress score (ASISS)

## Key Analysis Performed

- **Filtered Analysis**: Isolated records for international students to focus the analysis on this subgroup.
- **Trend Aggregation**: Calculated average scores for depression, social connectedness, and acculturative stress grouped by length of stay (`stay`).
- **Visualization**: Created basic visualizations to observe relationships between mental health scores and length of stay.
- **Exploratory Assessment**: Examined whether length of stay shows patterns associated with mental health indicators.


## What I Learned

- **Analytical Insight**: Observed how social connectedness and acculturative stress relate to depression scores in the dataset.
- **SQL Structuring**: Learned to structure queries that produce grouped and rounded aggregates for clearer interpretation.
- **Data Translation**: Practiced converting academic survey data into SQL queries to extract interpretable patterns.

## Next Improvements

- Incorporate additional dimensions.
- Optimize queries for scalability on larger datasets.
- Improve and expand visualizations (e.g., clearer trend plots and comparisons across mental health metrics).


