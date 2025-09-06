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
├── data.xlsx                     # Structural dataset (district level)
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

These are the variables already grouped by themes: 

**1. General Information**
Land
District
Name
Municipalities
Area in km²

**2. Population Dynamics**
Population on 31.12.2022 – Total (in 1000)
Population on 31.12.2022 – German (in 1000)
Population on 31.12.2022 – Foreigners (%)
Population density on 31.12.2022 (inhabitants per km²)
Birth balance 2022 (per 1000 inhabitants)
Migration balance 2022 (per 1000 inhabitants)

**3. Age Structure (as of 31.12.2022)**
Under 16 years (%)
16–17 years (%)
18–24 years (%)
25–34 years (%)
35–59 years (%)
60–74 years (%)
75 years and over (%)

**4. Land Use and Housing**
Land use – Settlement and traffic (%)
Land use – Vegetation and water (%)
Completed dwellings in 2021 (per 1000 inhabitants)
Stock of dwellings on 31.12.2021 (per 1000 inhabitants)
Residential space on 31.12.2021 (per dwelling)
Residential space on 31.12.2021 (per inhabitant)

**5. Mobility**
Car stock on 01.01.2023 – Total cars (per 1000 inhabitants)
Car stock on 01.01.2023 – Cars with electric or hybrid drive (%)

**6. Economy and Employment**

**6.1 Business Activity**
Total companies (per 1000 inhabitants)
Craft enterprises (per 1000 inhabitants)
Disposable income of private households in 2021 (EUR per inhabitant)
Gross domestic product in 2021 (EUR per inhabitant)

**6.2 Social Insurance Contributions (as of 30.06.2023)**
Total (per 1000 inhabitants)

By Industry Share (%):
Agriculture, forestry, fishing
Manufacturing industry
Trade, hospitality, transport
Public and private service providers
Other service providers and “unspecified”

**7. Education and Childcare**

**7.1 School Graduates (2022)**
Vocational schools (per 1000 inhabitants)
General education schools – total excl. external candidates (per 1000 inhabitants)
General education schools – without a secondary school certificate (%)
General education schools – with a secondary school certificate (%)
General education schools – with an intermediate school certificate (%)
General education schools – with general or subject-specific higher education entrance qualification (%)

**7.2 Childcare (as of 01.03.2023)**
Children under 3 years – care rate (%)
Children aged 3 to under 6 years – care rate (%)

**8. Social Welfare and Labor Market**

**8.1 Social Benefits (August 2023)**
Recipients of benefits under SGB II – total (per 1000 inhabitants)
Recipients of benefits under SGB II – Non-working individuals in need (%)
Recipients of benefits under SGB II – Foreigners (%)

**8.2 Unemployment (October 2023)**
Unemployment rate – Total
Unemployment rate – Men
Unemployment rate – Women
Unemployment rate – 15 to 24 years
Unemployment rate – 55 to 64 years

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
