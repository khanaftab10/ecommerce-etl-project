from extract import extract_data
from transform import transform_data
from load import load_data


file_path = "D:\ecommerce-etl-project\data\SampleSuperstore.csv"

# Extract
raw_data = extract_data(file_path)

# Transform
clean_data = transform_data(raw_data)

# Load
load_data(clean_data)

print('ETL Pipeline Completed Successfully!')