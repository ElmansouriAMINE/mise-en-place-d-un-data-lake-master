from hdfs import InsecureClient

# Replace with the actual hostname or IP address of your NameNode
hdfs_namenode_host = 'localhost'
hdfs_namenode_port = 9870
hdfs_client = InsecureClient(f'http://{hdfs_namenode_host}:{hdfs_namenode_port}')

# Example: List the contents of the root directory
try:
    content = hdfs_client.list('/user/inputs')
    print("Contents of the root directory:")
    for item in content:
        print(item)
except Exception as e:
    print(f"Error: {e}")



local_file_path = './data/rt.txt'
hdfs_file_path = '/user/text.txt'

# try:
#     with open(local_file_path, 'rb') as local_file:
#         hdfs_client.write(hdfs_file_path, local_file)
#     print(f"File {local_file_path} uploaded to HDFS at {hdfs_file_path}")
# except Exception as e:
#     print(f"Error: {e}")



# this code is working in zeppelin

# from hdfs import InsecureClient

# # Replace with the actual hostname or IP address of your NameNode
# hdfs_namenode_host = 'localhost'
# hdfs_namenode_port = 9870
# hdfs_client = InsecureClient(f'http://{hdfs_namenode_host}:{hdfs_namenode_port}')

# # Example: List the contents of the root directory
# try:
#     content = hdfs_client.list('/user/')
#     print("Contents of the root directory:")
#     for item in content:
#         print(item)
# except Exception as e:
#     print(f"Error: {e}")



# local_file_path = '/opt/zeppelin/rt.txt'
# hdfs_file_path = '/user/text2.txt'

# try:
#     with open(local_file_path, 'rb') as local_file:
#         hdfs_client.write(hdfs_file_path, local_file)
#     print(f"File {local_file_path} uploaded to HDFS at {hdfs_file_path}")
# except Exception as e:
#     print(f"Error: {e}")