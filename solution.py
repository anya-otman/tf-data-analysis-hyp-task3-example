import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1105842906

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    t_stat, p_value = ttest_ind(x, y, equal_var=False)
    
    return p_value < alpha
