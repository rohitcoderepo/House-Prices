#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import random




class BasicPlots:

    def __init__(self, df):
        self.df = df
        
    def density_plot(self, col, rng, color):
        '''
    This method will display the density plots of the specified columns. It is better to visualize not more than
    12 graphs at max.
    @param col: number of columns in graph
    @param rng: list of features whose density plot is required
    @param color: desired color for plot
    
        '''



        range_features = len(rng)

        print('Features : {}'.format(rng))

        if int(math.remainder(range_features, col)) == 0:
            rows = math.floor(range_features/col)
        else:
            rows = math.floor(range_features/col) + 1

        count = 0
        f, axes = plt.subplots(rows, col, figsize=(200, 200), sharex=False, sharey=False)
        x = 0
        y = 0

        for i in rng:
            sns.distplot(self.df[i], color=color, ax=axes[x, y], label='big')
    
            count += 1
            x = math.floor(count/col)
            if y < col-1:
                y += 1
            else:
                y = 0

    def scatter_plot(self, response, target):
        '''
         This method will create the scatter plot between the feature and target variable.
         It is useful to see the distribution of numerical feature against the target.
         :param response: feature in the dataframe
         :param target: target variable
         :param color: color of scatter ploy
         :return: scatter plot
        '''
        sns.set(font_scale=1.5, rc={"lines.linewidth": 1})
        ax = sns.scatterplot(x=response, y=target, data=self.df)

        return plt.show(ax)

    

