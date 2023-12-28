# Setting up a data lake for financial data visualization using Apache Kafka, Apache Spark, Apache Beam, Apache Druid, and Streamlit

## OverView
This project aims to establish a data lake for visualizing financial data using Apache Spark, Apache Beam, Apache Druid, and Streamlit. Two data sources, namely Yahoo Finance and the New York Times API, are integrated through Apache Beam and stored in Parquet format. Using Spark ML, multiple sentiment analysis models are trained on a Kaggle dataset, and the best model is selected. The data is then analyzed with Spark SQL to predict NYT sentiment scores, and the result is stored in Apache Druid. Finally, Streamlit provides an interactive interface for exploring the results, including the data table and daily sentiment statistics, etc.

## Prerequisites
Before getting started, ensure your environment meets the following requirements:
-  Operating System: Compatible with Docker and necessary tools.
-  RAM: Minimum of 13 GB.
-  Docker: Installed and verified.
-  Docker Compose: Installed and verified.
## System Architecture
System Architecture
:------------:
![architecture projet](https://github.com/ElmansouriAMINE/MOROCCO-MONUMENTS-LOCATION-IDENTIFYING/assets/101812229/902de86a-66ed-4163-b1fa-d0581ce81f3a)
### 1.  Intercepting data from the 2 APIs using Apache Beam:
We use Apache Beam to create a data processing pipeline. It defines two data schemas, one for New York Times news articles and the other for financial information from Yahoo Finance, using the PyArrow library. The pipeline aims to retrieve article data via HTTP requests, as well as financial data from Yahoo Finance, and process them simultaneously. The schemas specify the data structure to ensure consistency during parallel processing in the Apache Beam pipeline.

### 2.  Saving raw data in Parquet format:
The results of the Beam pipeline execution are written to Parquet files with explicit schemas for both New York Times and Yahoo Finance data.

### 3.  Training multiple ML models for sentiment analysis:
Multiple sentiment analysis models are trained using Spark ML on a Zeppelin notebook, and the best model is saved in HDFS.

### 4.  Reading saved data with Spark SQL.

### 5.  Predicting sentiment scores of texts using Spark ML:
A pre-trained model is used to predict sentiment labels from a text column in a New York Times DataFrame. The results are then filtered and displayed.

### 6.  Adding new columns to NYT data:
Analyzing New York Times sentiment data by truncating abstracts, calculating the total number of abstracts, and the average sentiment per day, providing an overall summary of daily statistics, and displaying results sorted by date.

### 7.  Saving the new DataFrame obtained in Apache Druid

### 8.  Visualizing the processing result using Streamlit


## Running the Project
### Clone the Repository
```bash
# Clone the repository from GitHub
git clone https://github.com/ElmansouriAMINE/mise-en-place-d-un-data-lake-master.git

cd mise-en-place-d-un-data-lake-master
```
### Start the Project with Docker Compose
```bash
# Make sure to be in the project directory
cd mise-en-place-d-un-data-lake-master

# Start the services in the background with Docker Compose
docker-compose up -d
```

## Contributors
-  #### AMINE ELMANSOURI
-  #### CHARAFEDDINE ELBAHJA
-  #### YASSINE HASSINI

