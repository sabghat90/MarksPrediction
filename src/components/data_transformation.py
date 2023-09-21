import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_obj


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('../../artifacts', 'preprocessor_obj.pkl')


def get_data_transformer_obj():
    """
    This function is used to get the data transformer object
    :return: data transformer object
    """
    try:
        numerical_columns = ['writing_score', 'reading_score']
        categorical_columns = [
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
        ]

        logging.info("Creating numerical pipeline")

        numerical_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ])

        logging.info("Creating categorical pipeline")

        categorical_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ("scaler", StandardScaler(with_mean=False)),
            ])
        logging.info("Numerical and Categorical pipeline created")

        logging.info("Creating column transformer")

        preprocessor = ColumnTransformer(
            [
                ("numerical_pipeline", numerical_pipeline, numerical_columns),
                ("categorical_pipeline", categorical_pipeline, categorical_columns),
            ]
        )
        logging.info("Column transformer created")

        return preprocessor

    except Exception as e:
        raise CustomException(e, sys)


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Initiating data transformation")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Data loaded successfully")

            logging.info("Getting data transformer object")
            preprocessor = get_data_transformer_obj()
            logging.info("Data transformer object created")

            target_column = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_features_train_df = train_df.drop(columns=[target_column], axis=1)
            target_features_train_df = train_df[target_column]

            input_features_test_df = test_df.drop(columns=[target_column], axis=1)
            target_features_test_df = test_df[target_column]

            logging.info("Fitting data transformer object")

            input_features_train_array = preprocessor.fit_transform(input_features_train_df)
            input_features_test_array = preprocessor.transform(input_features_test_df)

            logging.info("Data transformer object fitted")

            logging.info("Creating input features dataframe")
            train_arr = np.c_[
                input_features_train_array, np.array(target_features_train_df)
            ]
            test_arr = np.c_[
                input_features_test_array, np.array(target_features_test_df)
            ]
            logging.info("Input features dataframe created")

            save_obj(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor,
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
