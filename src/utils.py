import pandas as pd

def calculate_bmi(w: float, h: float)-> float:
    """
    calculate bmi index 
    BMI(kg/m2) = mass(kg) / height(m)2
    The BMI (Body Mass Index) in (kg/m2 ) is equal to the weight in kilograms (kg) divided by your height in meters squared (m)2

    # input 
    w -> float : weight
    h -> float : height
    # output
    bmi index -> float
    
    """
    return  float(w)/ ((float(h) /100) ** 2 )

def calculate_bmi_row(x: pd.Series)-> float:
    """
    calculate bmi for a pandas dataframe row
    
    # input 
    # x pandas.Series: is a pandas dataframe row
    # output
    bmi index -> float
    """
    return  calculate_bmi(float(x.WeightKg), float(x.HeightCm))

def bmi_cat_health_risk(x: pd.Series , dicc: dict):
    """
    return  bmi category and heath risk according to static data in dictionary
    
    # input 
    x -> pandas.Series: is a pandas dataframe row
    dicc -> dict : bmi category and health risk configuration . Static File bmi.json
    # output
    cat -> str : BMI Category
    hr -> str : Health Risk
    """
    bmi = float(x.BMI) # get the bmi index
    cat= None
    hr = None
    # get Category and Heath risk according to the bmi index configuration file
    for ele in dicc:
        # get the range in str and split using the - to get range inferior and superior 
        range_bmi = ele['Category_BMI_Range'].split('-')
        range_bmi_inf = float(range_bmi[0])
        range_bmi_sup = float(range_bmi[1])
        # if BMI index falls into range inf and range sup, get cat and hr, break loop and return values
        if bmi >= range_bmi_inf and bmi < range_bmi_sup:
            cat = ele['BMI']
            hr = ele['Health_risk']
            break
    return cat, hr

def count_label(df, label):
    """
    count number of ocurrences of BMI_Category on a dataframe df
    # input
    df -> pandas.DataFrame : input Dataframe
    label -> str : category to match
    # output
    int : number of ocurrences of that category
    """
    return len(df[df.BMI_Category==label])

