#Heart Disease Prediction: Data ingestion Pipeline
from src.Heart_Disease_Prediction.components.Data_ingestion import DataIngestion
obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()