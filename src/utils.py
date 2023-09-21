import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score

from src.exception import CustomException


def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(file_path, 'wb') as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(x_train, y_train, x_test, y_test, models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(x_train, y_train)  # training the model

            y_train_pred = model.predict(x_train)  # predicting the model
            y_test_pred = model.predict(x_test)  # predicting the model

            train_model_score = r2_score(y_train, y_train_pred)  # calculating the r2 score
            test_model_score = r2_score(y_test, y_test_pred)  # calculating the r2 score

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)