# Automated Crypto & Market Data Intelligence Pipeline

An automated ETL and data warehousing pipeline that extracts cryptocurrency market data from the CoinGecko API, processes it using Python and SSIS, and loads it into a SQL Server data warehouse.

## Project Objective

To build an automated and reliable data pipeline that collects cryptocurrency market data, validates and transforms it, stores it in a structured SQL Server data warehouse, and automatically refreshes the data daily.

## Architecture

CoinGecko API
↓
Python + Pandas
↓
CSV Staging
↓
SSIS ETL
↓
SQL Server Data Warehouse
↓
SSISDB
↓
DTExec
↓
Windows Task Scheduler

## Technologies Used

- Python
- Pandas
- REST API
- SQL Server
- SSIS
- SSISDB
- SQL Server Management Studio
- DTExec
- Windows Task Scheduler

## Key Features

- Automated cryptocurrency data extraction
- CSV staging layer
- Data cleaning and type conversion
- Data validation
- SSIS Lookup transformations
- Incremental dimension loading
- Surrogate key implementation
- Fact and dimension tables
- Rejected-row handling
- ETL execution logging
- Error capture using SSIS Event Handlers
- Parameterized SSIS package
- Daily automated execution

## Data Warehouse

### Dim_Coin

Stores cryptocurrency master information.

- CoinKey
- CoinID
- Symbol
- CoinName

### Fact_MarketMetrics

Stores cryptocurrency market metrics.

- MetricID
- CoinKey
- CurrentPrice
- MarketCap
- TotalVolume
- PriceChange24h
- LoadDate

## ETL Logging

The pipeline maintains an `ETL_RunLog` table containing:

- Run ID
- Start and end time
- Execution status
- Source row count
- Dimension rows inserted
- Fact rows inserted
- Rejected rows
- Error messages

Rejected records are stored separately in `ETL_RejectedRows` with the reason for rejection.

## Automation

The deployed SSIS package is executed using `DTExec` and scheduled through Windows Task Scheduler to run automatically on a daily basis.

## Result

The pipeline successfully processes 50 cryptocurrency records per run with validation, logging, lookup-based dimension loading, and automated SQL Server loading.

## Future Improvements

- Power BI dashboard for market analysis
- Historical price trend analysis
- Additional market indicators
- Data quality monitoring dashboard
- Cloud deployment
