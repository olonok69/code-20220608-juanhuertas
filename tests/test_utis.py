from src.utils import *
import unittest
import pandas as pd
import json



data_test = pd.DataFrame(data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 100 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 57 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 110},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}])

data_validation = pd.DataFrame(data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 , "BMI": 32.830615, "BMI_Category": "Moderately obese", "Health_risk": "Medium risk"},
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 100, "BMI": 38.578759, "BMI_Category": "Severely obese", "Health_risk": "High risk" },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 57 , "BMI": 17.592593, "BMI_Category": "Underweight", "Health_risk": "Malnutrition risk"},
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62 , "BMI": 22.499637, "BMI_Category": "Normal weight", "Health_risk": "Low risk"},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 110, "BMI": 48.888889, "BMI_Category": "Very severely obese", "Health_risk": "Very high risk"},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82, "BMI": 29.402273, "BMI_Category": "Overweight", "Health_risk": "Enhanced risk"}])

bmi_conf = """
[{"BMI":"Underweight","Category_BMI_Range":"0-18.4","Health_risk":"Malnutrition risk"},
{"BMI":"Normal weight","Category_BMI_Range":"18.5-24.9","Health_risk":"Low risk"},
{"BMI":"Overweight","Category_BMI_Range":"25-29.9","Health_risk":"Enhanced risk"},
{"BMI":"Moderately obese","Category_BMI_Range":"30-34.9","Health_risk":"Medium risk"},
{"BMI":"Severely obese","Category_BMI_Range":"35-39.9","Health_risk":"High risk"},
{"BMI":"Very severely obese","Category_BMI_Range":"40-9999","Health_risk":"Very high risk"}]"""


class Test_utils_bmi(unittest.TestCase):
    def test_calculate_bmi(self):
        weight = 195 # cm
        height = 75 # kg

        assert  float(weight)/ ((float(height) /100) ** 2 ) ==  calculate_bmi(weight, height)

    def test_calculate_bmi_row(self):
        data_test['BMI']= data_test.apply(lambda row: calculate_bmi_row(row), axis=1)
        pd.testing.assert_frame_equal(data_test[['BMI']], data_validation[['BMI']])

    def test_bmi_cat_health_risk(self):
        d = json.loads(bmi_conf)
        data_test['BMI']= data_test.apply(lambda row: calculate_bmi_row(row), axis=1)
        data_test[['BMI_Category', 'Health_risk']] = data_test.apply(lambda row: bmi_cat_health_risk(row, d), axis=1, result_type="expand")
        pd.testing.assert_frame_equal(data_test[['BMI_Category', 'Health_risk']], data_validation[['BMI_Category', 'Health_risk']])

    def test_count_label(self):
        assert count_label(data_validation, "Moderately obese") == 1
        assert count_label(data_validation, "Severely obese") == 1
        assert count_label(data_validation, "Underweight") == 1
        assert count_label(data_validation, "Normal weight") == 1
        assert count_label(data_validation, "Moderately obese") == 1
        assert count_label(data_validation, "Overweight") == 1
        assert count_label(data_validation, "Moderately not obese") == 0
