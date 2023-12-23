# StreamlitSandbox
A collection of various tools built into a Streamlit app

## Project Management
### I. Portfolio Viewer
1. Prioritization Matrix
1. Connect to Agile Boards, to create consolidated view of Portfolio status
1. Requirements mapping to deliverables & user stories

## Data Engineering
### I. Boilerplate DDL 
1. Create database objects based on configurable patterns
1. Create views based on tables in another db
### II. Migration Toolkit
1. Extract & cleanse metadata from source
1. View of existing job execution pipeline & mapping to new
1. Status for each new job (integration with Agile Boards)
1. Recommendations: TBD

## Data Quality
## Source To Target Validation (SttV)
1. Validate consistency & accuracy of Lake/Raw data vs Source
    - Row hash to ensure accuracy
    - Row modification counts (ins/updt/del)
## Audit, Balance & Control 
Build network of tests to execute, then run tests & display resuls
1. Audit: 
Operational data that records metadata when data was inserted, updated or deleted from tables, so that we know how many rows/cols are changing and compute cost for transformation.
    - Operational Dashboard to show how much data moved & associated costs
    - Do the values conform to expected domain of values?
    - Data Quality Dashboard: Expected Value metrics & exceptions
1. Balance: 
Did we add/lose data when moving from Source to Target, or while transforming & aggregating data in Targe?
    - Do column totals in one table, balance with (subset) of column totals in a another table?
    - 
1. Control: 
How do we recover from failures & data quality issues?

    - Identified issues, root cause analysis, remediation, 
