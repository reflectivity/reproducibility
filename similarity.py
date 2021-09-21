# Code written by James Durant 2021 and adapted by Jos Cooper (jos.cooper@stfc.ac.uk)
# Takes two datasets and computes the Hotelling t^2 value and associated p-value (see for example https://en.wikipedia.org/wiki/Hotelling%27s_T-squared_distribution)
# Requires datasets to be at the same points (but calculates t_statistic irrespective of this being true)

import numpy as np
from scipy.stats import t

def similarity(data_1, data_2):
    """Determines whether there is significant difference between given
       `data_1` and `data_2` reflectivity datasets.
    Args:
        data_1 (tuple): measured reflectivity data with y errors. Expected [Q, r, dr] optional dQ
        data_2 (tuple): simulated reflectivity data with y errors.  Expected [Q, r, dr] optional dQ
    Returns:
        t_statistic (float): Hotelling T-squared statistic.
        pval (float): associated p-value for t-statistic.
    """
    r_data_1 = data_1[1]
    r_data_2 = data_2[1]
    assert(len(r_data_1) == len(r_data_2)), "These arrays are not the same length, please input data binnned and cropped to the same Q points"
    r_error_data_1 = data_1[2]
    r_error_data_2 = data_2[2]
    # Calculate the measured and reflected counts, taking the count as 0 if the reflectivity error is 0.
    counts_data_1 = np.divide(r_data_1, r_error_data_1,
                                out=np.zeros_like(r_data_1), where=r_error_data_1!=0)

    counts_data_2 = np.divide(r_data_2, r_error_data_2,
                                 out=np.zeros_like(r_data_2), where=r_error_data_2!=0)

    # Apply an Anscombe transformation to make the values approximately normal.
    # Then weight each value by 1 / standard deviation
    counts_data_1 = 2*np.sqrt(counts_data_1 + 3/8) / np.std(counts_data_1)
    counts_data_2 = 2*np.sqrt(counts_data_2 + 3/8) / np.std(counts_data_2)

    # Calculate the mean over the squared differences in reflectivity values.
    # Then take the square root of this value to get a Hotelling T-statistic.
    
    t_statistic = np.sqrt(np.mean(np.square(counts_data_1-counts_data_2)))

    # Get the associated p-value using the SciPy survival function.
    pval = t.sf(np.abs(t_statistic), len(r_data_1)-1)*2
    
    return t_statistic, pval
