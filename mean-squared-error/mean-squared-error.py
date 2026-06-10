import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    n=len(y_true)
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)
    mse=(y_true-y_pred)**2
    sum=0
    for i in range(n):
        sum+=mse[i]

    return sum/n    
    
    