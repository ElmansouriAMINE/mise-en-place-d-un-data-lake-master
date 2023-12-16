import apache_beam as beam
import requests
import yfinance as yf
from pyarrow import schema
from apache_beam.options.pipeline_options import PipelineOptions
from hdfs import InsecureClient
from apache_beam.io.filesystems import FileSystems
from apache_beam.io.hadoopfilesystem import HadoopFileSystemOptions, HadoopFileSystem

# Define the Parquet schema using pyarrow schema
article_schema = schema([
    ('title', 'utf8'),
    ('abstract', 'utf8'),
    ('item_type', 'utf8'),
    ('source', 'utf8'),
    ('updated_date', 'utf8'),
    ('created_date', 'utf8'),
    ('published_date', 'utf8'),
    ('first_published_date', 'utf8'),
    ('material_type_facet', 'utf8'),
    ('kicker', 'utf8'),
    ('subheadline', 'utf8')
])

# Define schema for Yahoo Finance data
yahoo_finance_schema = schema([
    ('Date', 'utf8'),
    ('Open', 'double'),
    ('High', 'double'),
    ('Low', 'double'),
    ('Close', 'double'),
    ('Adj Close', 'double'),
    ('Volume', 'double')
])

class NYTAPIClient(beam.DoFn):
    def process(self, element):
        api_url = "https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=47Ecm6QPRMxjyIz8EmyD6g2agAiXMTKJ"
        response = requests.get(api_url)
        api_response = response.json()
        if 'results' in api_response:
            yield api_response['results']

class YahooFinanceAPIClient(beam.DoFn):
    def process(self, element):
        stock_data = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
        for date, record in stock_data.iterrows():
            record_dict = record.to_dict()
            record_dict['Date'] = date.strftime('%Y-%m-%d')
            yield record_dict

def process_article(articles):
    selected_fields_list = []
    for article in articles:
        selected_fields = {
            'title': article.get('title', ''),
            'abstract': article.get('abstract', ''),
            'item_type': article.get('item_type', ''),
            'source': article.get('source', ''),
            'updated_date': article.get('updated_date', ''),
            'created_date': article.get('created_date', ''),
            'published_date': article.get('published_date', ''),
            'first_published_date': article.get('first_published_date', ''),
            'material_type_facet': article.get('material_type_facet', ''),
            'kicker': article.get('kicker', ''),
            'subheadline': article.get('subheadline', '')
        }
        selected_fields_list.append(selected_fields)

    return selected_fields_list

# Output paths in HDFS
output_path_nyt = "./test2/nyt"
output_path_yahoo = "./test2/yh"
# Apache Beam Pipeline Options
options = PipelineOptions()
options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'DirectRunner'

# HDFS Client Setup
hdfs_namenode_host = 'localhost'  # Replace with the actual hostname or IP address of your NameNode
hdfs_namenode_port = 9870  # Port du NameNode
hdfs_client = InsecureClient(f'http://{hdfs_namenode_host}:{hdfs_namenode_port}')

with beam.Pipeline(options=options) as pipeline:
    nyt_data = (
        pipeline
        | "Create URL NYT" >> beam.Create([None])
        | "Get NYT Data" >> beam.ParDo(NYTAPIClient())
        | "Process NYT Articles" >> beam.FlatMap(lambda result: process_article(result))
    )

    yahoo_data = (
        pipeline
        | "Create URL Yahoo" >> beam.Create([None])
        | "Get Yahoo Finance Data" >> beam.ParDo(YahooFinanceAPIClient())
    )

    # Debugging: Print the data before writing to Parquet
    nyt_data | "Debug Print NYT" >> beam.Map(print)
    yahoo_data | "Debug Print Yahoo" >> beam.Map(print)

    # Write data to Parquet with explicit schema
    nyt_data | "Write NYT Data to Parquet" >> beam.io.WriteToParquet(
        file_path_prefix=output_path_nyt,
        file_name_suffix=".parquet",
        num_shards=1,
        schema=article_schema
    )

    yahoo_data | "Write Yahoo Finance Data to Parquet" >> beam.io.WriteToParquet(
        file_path_prefix=output_path_yahoo,
        file_name_suffix=".parquet",
        num_shards=1,
        schema=yahoo_finance_schema
    )

# try:
#     # Copie du fichier nyt_data.parquet vers HDFS
#     hdfs_client.upload(hdfs_path=output_path_nyt, local_path='nyt_data.parquet', overwrite=True)
#     # Upload the yh_data.parquet file to HDFS
#     hdfs_client.upload(hdfs_path=output_path_yahoo, local_path='yh_data.parquet', overwrite=True)

#     print("Copie des fichiers vers HDFS réussie.")
# except Exception as e:
#     print(f"Erreur lors de la copie vers HDFS : {e}")

# print("Notre Beam Pipeline a été exécuté avec succès.")

