# Setting up a data lake for financial data visualization using Apache Kafka, Apache Spark, Apache Beam, Apache Druid, and Streamlit

## OverView
This project aims to establish a data lake for visualizing financial data using Apache Spark, Apache Beam, Apache Druid, and Streamlit. Two data sources, namely Yahoo Finance and the New York Times API, are integrated through Apache Beam and stored in Parquet format. Using Spark ML, multiple sentiment analysis models are trained on a Kaggle dataset, and the best model is selected. The data is then analyzed with Spark SQL to predict NYT sentiment scores, and the result is stored in Apache Druid. Finally, Streamlit provides an interactive interface for exploring the results, including the data table and daily sentiment statistics, etc.



