"""Util methods related to probability distributions."""

from numpy import arange

def check_prob_distribution(prob):
    """Chech wheter the vector is a probability distribution or not.
    All the values must be in the interval [0,1] and they must sum up to 1.
    It raises an error if the array is not a probability distribution or
    returns the input parameters if it is a valid probability distribution.
    """

    epsilon = 0.000001 # Used to compare probability distributions
    for i in arange(len(prob)):
        if prob[i] < 0 or prob[i] > 1:
            raise ValueError('The values must be in the interval [0,1]')
    
    prob_sum = sum(prob)
    if prob_sum < 1-epsilon or prob_sum > 1+epsilon:
        raise ValueError('All the values must sum up to 1 (with an error of ' +
                         'at most 1^(-6)')

    return prob