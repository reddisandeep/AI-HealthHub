import os
from pathlib import Path

list_of_files = [
    ".github/workflows/main.yaml",

    "Notebook_Experiments/Data/.gitkeep",
    "Notebook_Experiments/Heart_Disease_Prediction.ipynb",
    "Notebook_Experiments/Diabetes_Disease_Prediction.ipynb",
    "Notebook_Experiments/Breast_Cancer_Prediction.ipynb",
    "Notebook_Experiments/Skin_Cancer_Prediction.ipynb",
    "Notebook_Experiments/Parkinsons_Disease_Prediction.ipynb",
    "Notebook_Experiments/Brain_Tumor_Detection.ipynb",
    "Notebook_Experiments/Lung_Disease_Prediction.ipynb",
    "Notebook_Experiments/Kidney_Disease_Prediction.ipynb",
    "Notebook_Experiments/Liver_Disease_Prediction.ipynb",
    "Notebook_Experiments/Pneumonia_Prediction.ipynb",
    "Notebook_Experiments/Malaria_Prediction.ipynb",
    "Notebook_Experiments/Ocular_Prediction.ipynb",

    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",

    "src/Heart_Disease_Prediction/components/__init__.py",
    "src/Heart_Disease_Prediction/components/Data_ingestion.py",
    "src/Heart_Disease_Prediction/components/Data_transformation.py",
    "src/Heart_Disease_Prediction/components/Model_trainer.py",
    "src/Heart_Disease_Prediction/components/Model_evaluation.py",
    "src/Heart_Disease_Prediction/pipelines/__init__.py",
    "src/Heart_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Heart_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Diabetes_Disease_Prediction/components/__init__.py",
    "src/Diabetes_Disease_Prediction/components/Data_ingestion.py",
    "src/Diabetes_Disease_Prediction/components/Data_transformation.py",
    "src/Diabetes_Disease_Prediction/components/Model_trainer.py",
    "src/Diabetes_Disease_Prediction/components/Model_evaluation.py",
    "src/Diabetes_Disease_Prediction/pipelines/__init__.py",
    "src/Diabetes_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Diabetes_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Breast_Cancer_Prediction/components/__init__.py",
    "src/Breast_Cancer_Prediction/components/Data_ingestion.py",
    "src/Breast_Cancer_Prediction/components/Data_transformation.py",
    "src/Breast_Cancer_Prediction/components/Model_trainer.py",
    "src/Breast_Cancer_Prediction/components/Model_evaluation.py",
    "src/Breast_Cancer_Prediction/pipelines/__init__.py",
    "src/Breast_Cancer_Prediction/pipelines/Prediction_pipeline.py",
    "src/Breast_Cancer_Prediction/pipelines/Training_pipeline.py",

    "src/Skin_Cancer_Prediction/components/__init__.py",
    "src/Skin_Cancer_Prediction/components/Data_ingestion.py",
    "src/Skin_Cancer_Prediction/components/Data_transformation.py",
    "src/Skin_Cancer_Prediction/components/Model_trainer.py",
    "src/Skin_Cancer_Prediction/components/Model_evaluation.py",
    "src/Skin_Cancer_Prediction/pipelines/__init__.py",
    "src/Skin_Cancer_Prediction/pipelines/Prediction_pipeline.py",
    "src/Skin_Cancer_Prediction/pipelines/Training_pipeline.py",

    "src/Parkinsons_Disease_Prediction/components/__init__.py",
    "src/Parkinsons_Disease_Prediction/components/Data_ingestion.py",
    "src/Parkinsons_Disease_Prediction/components/Data_transformation.py",
    "src/Parkinsons_Disease_Prediction/components/Model_trainer.py",
    "src/Parkinsons_Disease_Prediction/components/Model_evaluation.py",
    "src/Parkinsons_Disease_Prediction/pipelines/__init__.py",
    "src/Parkinsons_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Parkinsons_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Brain_Tumor_Detection/components/__init__.py",
    "src/Brain_Tumor_Detection/components/Data_ingestion.py",
    "src/Brain_Tumor_Detection/components/Data_transformation.py",
    "src/Brain_Tumor_Detection/components/Model_trainer.py",
    "src/Brain_Tumor_Detection/components/Model_evaluation.py",
    "src/Brain_Tumor_Detection/pipelines/__init__.py",
    "src/Brain_Tumor_Detection/pipelines/Prediction_pipeline.py",
    "src/Brain_Tumor_Detection/pipelines/Training_pipeline.py",

    "src/Lung_Disease_Prediction/components/__init__.py",
    "src/Lung_Disease_Prediction/components/Data_ingestion.py",
    "src/Lung_Disease_Prediction/components/Data_transformation.py",
    "src/Lung_Disease_Prediction/components/Model_trainer.py",
    "src/Lung_Disease_Prediction/components/Model_evaluation.py",
    "src/Lung_Disease_Prediction/pipelines/__init__.py",
    "src/Lung_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Lung_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Kidney_Disease_Prediction/components/__init__.py",
    "src/Kidney_Disease_Prediction/components/Data_ingestion.py",
    "src/Kidney_Disease_Prediction/components/Data_transformation.py",
    "src/Kidney_Disease_Prediction/components/Model_trainer.py",
    "src/Kidney_Disease_Prediction/components/Model_evaluation.py",
    "src/Kidney_Disease_Prediction/pipelines/__init__.py",
    "src/Kidney_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Kidney_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Liver_Disease_Prediction/components/__init__.py",
    "src/Liver_Disease_Prediction/components/Data_ingestion.py",
    "src/Liver_Disease_Prediction/components/Data_transformation.py",
    "src/Liver_Disease_Prediction/components/Model_trainer.py",
    "src/Liver_Disease_Prediction/components/Model_evaluation.py",
    "src/Liver_Disease_Prediction/pipelines/__init__.py",
    "src/Liver_Disease_Prediction/pipelines/Prediction_pipeline.py",
    "src/Liver_Disease_Prediction/pipelines/Training_pipeline.py",

    "src/Pneumonia_Prediction/components/__init__.py",
    "src/Pneumonia_Prediction/components/Data_ingestion.py",
    "src/Pneumonia_Prediction/components/Data_transformation.py",
    "src/Pneumonia_Prediction/components/Model_trainer.py",
    "src/Pneumonia_Prediction/components/Model_evaluation.py",
    "src/Pneumonia_Prediction/pipelines/__init__.py",
    "src/Pneumonia_Prediction/pipelines/Prediction_pipeline.py",
    "src/Pneumonia_Prediction/pipelines/Training_pipeline.py",

    "src/Malaria_Prediction/components/__init__.py",
    "src/Malaria_Prediction/components/Data_ingestion.py",
    "src/Malaria_Prediction/components/Data_transformation.py",
    "src/Malaria_Prediction/components/Model_trainer.py",
    "src/Malaria_Prediction/components/Model_evaluation.py",
    "src/Malaria_Prediction/pipelines/__init__.py",
    "src/Malaria_Prediction/pipelines/Prediction_pipeline.py",
    "src/Malaria_Prediction/pipelines/Training_pipeline.py",

    "src/Ocular_Prediction/components/__init__.py",
    "src/Ocular_Prediction/components/Data_ingestion.py",
    "src/Ocular_Prediction/components/Data_transformation.py",
    "src/Ocular_Prediction/components/Model_trainer.py",
    "src/Ocular_Prediction/components/Model_evaluation.py",
    "src/Ocular_Prediction/pipelines/__init__.py",
    "src/Ocular_Prediction/pipelines/Prediction_pipeline.py",
    "src/Ocular_Prediction/pipelines/Training_pipeline.py",

    "static/styles.css",
    "templates/index.html",
    "templates/result.html",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "README.md",
    "dvc.yaml",
    "requirements.txt",
    "setup.py"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass