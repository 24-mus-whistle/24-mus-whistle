import numpy as np
import sklearn.utils

def reduce_and_reshuffle(X, y, ratio, random_state, label_whistle=1, label_no_whistle=-1):
    # indices of each class
    idx_whistle = np.where(y == label_whistle)[0]
    idx_no_whistle = np.where(y == label_no_whistle)[0]
    
    # shuffle indices
    idx_whistle = sklearn.utils.shuffle(idx_whistle, random_state=random_state)
    idx_no_whistle = sklearn.utils.shuffle(idx_no_whistle, random_state=random_state)
    
    # new number of samples for no whistle
    new_no_whistle_count = int(ratio * idx_whistle.shape[0])
    
    # select samples according to ratio
    X_new = np.concatenate((X[idx_whistle], X[idx_no_whistle][:new_no_whistle_count]))
    y_new = np.concatenate((y[idx_whistle], y[idx_no_whistle][:new_no_whistle_count]))
    
    # shuffle new data and labels
    shuffle_idx = sklearn.utils.shuffle(np.arange(y_new.shape[0]), random_state=random_state)
    X_new = X_new[shuffle_idx]
    y_new = y_new[shuffle_idx]
    
    return X_new, y_new
