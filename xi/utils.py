import itertools
from xi.exceptions import *
import numpy as np
from typing import *
from xi.separation.measure import *


def partition_validation(arg, k):
    """

    :param arg:
    :param k:
    :return:
    """
    if isinstance(arg,float):
        raise TypeError('Argument need to be a positive integer')

    if isinstance(arg,int):
        if arg <= 0:
            raise ValueError('Argument could only be a strictly positive integer'
                             'or a dictionary.')
    if isinstance(arg,dict):
        keys = len(list(arg.keys()))
        if keys>k:
            raise XiError("Number of keys of dictionary specifying partions"
                          "is greater than number of features")



def measurement_validation(measure: Union[List,AnyStr]):
    """

    :param measure:
    :return:
    """
    if isinstance(measure,str):
        measure = [measure]
    for m in measure:
        if m not in builder_mapping.keys():
            raise XiError(f"Separation measure {m} not implemented. Please choose "
                          f"one or more than one from {list(builder_mapping.keys().pop('Custom'))}")


def check_args_overlap(*args):

    overlap = []
    sets = tuple(set(d) for d in args)
    prods = itertools.combinations(sets,r=2)
    for s in prods:
        overlap.extend(set.intersection(*s))

    overlap = set(overlap)
    if len(overlap)>0:
        raise XiError(f"Parameter m, obs, discrete can\'t have the same keys.\n"
                      f"Overlapping keys {overlap}.\n"
                      f"Please specify parameters differently.")


def nrmd(x): # maybe this can be rewritten as a lambda function
    if np.sum(x) == 0:
        total = 1
    else:
        total = np.sum(x)
    return(np.divide(x, total))


