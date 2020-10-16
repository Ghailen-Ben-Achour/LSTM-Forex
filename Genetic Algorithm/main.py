# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:11:27 2020

@author: msi
"""

import os
import evolution
import pandas as pd 

df1=pd.DataFrame()

model_path='./models/'
csv_path="./params.xls"
n_output=2
n = 28

def make_input_param(n):
    params ={}
    for i in range(n):
        params["p"+str(i)] = [0,1]
    return params


params = { "time":["h4", "h1"],
           
           "output":[0,1,2,3,4,5,6]
           }


params = {**params, **make_input_param(n)}
for _, _, files in os.walk(model_path):
    for file in files:
        for i in range(n_output):
            search = evolution.NeuroEvolution(generations = 2, population = 5, params=params)

            _,df=search.evolve(model_path=model_path+str(file),output=i)
            df1 = [df, df1]
            df1 = pd.concat(df1,ignore_index=True)
            # print(df1 )

df1.to_excel(csv_path)