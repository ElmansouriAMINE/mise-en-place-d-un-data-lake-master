# Setting up a data lake for financial data visualization using Apache Kafka, Apache Spark, Apache Beam, Apache Druid, and Streamlit

## OverView
This project aims to establish a data lake for visualizing financial data using Apache Spark, Apache Beam, Apache Druid, and Streamlit. Two data sources, namely Yahoo Finance and the New York Times API, are integrated through Apache Beam and stored in Parquet format. Using Spark ML, multiple sentiment analysis models are trained on a Kaggle dataset, and the best model is selected. The data is then analyzed with Spark SQL to predict NYT sentiment scores, and the result is stored in Apache Druid. Finally, Streamlit provides an interactive interface for exploring the results, including the data table and daily sentiment statistics, etc.

## Prerequisites
Before getting started, ensure your environment meets the following requirements:
-  Operating System: Compatible with Docker and necessary tools.
-  RAM: Minimum of 13 GB.
-  Docker: Installed and verified.
-  Docker Compose: Installed and verified.

## Getting Started
### Clone the Repository
```bash
# Clone the repository from GitHub
git clone https://github.com/ElmansouriAMINE/mise-en-place-d-un-data-lake-master
cd mise-en-place-d-un-data-lake-master
```
