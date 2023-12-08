#Heart Disease Prediction: Data ingestion Pipeline
from src.Breast_Cancer_Prediction.components.Data_ingestion import DataIngestion
obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()

# Data Transformation Pipeline
from src.Breast_Cancer_Prediction.components.Data_transformation import DataTransformation
data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)