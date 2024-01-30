# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:56:14 2024

@author: patel
"""

import pandas as pd
file = pd.read_csv("iris.csv")

"""
Absolute Path:
C:/Users?BBarsch.CSIR/css2024_day02/data_02/iris.csv

Relative Path:
data_02/iris.csv
"""

file = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

file = pd.read_csv(url)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

file = pd.read_csv(url, header=None, names = column_names)

file = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

file = pd.read_excel("data_02/residentdoctors.xlsx")

file = pd.read_json("data_02/student_data.json")

print(file)

url = https;//raw.githubusercontent.com/Asabele240702/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv
