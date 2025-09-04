# Database-and-Techbology
Descriptive analysis 



European Elections 2024 – Structural Data Analysis
📌 Project Overview

This project is part of Assignment 1 for our university course. It is a group work, graded project focusing on a descriptive analysis of structural data at the district level for Germany in the context of the 2024 European elections.

The dataset provided (ew24_structure_data.xlsx) includes demographic, economic, housing, education, and labor market indicators for all districts.
Our goal is to explore patterns, distributions, and relationships across German districts and provide insights into regional structures.

📂 Repository Structure
.
├── AssignmentStarterCode.ipynb   # Provided starter notebook
├── analysis.ipynb                # Our completed descriptive analysis
├── ew24_structure_data.xlsx      # Structural dataset (district level)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation


📊 Analysis Workflow

Data Loading & Cleaning

Read and inspect ew24_structure_data.xlsx.

Handle missing values, rename columns to a consistent format.

Descriptive Statistics

Summary statistics for numeric variables.

Missingness analysis.

Exploratory Analysis by Themes

The variables we have are: 

Land

District

Name

Municipalities

Area (km²)

Population on 31.12.2022 – Total (in 1000)

Population on 31.12.2022 – German (in 1000)

Population on 31.12.2022 – Foreigners (%)

Population density on 31.12.2022 (inhabitants per km²)

Increase (+) or decrease (–) in population in 2022 – Birth balance (per 1000 inhabitants)

Social insurance contributions as of 30.06.2023 – Public and private service providers (%)

Social insurance contributions as of 30.06.2023 – Other service providers and “unspecified” (%)

Recipients of benefits under SGB II in August 2023 – Total (per 1000 inhabitants)

Recipients of benefits under SGB II in August 2023 – Non-working individuals in need (%)

Recipients of benefits under SGB II in August 2023 – Foreigners (%)

Unemployment rate in October 2023 – Total

Unemployment rate in October 2023 – Men

Unemployment rate in October 2023 – Women

Unemployment rate in October 2023 – 15 to 24 years

Unemployment rate in October 2023 – 55 to 64 years

Visualization & Relationships

Histograms, boxplots, scatterplots, heatmaps.

Top/bottom 10 districts for selected indicators.

Correlation matrix to identify relationships.

Findings & Interpretation

Highlight regional differences.

Identify outliers and patterns.

Summarize insights in bullet points.


✅ Evaluation Criteria Addressed

Completeness: All key variables analyzed with descriptive stats & visuals.

Efficiency: Vectorized operations in pandas, no redundant loops.

Robustness: Checks for missing/invalid data, reusable helper functions.

Documentation: Code comments, Markdown explanations, structured workflow.

Argumentation: Logical flow from data → analysis → interpretation.

👥 Group Members

Alens Laskovs

Linus Wössner

[Your Name 3]

📌 License

This repository is created for educational purposes as part of a university assignment.
