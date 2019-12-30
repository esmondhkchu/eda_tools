import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def count_n_sort(in_arr, return_='total', ascending=True):
    """ count and sort an array, and return a dictionary

    Parameters: in_arr (tuple/list/array) - the input array
                return_ (str) - the return format, either
                                'total' for the actual count or
                                'percentage' for percenrage
                ascending (boolean) - ascending or descending

    Returns: count_ (dict) - counted and sorted in a dictionary, {val:count/percentage}
    """
    val, count = np.unique(in_arr, return_counts=True)
    if ascending == True:
        sorted_val = val[np.argsort(count)]
        sorted_count = np.sort(count)
    elif ascending == False:
        sorted_val = val[np.argsort(count)[::-1]]
        sorted_count = np.sort(count)[::-1]
    if return_ == 'total':
        count_ = {i:j for i,j in zip(sorted_val, sorted_count)}
    elif return_ == 'percentage':
        total = np.sum(sorted_count)
        count_ = {i:j for i,j in zip(sorted_val, sorted_count / total)}
    return count_

def plot_barh(in_arr, y_lab, y_index=0):
    """ plot a horizontal stacked barchart

    Parameters: in_arr (tuple/list/array like) - the input array
                y_lab (str) - y-label name for this array
                y_index (int) - y_index, the plot in which y-index location of a graph
                                optional, default is 0
    """
    dict_ = count_n_sort(in_arr, ascending=False, return_='percentage')
    val = np.append(0,np.cumsum(list(dict_.values())))
    for i in range(1,len(val)):
        plt.barh(y_lab, val[i]-val[i-1], left=val[i-1], color='azure', edgecolor='black')
    keys = list(dict_)
    for i in range(len(keys)):
        plt.annotate(keys[i], (val[i]+0.02, y_index), color='black', size=12)

def discrete_inspector(in_df, col_name=None):
    """ plot n features of a dataframe as n horizontal stacked barchart
        a tool to help inspect a feature characteristic

    Parameters: in_df (DataFrame) - the input DataFrame
                col_name (tuple/list/array like) - a list of feature names you want to inspect
                                                   optional, default is None, will plot all features
    """
    if col_name:
        for i,j in enumerate(col_name):
            plot_barh(in_df[j], j, i)
    else:
        for i,j in enumerate(list(in_df)):
            plot_barh(in_df[j], j, i)
    plt.ylabel('feature', size=15)
    plt.xlabel('density', size=15)
    sns.despine(top=True, right=True, left=True, bottom=True)

##
