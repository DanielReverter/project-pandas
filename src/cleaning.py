import re
import pandas as pd
import numpy as np

# This file has all the cleaning functions that are used in the project


def duplicates(df):
    '''
    This function takes a dataframe, checks for pseudoduplicates (entries 
    that are almost identical to another one) and returns a dataframe with
    those duplicates deleted.
    
    
    Parameters
    ----------
    df : dataframe where we want pseudoduplicates to be removed

    Returns
    -------
    df2 : original dataframe with deleted pseudoduplicates

    '''
    counter = 0
    df2 = pd.DataFrame()
    indexes = df.index.values.tolist()
    for i in range(len(indexes)-1):
        data = df.iloc[[indexes[i]]]
        for column in df.columns:
                if df.at[indexes[i], column] == df.at[indexes[i+1], column]:
                    counter += 1
        if counter < 9:
            df2 = pd.concat([df2, data])
        counter = 0
    return df2


def surf(x):
    '''
    This function is used to clean data in the "Activity" column. If there is 
    the substring surf (or Surf), the function returns "Surfing". This is done
    to standarize data, so I don't miss any Surfing entry. I do this because 
    it will be relevant whenever I do the analysis.
    
    
    Parameters
    ----------
    x : dataframe cell that I want to check

    Returns
    -------
    "Surfing" : if I get a match
    x : if I don-t get a match (so any non-surfing entry ends unchanged)
    '''
    if re.search("[sS]urf", str(x)):
        return "Surfing"
    else:
        return x
    
    
def leg(x):
    '''
    This function will be used to check if the each string in the column
    "Injury" has any body related to legs (which are leg/s, feet/foot, 
    thigh/s and ankle/s, with any combination of upper/lower case letters)

    Parameters
    ----------
    x : the srting to check
    Returns
    -------
    "Y" if there is a match and "N" if there isn't'

    '''
    if re.search("\s?([lL][eE][gG][sS]?|[fF][eEoO][eEoO][tT]?|[tT][hH][iI][gG]\
                 [hH][sS]?|[aA][nN][kK][lL][eE][sS]?)\s?", str(x)):
        return "Y"
    else:
        return "N"
    
def age(x):
    '''
    This function will clean the "Age" column. It checks a string for the first
    ocurrence of double digits (ages from 10 to 99) and returns either it 
    (if there is a match) or the original string

    Parameters
    ----------
    x : The string I want to check for digits

    Returns
    -------
    If there is a match, it returns it. If there isn't, it returns the same
    parameter that was given to the function (but in a string so all cells 
    in that column will be strings)

    '''
    if re.findall("\d\d", str(x)):
        return re.findall("\d\d", str(x))[0]
    else:
        return str(x)
    
def male(x):
    '''
    This function checks if a string is "M " (with a space at the end), and 
    if it is, it changes it returns "M". Otherwise it returns the original 
    string.

    Parameters
    ----------
    x : the original string

    Returns
    -------
    "M" if there is a match or x if there isn't

    '''
    if re.search("M\s", str(x)):
        return "M"
    else:
        return x

def age2(x):
    '''
    This function further cleans the age column. If the string is either a 
    single digit or a double digit it returns it, and if it isn't it returns
    NaN

    Parameters
    ----------
    x : the string to check

    Returns
    -------
    Either the single/double digit or NaN

    '''
    if re.match("^\d\d?$", str(x)):
        return re.findall("^\d\d?$", str(x))[0]
    else:
        return np.nan