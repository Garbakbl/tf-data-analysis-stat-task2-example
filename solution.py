import numpy as np
from scipy.stats import chi2


chat_id = 356550601

def solution(p, x):
    n = len(x)
    s = np.sqrt(np.sum(x**2)/(n-1))
    alpha = 1 - p
    left = np.sqrt((n-1)*s**2/chi2.ppf(1-alpha/2, n-1))
    right = np.sqrt((n-1)*s**2/chi2.ppf(alpha/2, n-1))
    return (left, right)
