# Data Engineering Project: Sports Analytics

## Project Overview

This project is part of a personal data engineering side project focusing on sports analytics, with an initial focus on football data collection. The goal is to develop a comprehensive data pipeline that fetches, processes, and analyzes sports data, starting with fetching upcoming matches for F.C. Barcelona from a REST API.

### Current Features

- **Fetch Upcoming Matches**: A Python script (`fc_barcelona_matches.py`) that uses the REST API from [football-data.org] to fetch upcoming matches for F.C. Barcelona and dumps the data into a CSV file for further analysis.

### Future Scope

- **Data Collection Expansion**: Expand the data collection to include detailed team stats, player performance stats, and historical match data.
- **Data Storage**: Migrate data storage from CSV files to cloud data warehouses like Snowflake or BigQuery for scalable storage and advanced analysis.
- **Data Processing and Analysis**: Implement SQL queries and aggregations to analyze collected data, focusing on insights like player performance trends, team statistics, and predictive analytics.
- **Automation**: Develop an Airflow pipeline using an Astronomer account to automate the data ingestion and processing workflow.
- **Data Visualization**: Connect the data warehouse to a visualization tool like Looker to create dynamic charts and dashboards that showcase the analysis results.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library for API calls
-  An API key from [football-data.org](https://www.football-data.org/)

### Installation

1. Clone the repository to your local machine: https://github.com/borjadam/football-data
2. Install required Python packages: pip install -r requirements.txt


### Usage

To fetch upcoming matches for F.C. Barcelona, run: python fc_barcelona_matches.py

## Roadmap

- [x] Fetch upcoming matches for F.C. Barcelona
- [ ] Expand data collection to other teams and players
- [ ] Migrate data storage to Snowflake/BigQuery
- [ ] Implement data processing and analysis in SQL
- [ ] Set up data ingestion automation with Airflow
- [ ] Create dynamic visualizations with Looker

## Acknowledgments

- Football-data.org for providing the sports data API
