# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:08:26 2018

@author: HARIPRASADG
"""
#Example to deal with missing values

import pandas as pd
import numpy
import os
cwd = os.getcwd()
print(cwd)
url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
colNames=('pregnant_times','plasma_glucose','dia_bp','triceps_skinfold','serum_insulin','bmi','dia_pedigree','age_yrs','class_variable')
dataset = pd.read_csv(url,names=colNames)
dataset1 = pd.read_csv(url,names=colNames)
dataset2 = pd.read_csv(url,names=colNames)
summary = dataset.describe()
head = dataset.head(20)
#below are the variables of interest that cannot hold legitamate zero values. They are missing values.
zeroes = ((dataset[['plasma_glucose','dia_bp','triceps_skinfold','serum_insulin','bmi']]==0).sum())
#Replace the missing values with NaN
dataset[['plasma_glucose','dia_bp','triceps_skinfold','serum_insulin','bmi']] = dataset[['plasma_glucose','dia_bp','triceps_skinfold','serum_insulin','bmi']].replace(0,numpy.NaN)
nulls = dataset.isnull().sum()
#Dropping all the records with NaN values in dataset1
dataset1.shape
dataset1.dropna(inplace=True)
dataset1.shape
#Replacing all the null records with mean in dataset2
dataset2.shape
dataset2.fillna(dataset2.mean(),inplace=True)
dataset2.shape
#verifying the nulls in datasets
dataset.isnull().sum()
dataset1.isnull().sum()
dataset2.isnull().sum()
