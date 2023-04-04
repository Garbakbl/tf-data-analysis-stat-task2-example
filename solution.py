import numpy as np
from scipy.stats import chi2

chat_id = 356550601

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    size = len(x)
    left = np.sqrt(size * (x ** 2).mean() / (35 * chi2.ppf(q=1 - alpha / 2, df=2 * size)))
    right = np.sqrt(size * (x ** 2).mean() / (35 * chi2.ppf(q=alpha / 2, df=2 * size)))
    return (left, right)
