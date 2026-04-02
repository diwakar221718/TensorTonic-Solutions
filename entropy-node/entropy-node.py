import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y=np.array(y)
    values, counts = np.unique(y, return_counts=True) # imp concepts
    p = counts/len(y)
    sum=0
    for i in p:
        sum=sum+(i*np.log2(i))

    return float(sum*(-1))


    
    