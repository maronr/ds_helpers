# AUTOGENERATED! DO NOT EDIT! File to edit: 00_training.balance.ipynb (unless otherwise specified).

__all__ = ['downsample']

# Cell
import pandas as pd
import numpy as np

# Cell
def downsample(df:pd.DataFrame, y_column:str, min_size:int=None, random_state:int=115, **kwargs) -> pd.DataFrame:
    '''Balance classes of the target variable by downsampling all classes to be equal to or smaller than "min_size".

    Classes smaller than "min_size" are not affected and will remain at their current size. If "min_size" is ommitted,
    the size of the smallest current class is taken as "min_size".
    '''
    df_new = df.copy()

    # get smallest current class if not supplied
    if min_size == None:
        min_size = df_new[y_column].value_counts().min()

    # downsample all classes larger than min_size
    for class_index, group in df_new.groupby(y_column):
        if group.shape[0] > min_size:
            drop_idx = group.sample(len(group)-min_size, random_state=random_state, **kwargs).index
            df_new = df_new.drop(drop_idx)

    return df_new.reset_index(drop=True)