# AUTOGENERATED! DO NOT EDIT! File to edit: 00_training.balance.ipynb (unless otherwise specified).

__all__ = ['downsample']

# Cell
import pandas as pd
import numpy as np

# Cell
def downsample(df:pd.DataFrame, y_column:str, random_state:int, min_size:int=None, **kwargs) -> pd.DataFrame:
    '''Balance classes of the target variable by downsampling all classes to be equal to or smaller than "min_size".

    Classes smaller than "min_size" are not affected and will remain at their current size. If "min_size" is ommitted,
    the size of the smallest current class is taken as "min_size".

    Paramters
    ---------
    df : pandas dataframe
         Dataframe containing column "y_column".

    y_column : str
               Name of df column containing the target variable (label).

    ranomd_state : int
                   Random state for reproducibility.

    min_size : int, default=None
               If no value is supplied, min_size will be set to the size of the smallest current class.

    Returns
    -------
    new_df : pandas dataframe
             Has the same structure as the input dataframe but classes were balanced by downsampling.

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