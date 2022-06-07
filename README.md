# code-20220608-juanhuertas
Python BMI Calculator Offline Coding Challenge V7

** Problem Statement** 

Given the following JSON data
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
as the input with weight and height parameters of a person, we have to perform the following:
1) Calculate the BMI (Body Mass Index) using FormUla 1, BMI Category and Health risk
from Table 1 of the person and add them as 3 new columns
2) Count the total number of overweight people using ranges in the column BMI Category
of Table 1, check this is consistent programmatically and add any other observations in
the documentation
3) Create build, tests to make sure the code is working as expected and this can later be
added to an automation build / testing / deployment pipeline
4) Write a solid production-grade Python3 Program to solve this problem, imagine this will
be used in-product for 1 million patients. We are only interested in a standalone
backend application, we are NOT expecting a UI, webpage, frontend, Mobile App,
microsite, docker, web app etc. Simple and clean solution. Feel free to explore and use
the standard Python libraries or any open source Python modules
5) Check in the documentation, configuration, code and tests into github and please email
us the link with the URL pattern
https://www.github.com/<owner>/code-<date>-<your fullname> and do NOT
use Vamstar in URL, title or description. e.g. for me it could be
https://www.github.com/richard/code-20200917-richardfreeman


**Formula 1 - BMI**

**BMI(kg/m2) = mass(kg) / height(m)2**


The BMI (Body Mass Index) in (kg/m2
) is equal to the weight in kilograms (kg) divided by your
height in meters squared (m)2
. For example, if you are 175cm (1.75m) in height and 75kg in
weight, you can calculate your BMI as follows: 75kg / (1.75m²) = 24.49kg/m²

**Program skeleton**


