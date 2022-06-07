import pandas as pd
import json
import argparse
import yaml
import glob
from src.utils import *
import os


def main():
    # read cmd arguments
    parser = argparse.ArgumentParser("BMI Calculator")
    parser.add_argument("--conf_file", type=str, help="configuration file" ,required=True)
    args = parser.parse_args()

    # read yaml configuration file
    try:
        with open(args.conf_file, 'r') as f:
            dictionary =  yaml.safe_load(f)
    except:
        print("Wrong configuration File")
        exit(1)
    
    # read bmi configurations files
    try:
        with open(dictionary['conf_bmi'], 'r') as f: # read csv
            bmi_conf_df=  pd.read_json(f)
        with open(dictionary['conf_bmi'], 'r') as f: # read  in json
            d = json.load(f)
            
    except:
        print("Wrong BMI configuration File")
        exit(1)

    # files in input directory
    files = glob.glob(dictionary['input_folder'] + "/*.json")
    
    # if no new files exits
    if len(files) == 0:
        print("No files in input folder")
        exit(0)

    output_path = dictionary['output_folder']

    # if output directory dont exists, create it
    os.makedirs(output_path, exist_ok=True)
    # for each json file in the output directory
    for file in files:
        file_name = file.split("\\")[1].split(".")[0] # get the file name without extension
        data = pd.read_json(file) # read the json
        # calculate BMI index
        data['BMI'] = data.apply(lambda row: calculate_bmi_row(row), axis=1)
        # get BMI category and Health Risk category
        data[['BMI_Category', 'Health_risk']] = data.apply(lambda row: bmi_cat_health_risk(row, d), axis=1, result_type="expand")
        # serialize to dataframe to json to output directory
        data.to_json(output_path + f"/{file_name}_output.json", orient='records')


if __name__ == '__main__':


    main()
