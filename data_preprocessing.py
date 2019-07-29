#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


class DataPrep:
    
    def __init__(self, df):
        
        self.df = df
        
    def change_numerical_nominal(self, columns):
        '''
        This method will change the list of columns or column of dataframe from numerical to categorical datatype(nominal)
        @param columns: list of columns

        '''

        for column in columns:
            if self.df[column].dtype == 'int64' or self.df[column] == 'float64':
                self.df[column] = self.df[column].astype('category')
                print('{} changed to nominal datatype'.format(column))
                
    def change_numerical_ordinal(self, columns, order):
        '''
        This method will change the list of columns or column of dataframe from numerical to categorical datatype(ordinal)
        @param order: order of ordinal columns
        @param columns: list of columns

        '''

        for col in columns:
            cat_order = pd.api.types.CategoricalDtype(categories=order, ordered=True)
            self.df[col] = self.df[col].astype(cat_order)
            print('{} changed to ordinal datatype'.format(col))

    def change_object_float(self, columns):

        '''
        This method will change the list of columns or column of dataframe from categorical to numerical datatype
        @param columns: list of columns

        '''

        for column in columns:
            self.df[column] = self.df[column].astype('float64')
            print('{} changed to float datatype'.format(column))   

# to find the percentage of missing values in columns 

    def find_missing_col(self):
        '''
        This method is used to find the columns which has the missing values, count of missing values and
        percentage of missing values.
        return: list of columns with missing values
        '''
        missing_col = [[i, self.df[i].isnull().sum(), "{0:.2f}".format(self.df[i].isnull().sum()*100/self.df.shape[0]),
                        self.df[i].dtype]
                       for i in self.df.columns if self.df[i].isnull().sum() > 0]
        return missing_col

# Deleting the rows where the missing values in columns are equal or less than 1 %.

    def delete_missing_1percent(self):
        '''
        This method is used to delete the rows where the columns with less than 1% of missing values are there.
        Most of the time we just want to remove those rows.
        return: dataframe
        '''
    
        missing_col = [[i,self.df[i].isnull().sum(),self.df[i].isnull().sum()*100/self.df.shape[0]] 
                       for i in self.df.columns if self.df[i].isnull().sum() > 0]  
        missing_col_1per = [i[0] for i in missing_col if i[2] <= 1]
        df = self.df.dropna(axis=0, how='any', subset=missing_col_1per)
        return df
    
    def impute_null(self, columns):
    
        '''
        This method is used to impute the missing values with 0 for numerical columns and NA for categorical columns.
        @param columns: list of columns
        '''
        for column in columns:
            if column == 'LotFrontage' or column == 'GarageYrBlt':
                self.df[column].fillna(value=0, inplace=True)
            else:
                self.df[column].fillna(value='NA', inplace=True)

